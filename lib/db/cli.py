import click
from budget_cli import BudgetCLI 

@click.group()
def cli():
    pass

@cli.command(name='welcome')
def welcome():
    budget_cli = BudgetCLI()
    budget_cli.welcome_message()

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

@cli.command(name='add_category')
def add_category():
    budget_cli = BudgetCLI()
    budget_cli.add_category()

if __name__ == '__main__':
    cli()
