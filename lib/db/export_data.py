import os
import pandas as pd
from datetime import datetime
from sqlalchemy import extract, func
from models import Budget, Expense, Income, IncomeType, engine
from sqlalchemy.orm import sessionmaker
from helpers import current_month, current_year, get_all

def export_to_excel(table_name, data, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    df = pd.DataFrame(data)
    output_file = os.path.join(output_dir, f"{table_name}.xlsx")
    df.to_excel(output_file, index=False)

def export_budgets():
    Session = sessionmaker(bind=engine)
    session = Session()

    data = [
        {
            "Budget Category": budget.category,
            "Budget": budget.budget,
            "Actual": budget.actual,
            "Variance": budget.variance
        }
        for budget in get_all(self.session, Budget)
    ]

    export_to_excel("Monthly Budget", data, "output_directory")

def export_expenses():
    Session = sessionmaker(bind=engine)
    session = Session()

    data = [
        {
            "Expense Description": expense.description,
            "Amount": expense.amount,
            "Category Name": expense.category,
            "Date": expense.date
        }
        for expense in get_all(self.session, Expense)
    ]

    export_to_excel("All Expenses", data, "output_directory")

def export_yearly_expenses():
    Session = sessionmaker(bind=engine)
    session = Session()

    yearly_expenses = session.query(Expense).filter(extract('year', Expense.date) == current_year).all()

    data = [
        {
            "Expense Description": expense.description,
            "Amount": expense.amount,
            "Category Name": expense.category,
            "Date": expense.date
        }
        for expense in yearly_expenses
    ]

    export_to_excel("Yearly Expenses", data, "output_directory")

def export_monthly_expenses():
    Session = sessionmaker(bind=engine)
    session = Session()

    monthly_expenses = session.query(Expense).filter(extract('year', Expense.date) == current_year, extract('month', Expense.date) == current_month).all()

    data = [
        {
            "Expense Description": expense.description,
            "Amount": expense.amount,
            "Category Name": expense.category,
            "Date": expense.date
        }
        for expense in monthly_expenses
    ]

    export_to_excel("Monthly Expenses", data, "output_directory")

def export_income():
    Session = sessionmaker(bind=engine)
    session = Session()

    data = [
        {
            "Income Name": income.name,
            "Amount": income.amount,
            "Date": income.date,
            "Income Type": income.income_type.name
        }
        for income in get_all(self.session, Income)
    ]

    export_to_excel("All Income", data, "output_directory")

def export_yearly_income():
    Session = sessionmaker(bind=engine)
    session = Session()

    yearly_income = session.query(Income).filter(extract('year', Income.date) == current_year).all()


    data = [
        {
            "Income Name": income.name,
            "Amount": income.amount,
            "Date": income.date,
            "Income Type": income.income_type.name
        }
        for income in yearly_income
    ]

    export_to_excel("Yearly Income Details", data, "output_directory")

def export_monthly_income():
    Session = sessionmaker(bind=engine)
    session = Session()

    monthly_income = session.query(Income).filter(extract('year', Income.date) == current_year, extract('month', Income.date) == current_month).all()

    data = [
        {
            "Income Name": income.name,
            "Amount": income.amount,
            "Date": income.date,
            "Income Type": income.income_type.name
        }
        for income in monthly_income
    ]

    export_to_excel("Monthly Income Entries", data, "output_directory")

def export_income_types():
    Session = sessionmaker(bind=engine)
    session = Session()

    data = [
        {
            "Income Type": income_type.name,
            "Expected": income_type.expected,
            "Actual": income_type.actual,
            "Variance": income_type.variance
        }
        for income_type in get_all(self.session, IncomeType)
    ]

    export_to_excel("Monthly Income", data, "output_directory")

def export_all_data():
    print('Command E1: Export all data')
    print("-----------------------------------")

    choice = input("You are about to export all your existing data. Before you proceed, have you deleted your current out_directory folder? y/n: ")

    if choice == 'y':
        export_budgets()
        export_expenses()
        export_income()
        export_income_types()
        print("Data exported successfully to the output_directory folder!")
    else:
        print('Delete your existing out_directory folder and then run this command again.')


if __name__ == "__main__":
    export_budgets()
    export_expenses()
    export_income()
    export_income_types()