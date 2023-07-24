from datetime import datetime
from sqlalchemy import extract, func
from sqlalchemy.orm import sessionmaker
from models import Budget, Expense, Income, IncomeType, engine
from helpers import all_categories, current_month, current_year, get_total_expenses, get_total_income, line_print

    
class MonthSummary:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get_budget(self, month, year):
        budget = self.session.query(func.sum(Budget.budget)).scalar()
        return budget or 0.0

    def view_monthly_summary(self):

        print(f'Command 3: View your monthly summary for {current_month}/{current_year}')
        line_print()

        total_expenses = get_total_expenses(self.session, current_month, current_year)

        total_income = get_total_income(self.session, current_month, current_year)

        budget = self.get_budget(current_month, current_year)

        print(f"Summary for {datetime.now().strftime('%B %Y')}:")
        print(f"Total Monthly Expenses: ${total_expenses:.2f}")
        print(f"Total Monthly Income: ${total_income:.2f}")
        print(f"Monthly Budget: ${budget:.2f}")
        print(f"Income-to-Expenses Variance: ${total_income - total_expenses:.2f}")
    
    def view_monthly_expenses(self):

        print(f'Command 1: View all expenses for {current_year}')
        line_print()

        for budget in all_categories:
            print(f'{budget.category}:')
            print('Expenses')

            expenses = [expense for expense in budget.expenses if expense.date.year == current_year]
            if expenses:
                for expense in expenses:
                    print(f'\t{expense.description}: ${expense.amount:.2f}')
            else:
                print('\tNo expenses for this category.')

            print()

    def summary(self):
        total_income = sum([income.amount for income in self.session.query(Income).all()])
        total_expenses = sum([expense.amount for expense in self.session.query(Expense).all()])