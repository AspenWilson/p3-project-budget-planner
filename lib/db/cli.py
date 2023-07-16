import click
from budget_cli import BudgetCLI 


def welcome_message():
    print("Welcome to your Budget Planner CLI!")
    print("-----------------------------------")
    print("You have many options to choose from to help you set and maintain your budget:")
    print("View: This shows you your current budgets, broken out by category.")
    print("Add_Expense: This is where you can add a new expense.")
    print("Add_Income: This is where you can add income.")
    print("Set_Budget: This is where you can set the budget for each category based on a percentage of your monthly income.")
    print("Summary: This is where you can see a brief summary of your total income, total expenses, and your remaining budget.")
    print("Delete_Expense: This is where you can delete an expense using the expense ID.")

@click.group()
def cli():
    welcome_message()

@cli.command(name='view')
def view_budget():
    budget_cli = BudgetCLI()
    budget_cli.view_budget()

@cli.command(name='add_expense')
def add_expense():
    budget_cli = BudgetCLI()
    budget_cli.add_expense()

@cli.command(name='add_income')
def add_income():
    budget_cli = BudgetCLI()
    budget_cli.add_income()

@cli.command(name='set_budget')
def set_budget():
    budget_cli = BudgetCLI()
    budget_cli.set_budget()

@cli.command(name='summary')
def summary():
    budget_cli = BudgetCLI()
    budget_cli.summary()

@cli.command(name='delete_expense')
def delete_expense():
    budget_cli = BudgetCLI()
    budget_cli.delete_expense()

if __name__ == '__main__':
    cli()
