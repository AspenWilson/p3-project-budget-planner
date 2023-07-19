import click
from welcome import Welcome
from add_data import AddData
from delete_data import DeleteData
from update_data import UpdateData
from variances import Variance
from summary_and_budget import Budget
import export_data

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
    welcome = Welcome()
    welcome.view_budget()

@cli.command(name='set_budget')
def set_budget():
    summary_and_budget = Budget()
    summary_and_budget.set_budget()

@cli.command(name='summary')
def summary():
    budget_cli = BudgetCLI()
    budget_cli.summary()

#commands from add_data

@cli.command(name='add_expense')
def add_expense():
    add_data = AddData()
    add_data.add_expense()

    variances = Variance()
    variances.update_all_actuals_and_variances()

@cli.command(name='add_income')
def add_income():
    add_data = AddData()
    add_data.add_income()

    variances = Variance()
    variances.update_all_actuals_and_variances()

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

    variances = Variance()
    variances.update_all_actuals_and_variances()

@cli.command(name='update_expense')
def update_expense():
    update_data = UpdateData()
    update_data.update_expense()

    variances = Variance()
    variances.update_all_actuals_and_variances()

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

#commands from variances.py

@cli.command(name='update_all_actuals_and_variances')
def update_all_actuals_and_variances():
    variances = Variance()
    variances.update_all_actuals_and_variances()

#commands from export_data.py
@cli.command(name='export_data')
def export_data():
    export_data = export_data()
    export_data()

if __name__ == '__main__':
    cli()
