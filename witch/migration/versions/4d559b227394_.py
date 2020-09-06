"""Add new column gender to member model

Revision ID: 4d559b227394
Revises: 6236ea34c1f4
Create Date: 2020-09-05 16:44:44.413774

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '4d559b227394'
down_revision = '4ce3bd840d5a'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE TYPE member_gender AS ENUM ('male', 'female');")
    op.execute("CREATE TYPE member_gender AS ENUM ('male', 'female');")
    op.add_column(
        'member',
        sa.Column(
            'gender',
            sa.Enum('male', 'female', name='member_gender'),
            nullable=True,
        )
    )
    op.execute("UPDATE member SET gender = 'male';")
    op.execute('ALTER TABLE member ALTER COLUMN gender SET NOT NULL;')


def downgrade():
    op.drop_column('member', 'gender')
    op.execute("DROP TYPE member_gender;")

