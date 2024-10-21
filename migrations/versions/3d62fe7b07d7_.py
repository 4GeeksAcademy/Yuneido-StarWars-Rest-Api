"""empty message

Revision ID: 3d62fe7b07d7
Revises: a5cffa318ac2
Create Date: 2024-10-17 20:35:46.445244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d62fe7b07d7'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('films',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=25), nullable=True),
    sa.Column('episode_number', sa.Integer(), nullable=True),
    sa.Column('director', sa.String(length=50), nullable=True),
    sa.Column('productor', sa.String(length=50), nullable=True),
    sa.Column('release_date', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('episode_number')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('terrain', sa.String(length=100), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('climate', sa.String(length=50), nullable=True),
    sa.Column('gravity', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('item_type', sa.Enum('PLANETS', 'PEOPLE', name='fav_types'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('films_planets',
    sa.Column('film_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['film_id'], ['films.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], )
    )
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('gender', sa.String(length=50), nullable=True),
    sa.Column('eye_color', sa.String(length=50), nullable=True),
    sa.Column('hair_color', sa.String(length=50), nullable=True),
    sa.Column('height', sa.String(length=50), nullable=True),
    sa.Column('home_world', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['home_world'], ['planets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('films_people',
    sa.Column('film_id', sa.Integer(), nullable=True),
    sa.Column('people_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['film_id'], ['films.id'], ),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], )
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('name')

    op.drop_table('films_people')
    op.drop_table('people')
    op.drop_table('films_planets')
    op.drop_table('favorite')
    op.drop_table('planets')
    op.drop_table('films')
    # ### end Alembic commands ###