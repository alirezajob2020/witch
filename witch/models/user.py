from restfulpy.orm import Field, DeclarativeBase, OrderingMixin, \
    FilteringMixin, PaginationMixin, relationship
from sqlalchemy import Integer, Unicode, DateTime, ForeignKey, Enum, exists, \
    and_, UniqueConstraint, String


class User(OrderingMixin, FilteringMixin, PaginationMixin, DeclarativeBase):
    __tablename__ = 'user'

    id = Field(
        Integer,
        primary_key=True,
        readonly=True,
        not_none=True,
        required=False,
        label='ID',
        minimum=1,
    )
    title = Field(
        String(50)
    )
    first_name = Field(
        String(50),
    )
    last_name = Field(
        String(50),
    )
    birth_date = Field(
        DateTime,
    )
    email = Field(
        String,
    )
