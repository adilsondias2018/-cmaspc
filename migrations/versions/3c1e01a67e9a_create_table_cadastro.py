"""create table Cadastro

Revision ID: 3c1e01a67e9a
Revises: 
Create Date: 2021-08-09 23:43:40.843694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c1e01a67e9a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cadastro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=255), nullable=False),
    sa.Column('dataNascimento', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('cpf', sa.String(length=20), nullable=False),
    sa.Column('identidade', sa.String(length=20), nullable=False),
    sa.Column('telefone', sa.String(length=20), nullable=False),
    sa.Column('segmentoAtuacao', sa.String(length=20), nullable=False),
    sa.Column('tipoSegmento', sa.String(length=20), nullable=False),
    sa.Column('participacao', sa.String(), nullable=False),
    sa.Column('conselheiro', sa.String(length=3), nullable=False),
    sa.Column('candidato', sa.String(length=3), nullable=False),
    sa.Column('eixos', sa.String(length=6), nullable=False),
    sa.Column('termo', sa.String(length=5), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('identidade')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cadastro')
    # ### end Alembic commands ###