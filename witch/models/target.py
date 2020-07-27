from restfulpy.orm import Field, DeclarativeBase, OrderingMixin, \
    FilteringMixin, PaginationMixin, relationship
from sqlalchemy import Integer, Unicode, DateTime, ForeignKey, Enum, exists, \
    and_, UniqueConstraint

from .user import User



class Target(OrderingMixin, FilteringMixin, PaginationMixin, DeclarativeBase):
    __tablename__ = 'target'

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
        String(50),
    )
    creator_id = Field(
        Integer,
        ForeignKey('user.id'),
    )
    admin_id = Field(
        Integer,
        ForeignKey('user.id'),
    )


class TargetMember(Base):
    __tablename__ = 'target_member'

    user_id = Field(
        Integer,
        ForeignKey('user.id'),
        primary_key=True,
    )
    target_id = Field(
        Integer,
        ForeignKey('target.id'),
        primary_key=True,
    )
    extra_data = Field(
        String(50),
    )

    target = relationship(
        'Target',
        back_populates='users',
    )
    user = relationship(
        'User',
        back_populates='targets',
    )
