import os
import pandas as pd
from datetime import datetime
from sqlalchemy import extract, func
from models import Budget, Expense, Income, IncomeType, engine
from sqlalchemy.orm import sessionmaker
from helpers import current_month, current_year, get_all, generate_expense_data, generate_income_data, line_print

Session = sessionmaker(bind=engine)
session = Session()

def export_to_excel(table_name, data, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    df = pd.DataFrame(data)
    output_file = os.path.join(output_dir, f"{table_name}.xlsx")
    df.to_excel(output_file, index=False)

def export_budgets():

    data = [
        {
            "Budget Category": budget.category,
            "Budget": budget.budget,
            "Actual": budget.actual,
            "Variance": budget.variance
        }
        for budget in get_all(session, Budget)
    ]

    export_to_excel("Monthly Budget", data, "output_directory")

def export_expenses():

    data = [
        generate_expense_data(expense)
        for expense in get_all(session, Expense)
    ]

    export_to_excel("All Expenses", data, "output_directory")

def export_yearly_expenses():

    yearly_expenses = session.query(Expense).filter(extract('year', Expense.date) == current_year).all()

    data = [
        generate_expense_data(expense)
        for expense in yearly_expenses
    ]

    export_to_excel("Yearly Expenses", data, "output_directory")

def export_monthly_expenses():

    monthly_expenses = session.query(Expense).filter(extract('year', Expense.date) == current_year, extract('month', Expense.date) == current_month).all()

    data = [
        generate_expense_data(expense)
        for expense in monthly_expenses
    ]

    export_to_excel("Monthly Expenses", data, "output_directory")

def export_income():

    data = [
        generate_income_data(income)
        for income in get_all(session, Income)
    ]

    export_to_excel("All Income", data, "output_directory")

def export_yearly_income():

    yearly_income = session.query(Income).filter(extract('year', Income.date) == current_year).all()

    data = [
        generate_income_data(income)
        for income in yearly_income
    ]

    export_to_excel("Yearly Income Details", data, "output_directory")

def export_monthly_income():

    monthly_income = session.query(Income).filter(extract('year', Income.date) == current_year, extract('month', Income.date) == current_month).all()

    data = [
        generate_income_data(income)
        for income in monthly_income
    ]

    export_to_excel("Monthly Income Entries", data, "output_directory")

def export_income_types():

    data = [
        {
        "Income Type": income_type.name, 
        "Expected": income_type.expected, 
        "Actual": income_type.actual,
        "Variance:": income_type.variance
        }
        for income_type in get_all(session, IncomeType)
    ]

    export_to_excel("Monthly Income", data, "output_directory")

def export_all_data():
    print('Command E1: Export all data')
    line_print()

    choice = input("You are about to export all your existing data. Before you proceed, have you deleted your current output_directory folder? y/n: ")

    if choice == 'y':
        export_budgets()
        export_expenses()
        export_income()
        export_income_types()
        print("Data exported successfully to the output_directory folder!")
    else:
        print('Delete your existing out_directory folder and then run this command again.')

def export_yearly_data():
    print('Command E2: Export all yearly data')
    line_print()

    choice = input("You are about to export all your existing data for the current year. Before you proceed, have you deleted your current output_directory folder? y/n: ")

    if choice == 'y':
        export_budgets()
        export_yearly_expenses()
        export_yearly_income()
        export_income_types()
        print("Data exported successfully to the output_directory folder!")
    else:
        print('Delete your existing out_directory folder and then run this command again.')
    
def export_monthly_data():
    print('Command E3: Export all monthly data')
    line_print()

    choice = input("You are about to export all your existing data for the current month. Before you proceed, have you deleted your current output_directory folder? y/n: ")

    if choice == 'y':
        export_budgets()
        export_monthly_expenses()
        export_monthly_income()
        export_income_types()
        print("Data exported successfully to the output_directory folder!")
    else:
        print('Delete your existing out_directory folder and then run this command again.')


