"""set gender column based on member id

Revision ID: bdf333c9b4f2
Revises: a952771a97dc
Create Date: 2020-09-08 15:02:44.524685

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'bdf333c9b4f2'
down_revision = 'a952771a97dc'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("UPDATE member SET gender = 'male' WHERE (member.id % 2) = 0 ;")
    op.execute("UPDATE member SET gender = 'female' WHERE (member.id % 2) = 1;")


def downgrade():
    op.execute("UPDATE member SET gender = 'male';")

