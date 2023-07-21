from datetime import datetime
from sqlalchemy import extract, func
from sqlalchemy.orm import sessionmaker
from models import Budget, Expense, Income, IncomeType, engine

    
class MonthSummary:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get_total_expenses(self, month, year):
        total_expenses = self.session.query(func.sum(Expense.amount)).filter(extract('month', Expense.date) == month, extract('year', Expense.date) == year).scalar()
        return total_expenses or 0.0

    def get_total_income(self, month, year):
        total_income = self.session.query(func.sum(Income.amount)).filter(extract('month', Income.date) == month, extract('year', Income.date) == year).scalar()
        return total_income or 0.0

    def get_budget(self, month, year):
        budget = self.session.query(func.sum(Budget.budget)).scalar()
        return budget or 0.0

    def view_monthly_summary(self):
        
        current_month = datetime.now().month
        current_year = datetime.now().year

        total_expenses = self.get_total_expenses(current_month, current_year)

        total_income = self.get_total_income(current_month, current_year)

        budget = self.get_budget(current_month, current_year)

        print(f"Summary for {datetime.now().strftime('%B %Y')}:")
        print(f"Total Monthly Expenses: ${total_expenses:.2f}")
        print(f"Total Monthly Income: ${total_income:.2f}")
        print(f"Monthly Budget: ${budget:.2f}")
        print(f"Variance: ${budget - total_expenses:.2f}")


    def summary(self):
        total_income = sum([income.amount for income in self.session.query(Income).all()])
        total_expenses = sum([expense.amount for expense in self.session.query(Expense).all()])