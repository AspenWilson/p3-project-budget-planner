import click
from budget_cli import BudgetCLI 

@click.group()
def cli():
    pass

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

cli.add_command(view)
cli.add_command(add_expense, name="add_expense")
cli.add_command(add_income, name="add_income")
cli.add_command(set_budget, name = "set_budget")
cli.add_command(set_income, name = "set_income")

if __name__ == '__main__':
    cli()
