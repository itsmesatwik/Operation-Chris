"""empty message

Revision ID: cecb04c85dc5
Revises: ab24561bfba2
Create Date: 2017-12-07 16:03:10.351266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cecb04c85dc5'
down_revision = 'ab24561bfba2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('food', 'name_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('food', 'name_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###