import click
from budget_cli import BudgetCLI 


def welcome_message():
    print("Welcome to your Budget Planner CLI!")
    print("-----------------------------------")
    print("You have many options to choose from to help you set and maintain your budget:")
    print("View_Budget: This shows you your current budgets, broken out by category.")
    print("Add_Expense: This is where you can add a new expense.")
    print("Add_Income: This is where you can add income.")
    print("Set_Budget: This is where you can set the budget for each category based on a percentage of your monthly income.")
    print("Summary: This is where you can see a brief summary of your total income, total expenses, and your remaining budget.")
    print("Delete_Expense: This is where you can delete an expense using the expense ID.")

@click.group()
def cli():
    welcome_message()

def view_budget():
    budget_cli = BudgetCLI()
    budget_cli.view_budget()

def add_expense():
    budget_cli = BudgetCLI()
    budget_cli.add_expense()

def add_income():
    budget_cli = BudgetCLI()
    budget_cli.add_income()

def set_budget():
    budget_cli = BudgetCLI()
    budget_cli.set_budget()

def summary():
    budget_cli = BudgetCLI()
    budget_cli.summary()

def delete_expense():
    budget_cli = BudgetCLI()
    budget_cli.delete_expense()

if __name__ == '__main__':
    cli()
