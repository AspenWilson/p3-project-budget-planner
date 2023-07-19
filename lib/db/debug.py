from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Budget, Expense, Income, IncomeType

if __name__ == '__main__':
    engine = create_engine('sqlite:///budget_planner.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()