import os
import pandas as pd
from models import Budget, Expense, Income, IncomeType, engine
from sqlalchemy.orm import sessionmaker

def export_to_excel(table_name, data, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    df = pd.DataFrame(data)
    output_file = os.path.join(output_dir, f"{table_name}.xlsx")
    df.to_excel(output_file, index=False)

def export_budget():
    Session = sessionmaker(bind=engine)
    session = Session()
    budgets = session.query(Budget).all()

    data = [
        {
            "Budget Category": budget.category,
            "Budget": budget.budget,
            "Actual": budget.actual,
            "Variance": budget.variance
        }
        for budget in budgets
    ]

    export_to_excel("Budget", data, "output_directory")

def export_expenses():
    Session = sessionmaker(bind=engine)
    session = Session()
    expenses = session.query(Expense).all()

    data = [
        {
            "Expense Name": expense.name,
            "Amount": expense.amount,
            "Category Name": expense.category.name,
            "Date": expense.date
        }
        for expense in expenses
    ]

    export_to_excel("Expenses", data, "output_directory")

def export_income():
    Session = sessionmaker(bind=engine)
    session = Session()
    incomes = session.query(Income).all()

    data = [
        {
            "Income Name": income.name,
            "Amount": income.amount,
            "Date": income.date,
            "Income Type": income.income_type.name
        }
        for income in incomes
    ]

    export_to_excel("Income", data, "output_directory")

def export_income_types():
    Session = sessionmaker(bind=engine)
    session = Session()
    income_types = session.query(IncomeType).all()

    data = [
        {
            "Income Type": income_type.name,
            "Expected": income_type.expected,
            "Actual": income_type.actual,
            "Variance": income_type.variance
        }
        for income_type in income_types
    ]

    export_to_excel("IncomeTypes", data, "output_directory")

if __name__ == "__main__":
    export_budget()
    export_expenses()
    export_income()
    export_income_types()