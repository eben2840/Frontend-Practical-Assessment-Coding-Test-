"""empty message

Revision ID: 15575f46000d
Revises: 1dbe3c39f2cd
Create Date: 2024-05-24 01:57:34.876191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15575f46000d'
down_revision = '1dbe3c39f2cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('groups', schema=None) as batch_op:
        batch_op.drop_column('start_date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('groups', schema=None) as batch_op:
        batch_op.add_column(sa.Column('start_date', sa.DATE(), nullable=True))

    # ### end Alembic commands ###
