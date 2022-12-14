"""add_password_column

Revision ID: 25afaa270b96
Revises: 1ee28f529496
Create Date: 2022-08-21 19:02:52.604563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25afaa270b96'
down_revision = '1ee28f529496'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    # ### end Alembic commands ###
