"""Initial migration

Revision ID: e563b79cf394
Revises: 
Create Date: 2024-01-23 17:44:28.852625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e563b79cf394'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('end_device',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('ip_address', sa.String(length=15), nullable=False),
    sa.Column('memory_usage', sa.Float(), nullable=True),
    sa.Column('cpu_usage', sa.Float(), nullable=True),
    sa.Column('disk_usage', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ip_address')
    )
    op.create_table('io_t_device',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('topic', sa.String(length=50), nullable=False),
    sa.Column('temperature', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('topic')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('io_t_device')
    op.drop_table('end_device')
    op.drop_table('city')
    # ### end Alembic commands ###
