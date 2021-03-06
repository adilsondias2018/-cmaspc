"""empty message

Revision ID: ab0dd33ee3dc
Revises: 1cd8a02b6c08
Create Date: 2021-08-10 09:36:03.904600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab0dd33ee3dc'
down_revision = '1cd8a02b6c08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('cadastro_cpf_key', 'cadastro', type_='unique')
    op.drop_constraint('cadastro_email_key', 'cadastro', type_='unique')
    op.drop_constraint('cadastro_identidade_key', 'cadastro', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('cadastro_identidade_key', 'cadastro', ['identidade'])
    op.create_unique_constraint('cadastro_email_key', 'cadastro', ['email'])
    op.create_unique_constraint('cadastro_cpf_key', 'cadastro', ['cpf'])
    # ### end Alembic commands ###
