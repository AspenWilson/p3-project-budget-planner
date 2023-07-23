from models import Budget, Expense, Income, IncomeType, engine
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()

all_categories = session.query(Budget).all()
all_expenses = session.query(Expense).all()
all_income_types = session.query(IncomeType).all()
all_income_entries = session.query(Income).all()

