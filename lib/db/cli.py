import click
from welcome import Welcome
from add_data import AddData
from delete_data import DeleteData
from update_data import UpdateData

@click.group()
def cli():
    pass

#commands from welcome.py

@cli.command(name='0')
def welcome():
    welcome = Welcome()
    welcome.welcome_message()

@cli.command(name='1')
def view_budget():
    budget_cli = BudgetCLI()
    budget_cli.view_budget()

@cli.command(name='set_budget')
def set_budget():
    budget_cli = BudgetCLI()
    budget_cli.set_budget()

@cli.command(name='summary')
def summary():
    budget_cli = BudgetCLI()
    budget_cli.summary()

#commands from add_data

@cli.command(name='add_expense')
def add_expense():
    add_data = AddData()
    add_data.add_expense()

@cli.command(name='add_income')
def add_income():
    add_data = AddData()
    add_data.add_income()

@cli.command(name='add_expense_category')
def add_expense_category():
    add_data = AddData()
    add_data.add_expense_category()

@cli.command(name='add_income_type')
def add_income_type():
    add_data = AddData()
    add_data.add_income_type()

#commands from update_data.py

@cli.command(name='update_income')
def update_income():
    update_data = UpdateData()
    update_data.update_income()

@cli.command(name='update_expense')
def update_expense():
    update_data = UpdateData()
    update_data.update_expense()

#commands from delete_data.py

@cli.command(name='delete_expense')
def delete_expense():
    delete_data = DeleteData()
    delete_data.delete_expense()

@cli.command(name='delete_income')
def delete_income():
    delete_data = DeleteData()
    delete_data.delete_income()

@cli.command(name='delete_seed_data')
def delete_seed_data():
    delete_data = DeleteData()
    delete_data.delete_seed_data()

if __name__ == '__main__':
    cli()
