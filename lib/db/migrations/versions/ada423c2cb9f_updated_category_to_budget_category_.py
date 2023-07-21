"""Updated Category to Budget, category.name to budget.category and Expense.name to Expense.description

Revision ID: ada423c2cb9f
Revises: 58af5aa2a86b
Create Date: 2023-07-19 08:51:38.763705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ada423c2cb9f'
down_revision = '58af5aa2a86b'
branch_labels = None
depends_on = None


def upgrade():
    pass



def downgrade(): 
    pass
    # ### end Alembic commands ###
