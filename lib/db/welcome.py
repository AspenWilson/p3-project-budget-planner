from models import Budget, Expense, Income, IncomeType, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

class Welcome:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def welcome_message(self):
        print("-----------------------------------")
        print("Welcome to your Budget Planner CLI!")
        print("-----------------------------------")
        print("You have many options to choose from to help you set and maintain your budget. Your options are listed below. To call these commands, simply enter python cli.py and then enter the letter/number of the command. If you ever need to see your options, type 'python cli.py w' into your terminal:")
        print("--> 1. View Budget: This shows you all your expenses for the year, broken out by category.")
        print("--> 2. Set Budget: Enter you expected monthly income and set your monthly budget by allocating a percent of your income to each budget category.")
        print("--> 3. Monthly Summary: View a summary of your total expenses, total income, total budget, and the current variance between your expenses and your budget for the current month. ")
        print("-----------------------------------")
        print("Add New Data")
        print("--> a1. Add Expense: This is where you can add a new expense.")
        print("--> a2. Add Income: This is where you can add income.")
        print("--> a3. Add Expense Category: Add a new category to organize your expenses and budget.")
        print("--> a4. Add Income Type: Add a new income type to organize your income entries.")
        print("-----------------------------------")
        print("Update Existing Data")
        print("--> u1. Update Expense: Update an expense entry amount using it's ID.")
        print("--> u2. Update Income: Update an income entry amount using it's ID.")
        print("--> u3. Update All Actuals and Variances: Update all the actuals and variance numbers for your tables based on your expense and income entries.")
        print("--> u4. Update Expected Monthly Income: Update your expected monthly income, by income type.")
        print("-----------------------------------")
        print("Delete Data")
        print("--> d1. Delete Expense: Delete an expense entry using it's ID.")
        print("--> d2. Delete Income: Delete an income entry using it's ID.")
        print("--> d3. Delete Expense Category: Delete an existing expense category.")
        print("--> d4. Delete Income Type: Delete an existing income type.")
        print("-----------------------------------")
        print("Export Data")
        print("--> e1. Export All Data: Export all your data into .xlsx files. Data will be exported into the output_directory folder.")

#views and summaries

    def view_budget(self):
        budgets = self.session.query(Budget).all()

        for budget in budgets:
            print(f'{budget.category}:')
            print('Expenses')
            
            expenses = budget.expenses
            if expenses:
                for expense in expenses:
                    print(f'\t{expense.description}: ${expense.amount:.2f}')
            else:
                print('\tNo expenses for this category.')
            
            print()

    def summary(self):
        total_income = sum([income.amount for income in self.session.query(Income).all()])
        total_expenses = sum([expense.amount for expense in self.session.query(Expense).all()])

        print (f"\nTotal Income: ${total_income:.2f}")
        print (f"Total Expenses: ${total_expenses:.2f}")
        print (f"Remaining Budget: ${total_income - total_expenses:.2f}\n")


    
