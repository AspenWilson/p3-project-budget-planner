"""Added variance column

Revision ID: 07a63cb538c5
Revises: e825987f7464
Create Date: 2023-07-18 07:40:56.679387

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07a63cb538c5'
down_revision = 'e825987f7464'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('actual', sa.Float(), nullable=True))
    op.add_column('categories', sa.Column('variance', sa.Float(), nullable=True))
    op.add_column('income_type', sa.Column('expected', sa.Float(), nullable=True))
    op.add_column('income_type', sa.Column('actual', sa.Float(), nullable=True))
    op.add_column('income_type', sa.Column('variance', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('income_type', 'variance')
    op.drop_column('income_type', 'actual')
    op.drop_column('income_type', 'expected')
    op.drop_column('categories', 'variance')
    op.drop_column('categories', 'actual')
    # ### end Alembic commands ###