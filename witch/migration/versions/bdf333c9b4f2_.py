"""Set gender column based on member id

Revision ID: bdf333c9b4f2
Revises: a952771a97dc
Create Date: 2020-09-08 15:02:44.524685

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy import orm

from witch.models.member import Member

# revision identifiers, used by Alembic.
revision = 'bdf333c9b4f2'
down_revision = 'a952771a97dc'
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    members = session.query(Member)
    for member in members:
        if member.id % 2 == 0:
            member.gender = 'male'
        else:
            member.gender = 'female'

    session.commit()


def downgrade():
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    members = session.query(Member)
    for member in members:
        member.gender = 'male'

    session.commit()
    
