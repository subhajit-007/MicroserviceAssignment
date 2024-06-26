"""empty message

Revision ID: 2d26951e2327
Revises: 
Create Date: 2024-04-29 10:17:00.142918

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d26951e2327'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account_detail',
    sa.Column('account_no', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('balance', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('account_no')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('account_detail')
    # ### end Alembic commands ###
