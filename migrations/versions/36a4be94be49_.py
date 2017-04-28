"""empty message

Revision ID: 36a4be94be49
Revises: 
Create Date: 2017-04-28 21:40:57.886676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36a4be94be49'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('badge_type', sa.String(length=64), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('serial_number', sa.String(length=14), nullable=True),
    sa.Column('creation_date', sa.Interval(), nullable=True),
    sa.Column('valid_from', sa.Interval(), nullable=True),
    sa.Column('valid_until', sa.Interval(), nullable=True),
    sa.Column('revoked', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_card_serial_number'), 'card', ['serial_number'], unique=False)
    op.create_index(op.f('ix_card_user_id'), 'card', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_card_user_id'), table_name='card')
    op.drop_index(op.f('ix_card_serial_number'), table_name='card')
    op.drop_table('card')
    # ### end Alembic commands ###