from typing import List, Optional

from sqlalchemy.orm.session import Session as SessionType
from sqlalchemy_cockroachdb import run_transaction  # type: ignore

from src.db.main import Session
from src.db.models.event import Event, EventORM


def get_events(year: Optional[int] = None, id: Optional[int] = None) -> List[Event]:
    def callback(session: SessionType):
        data = session.query(EventORM)  # type: ignore
        if year is not None:
            data = data.filter(EventORM.year == year)  # type: ignore
        if id is not None:
            data = data.filter(EventORM.id == id)  # type: ignore
        data: List[EventORM] = data.all()  # type: ignore
        return [Event.from_dict(x.__dict__) for x in data]

    return run_transaction(Session, callback)  # type: ignore


def get_num_events() -> int:
    def callback(session: SessionType):
        return session.query(EventORM).count()  # type: ignore

    return run_transaction(Session, callback)  # type: ignore
