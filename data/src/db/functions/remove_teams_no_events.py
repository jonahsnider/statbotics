from sqlalchemy.orm import Session as SessionType
from sqlalchemy_cockroachdb import run_transaction  # type: ignore

from src.db.main import Session
from src.db.models.team import TeamORM
from src.db.models.team_event import TeamEventORM
from src.db.models.team_year import TeamYearORM


def remove_teams_with_no_events() -> None:
    def callback(session: SessionType):
        teams = [
            x[0]
            for x in session.query(TeamEventORM.team)  # type: ignore
            .group_by(TeamEventORM.team)
            .all()
        ]

        # Filter teams, teamYears with no events
        session.query(TeamYearORM).filter(TeamYearORM.team.notin_(teams)).delete()  # type: ignore
        session.query(TeamORM).filter(TeamORM.team.notin_(teams)).delete()  # type: ignore

    return run_transaction(Session, callback)  # type: ignore
