"""alter user table

Revision ID: 35ecdbff1b14
Revises: 
Create Date: 2020-09-01 10:00:54.987623

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '35ecdbff1b14'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('user', 'member')
    op.execute('ALTER SEQUENCE user_id_seq RENAME TO member_id_seq')


def downgrade():
    op.rename_table('member', 'user')
    op.execute('ALTER SEQUENCE member_id_seq RENAME TO user_id_seq')

