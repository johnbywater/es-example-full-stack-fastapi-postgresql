from eventsourcing.application.sqlalchemy import SQLAlchemyApplication
from eventsourcing.domain.model.aggregate import BaseAggregateRoot

from app.db.session import db_session


def test_application():

    with SQLAlchemyApplication(
        session=db_session, persist_event_type=BaseAggregateRoot.Event
    ) as app:
        aggregate = BaseAggregateRoot.__create__()
        aggregate.__save__()

        copy = app.repository[aggregate.id]
        assert isinstance(copy, BaseAggregateRoot)
