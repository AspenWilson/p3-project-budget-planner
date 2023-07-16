import click
from budget_cli import BudgetCLI 


def welcome_message():
    print("Welcome to your Budget Planner CLI!")
    print("-----------------------------------")
    print("You have many options to choose from to help you set and maintain your budget:")
    print("View: This shows you your current expenses, broken out by category.")
    print("Add_Expense: This is where you can add a new expense.")
    print("Add_Income: This is where you can add income.")
    print("Set_Budget: This is where you can set the budget for each category based on a percentage of your monthly income.")
    print("Summary: This is where you can see a brief summary of your total income, total expenses, and your remaining budget.")
    print("Delete_Expense: This is where you can delete an expense using the expense ID.")

@click.group()
def cli():
    welcome_message()

@click.command()
def view():
    budget_cli = BudgetCLI()
    budget_cli.view_budget()

@click.command()
def add_expense():
    budget_cli = BudgetCLI()
    budget_cli.add_expense()

@click.command()
def add_income():
    budget_cli = BudgetCLI()
    budget_cli.add_income()

@click.command()
def set_budget():
    budget_cli = BudgetCLI()
    budget_cli.set_budget()

@click.command()
def set_income():
    budget_cli = BudgetCLI()
    budget_cli.set_income()

@click.command()
def summary():
    budget_cli = BudgetCLI()
    budget_cli.summary()

@click.command()
def delete_expense():
    budget_cli = BudgetCLI()
    budget_cli.delete_expense()


if __name__ == '__main__':
    cli()
