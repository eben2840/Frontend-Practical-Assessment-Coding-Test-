"""empty message

Revision ID: 5cfa0ff0ddf5
Revises: 25b74c03536b
Create Date: 2024-04-17 09:35:39.315869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5cfa0ff0ddf5'
down_revision = '25b74c03536b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hospital', schema=None) as batch_op:
        batch_op.add_column(sa.Column('staff_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'user', ['staff_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hospital', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('staff_id')

    # ### end Alembic commands ###
