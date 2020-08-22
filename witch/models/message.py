from restfulpy.orm import Field, DeclarativeBase, OrderingMixin, \
    FilteringMixin, PaginationMixin, relationship
from sqlalchemy import Integer, Unicode, DateTime, ForeignKey, Enum, exists, \
    and_, UniqueConstraint, select, String
from sqlalchemy.orm import sessionmaker, object_session, relationship, \
    column_property

from .target import Target


class Message(OrderingMixin, FilteringMixin, PaginationMixin, DeclarativeBase):
    __tablename__ = 'message'

    id = Field(
        Integer,
        primary_key=True,
        readonly=True,
        not_none=True,
        required=False,
        label='ID',
        minimum=1,
    )
    body = Field(
        String(200),
    )
    sender_id = Field(
        Integer,
        ForeignKey('user.id'),
    )
    target_id = Field(
        Integer,
        ForeignKey('target.id'),
    )
    target_title = column_property(
        select([Target.title]) \
            .where(Target.id == id)
    )
