"""empty message

Revision ID: 178dc95b3c8d
Revises: e5ee41306ede
Create Date: 2020-09-05 12:39:23.286603

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '178dc95b3c8d'
down_revision = '6236ea34c1f4'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        "CREATE TYPE member_gender AS ENUM ('male', 'female');"
    )
    op.add_column(
        'member',
        sa.Column(
            'gender',
            sa.Enum(
                'male',
                'female',
                name='member_gender'
            ),
            nullable=True,
        )
    )
    op.execute("UPDATE member SET gender = 'male';")


def downgrade():
    op.drop_column('member', 'gender')
    op.execute(
        "DROP TYPE member_gender;"
    )
