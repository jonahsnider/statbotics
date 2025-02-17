from typing import List, Optional

from sqlalchemy.orm.session import Session as SessionType
from sqlalchemy_cockroachdb import run_transaction  # type: ignore

from src.db.main import Session
from src.db.models.team_match import TeamMatch, TeamMatchORM


def get_team_matches(
    year: Optional[int] = None, event: Optional[int] = None
) -> List[TeamMatch]:
    def callback(session: SessionType):
        data = session.query(TeamMatchORM)  # type: ignore
        if year is not None:
            data = data.filter(TeamMatchORM.year == year)  # type: ignore
        if event is not None:
            data = data.filter(TeamMatchORM.event_id == event)  # type: ignore
        data: List[TeamMatchORM] = data.all()  # type: ignore
        return [TeamMatch.from_dict(x.__dict__) for x in data]

    return run_transaction(Session, callback)  # type: ignore


def get_num_team_matches() -> int:
    def callback(session: SessionType):
        return session.query(TeamMatchORM).count()  # type: ignore

    return run_transaction(Session, callback)  # type: ignore
