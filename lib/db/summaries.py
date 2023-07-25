from datetime import datetime
from sqlalchemy import extract, func
from sqlalchemy.orm import sessionmaker
from models import Budget, Expense, Income, IncomeType, engine
from helpers import current_month, current_year, line_print, get_total, get_all

    
class MonthSummary:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def view_monthly_summary(self):

        print('Command 3: View your monthly summary for teh current month')
        line_print()

        total_expenses = get_total(self.session, Expense, current_month, current_year)

        total_income = get_total(self.session, Income, current_month, current_year)

        budget = self.session.query(func.sum(Budget.budget)).scalar()

        print(f"Summary for {datetime.now().strftime('%B %Y')}:")
        print(f"Total Monthly Expenses: ${total_expenses:.2f}")
        print(f"Total Monthly Income: ${total_income:.2f}")
        print(f"Monthly Budget: ${budget:.2f}")
        print(f"Income-to-Expenses Variance: ${total_income - total_expenses:.2f}")
    
    def view_monthly_expenses(self):

        print(f'Command 1: View all expenses for {current_year}')
        line_print()

        for budget in get_all(self.session, Budget):
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
        total_income = sum([income.amount for income in get_all(self.session, Income)])
        total_expenses = sum([expense.amount for expense in get_all(self.session, Expense)])

        print (f"\nTotal Income: ${total_income:.2f}")
        print (f"Total Expenses: ${total_expenses:.2f}")
        print (f"Remaining Budget: ${total_income - total_expenses:.2f}\n")