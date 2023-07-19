import click
from welcome import Welcome
from add_data import AddData
from delete_data import DeleteData
from update_data import UpdateData
from variances import Variance
from budget import Budget
from summaries import MonthSummary
from export_data import export_budgets, export_expenses, export_income, export_income_types


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

#commands from budget.py

@cli.command(name='set_budget')
def set_budget():
    budget = Budget()
    budget.set_budget()

#commands from summaries.py

@cli.command(name='monthly_summary')
def monthly_summary():
    summaries = MonthSummary()
    summaries.view_monthly_summary()

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
@cli.command(name='export_all_data')
def export_all_data():
    export_category()
    export_expenses()
    export_income()
    export_income_types()
    print("Data exported successfully to the output_directory folder.")

if __name__ == '__main__':
    cli()
