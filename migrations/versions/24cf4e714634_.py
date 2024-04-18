"""empty message

Revision ID: 24cf4e714634
Revises: a0dccab9f850
Create Date: 2024-04-17 16:24:36.631460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24cf4e714634'
down_revision = 'a0dccab9f850'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hospital', schema=None) as batch_op:
        batch_op.add_column(sa.Column('clientname', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hospital', schema=None) as batch_op:
        batch_op.drop_column('clientname')

    # ### end Alembic commands ###
