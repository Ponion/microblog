"""add language to posts

Revision ID: 19d2c636f8f1
Revises: 41137024c7ce
Create Date: 2024-03-22 20:19:41.817840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19d2c636f8f1'
down_revision = '41137024c7ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('language', sa.String(length=5), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('language')

    # ### end Alembic commands ###
