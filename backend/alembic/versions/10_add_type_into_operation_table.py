"""Add type into operation table

Revision ID: 7b423f8654e8
Revises: b833b8cae2bc
Create Date: 2023-03-20 00:46:12.372499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b423f8654e8'
down_revision = 'b833b8cae2bc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('operation_table', sa.Column('type', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('operation_table', 'type')
    # ### end Alembic commands ###