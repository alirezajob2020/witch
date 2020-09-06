"""Drop birthdate column

Revision ID: 4ce3bd840d5a
Revises: 6236ea34c1f4
Create Date: 2020-09-06 12:42:58.497405

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4ce3bd840d5a'
down_revision = '6236ea34c1f4'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('member', 'birth_date')


def downgrade():
    op.add_column('member', sa.Column('birth_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))

