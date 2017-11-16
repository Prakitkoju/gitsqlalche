"""empty message

Revision ID: 1391c48a7654
Revises: 178a3d28c247
Create Date: 2017-11-16 18:06:25.766748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1391c48a7654'
down_revision = '178a3d28c247'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'create_date')
    op.drop_column('users', 'remarks2')
    op.drop_column('users', 'lock')
    op.drop_column('users', 'modify_date')
    op.drop_column('users', 'remarks1')
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('remarks1', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('modify_date', sa.DATE(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('lock', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('remarks2', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('create_date', sa.DATE(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
