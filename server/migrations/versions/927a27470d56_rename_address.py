"""rename address

Revision ID: 927a27470d56
Revises: ac8cb13fb212
Create Date: 2023-11-14 22:38:31.041441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '927a27470d56'
down_revision = 'ac8cb13fb212'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address', new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location', new_column_name='address')
    # ### end Alembic commands ###