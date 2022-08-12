"""empty message

Revision ID: 8b20e3133ed9
Revises: 5d8a28b752c1
Create Date: 2022-08-12 15:02:36.432469

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b20e3133ed9'
down_revision = '5d8a28b752c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('show', 'image_link')
    op.drop_column('show', 'venue_name')
    op.drop_column('show', 'artist_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('show', sa.Column('artist_name', sa.VARCHAR(length=2000), autoincrement=False, nullable=True))
    op.add_column('show', sa.Column('venue_name', sa.VARCHAR(length=5000), autoincrement=False, nullable=True))
    op.add_column('show', sa.Column('image_link', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    # ### end Alembic commands ###