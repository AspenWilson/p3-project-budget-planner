from models import Budget, Expense, Income, IncomeType, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

class Welcome:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def welcome_message(self):
        print("Welcome to your Budget Planner CLI!")
        print("-----------------------------------")
        print("You have many options to choose from to help you set and maintain your budget. Your options are listed below. To call these commands, simply enter python cli.py and then enter the number of the command. If you ever need to see your options, type python cli.py 0 into your terminal")
        print("--> 1. View: This shows you your current budgets, broken out by category.")
        print("--> Add Expense: This is where you can add a new expense.")
        print("--> Add Income: This is where you can add income.")
        print("--> Set Budget: This is where you can set the budget for each category based on a percentage of your monthly income.")
        print("--> Summary: This is where you can see a brief summary of your total income, total expenses, and your remaining budget.")
        print("--> Delete Expense: This is where you can delete an expense using the expense ID.")

#views and summaries

    def view_budget(self):
        categories = self.session.query(Category).all()

        for category in categories:
            print(f'{category.name}: Budget - ${category.budget:.2f}')
            print('Expenses')
            
            expenses = category.expenses
            if expenses:
                for expense in expenses:
                    print(f'\t{expense.name}: ${expense.amount:.2f}')
            else:
                print('\tNo expenses for this category.')
            
            print()

    def summary(self):
        total_income = sum([income.amount for income in self.session.query(Income).all()])
        total_expenses = sum([expense.amount for expense in self.session.query(Expense).all()])

        print (f"\nTotal Income: ${total_income:.2f}")
        print (f"Total Expenses: ${total_expenses:.2f}")
        print (f"Remaining Budget: ${total_income - total_expenses:.2f}\n")


    
