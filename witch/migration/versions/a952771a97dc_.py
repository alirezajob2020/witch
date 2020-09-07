"""Add new value to member_gender Enum

Revision ID: a952771a97dc
Revises: 4d559b227394
Create Date: 2020-09-06 16:53:44.887983

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'a952771a97dc'
down_revision = '4d559b227394'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('COMMIT')
    op.execute('ALTER TYPE member_gender ADD VALUE \'other\'')


def downgrade():
    pass

