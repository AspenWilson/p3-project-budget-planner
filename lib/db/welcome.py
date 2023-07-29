from models import Budget, Expense, Income, IncomeType, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from helpers import line_print

class Welcome:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def welcome_message(self):
        line_print()
        print("Welcome to your Budget Planner CLI!")
        line_print()
        print("You have many options to choose from to help you set and maintain your budget. Your options are listed below. To call these commands, simply enter python cli.py and then enter the letter/number of the command. If you ever need to see your options, type 'python cli.py w' into your terminal:")
        print("\t--> 1. View Expenses: This shows you all your expenses for the year, broken out by category.")
        print("\t--> 2. Set Budget: Enter you expected monthly income and set your monthly budget by allocating a percent of your income to each budget category.")
        print("\t--> 3. Monthly Summary: View a summary of your total expenses, total income, total budget, and the current variance between your expenses and your budget for the current month. ")
        line_print()
        print("Add New Data")
        print("\t--> a1. Add Expense: This is where you can add a new expense.")
        print("\t--> a2. Add Income: This is where you can add income.")
        print("\t--> a3. Add Expense Category: Add a new category to organize your expenses and budget.")
        print("\t--> a4. Add Income Type: Add a new income type to organize your income entries.")
        line_print()
        print("Update Existing Data")
        print("\t--> u1. Update Expense: Update an expense entry amount using it's ID.")
        print("\t--> u2. Update Income: Update an income entry amount using it's ID.")
        print("\t--> u3. Update All Actuals and Variances: Update all the actuals and variance numbers for your tables based on your expense and income entries.")
        print("\t--> u4. Update Expected Monthly Income: Update your expected monthly income, by income type.")
        line_print()
        print("Delete Data")
        print("\t--> d1. Delete Expense: Delete an expense entry using it's ID.")
        print("\t--> d2. Delete Income: Delete an income entry using it's ID.")
        print("\t--> d3. Delete Expense Category: Delete an existing expense category.")
        print("\t--> d4. Delete Income Type: Delete an existing income type.")
        line_print()
        print("Export Data")
        print("\t--> e1. Export All Data: Export all your data into .xlsx files. Data will be exported into the output_directory folder.")
        print("\t--> e2. Export Current Year Data: Export all your data for the current year into .xlsx files. Data will be exported into the output_directory folder.")
        print("\t--> e3. Export Current Month Data: Export all your data for the current month into .xlsx files. Data will be exported into the output_directory folder.")
        line_print()
        print('Import Data')
        print("\t--> i1. Import Expenses: Import multiple expenses.")
        print("\t--> i2. Import Income: Import multiple income entries.")
        print("Delete All")
        print("\t--> x. Delete all your current data")



    
