import click
from welcome import Welcome
from add_data import AddData
from delete_data import DeleteData
from update_data import UpdateData
from variances import Variance
from budget import SetBudget
from summaries import MonthSummary
from import_data import ImportData
from export_data import export_all_data, export_yearly_data, export_monthly_data
from helpers import line_print


@click.group()
def cli():
    pass

#commands from welcome.py

@cli.command(name='w')
def welcome():
    welcome = Welcome()
    welcome.welcome_message()

#commands from budget.py

@cli.command(name='2')
def set_budget():
    budget = SetBudget()
    budget.set_budget()

    variances = Variance()
    variances.update_all_actuals_and_variances()

#commands from summaries.py

@cli.command(name='1')
def view_budget():
    summaries = MonthSummary()
    summaries.view_monthly_expenses()

@cli.command(name='3')
def monthly_summary():
    summaries = MonthSummary()
    summaries.view_monthly_summary()

#commands from add_data

@cli.command(name='a1')
def add_expense():
    add_data = AddData()
    add_data.add_expense()

    variances = Variance()
    variances.update_all_actuals_and_variances()

@cli.command(name='a2')
def add_income():
    add_data = AddData()
    add_data.add_income()

    variances = Variance()
    variances.update_all_actuals_and_variances()

@cli.command(name='a3')
def add_expense_category():
    add_data = AddData()
    add_data.add_expense_category()

@cli.command(name='a4')
def add_income_type():
    add_data = AddData()
    add_data.add_income_type()

#commands from update_data.py

@cli.command(name='u2')
def update_income():
    update_data = UpdateData()
    update_data.update_income()

    variances = Variance()
    variances.update_all_actuals_and_variances()

@cli.command(name='u1')
def update_expense():
    update_data = UpdateData()
    update_data.update_expense()

    variances = Variance()
    variances.update_all_actuals_and_variances()

@cli.command(name='u4')
def update_expected_income():
    update_data = UpdateData()
    update_data.update_expected_income()

    variances = Variance()
    variances.update_all_actuals_and_variances()

#commands from delete_data.py

@cli.command(name='d1')
def delete_expense():
    delete_data = DeleteData()
    delete_data.delete_expense()

    variances = Variance()
    variances.update_all_actuals_and_variances()

@cli.command(name='d2')
def delete_income():
    delete_data = DeleteData()
    delete_data.delete_income()

    variances = Variance()
    variances.update_all_actuals_and_variances()

@cli.command(name='d3')
def delete_expense_category():
    delete_data = DeleteData()
    delete_data.delete_expense_category()

@cli.command(name='d4')
def delete_income_type():
    delete_data = DeleteData()
    delete_data.delete_income_type()

@cli.command(name='x')
def delete_seed_data():
    delete_data = DeleteData()
    delete_data.delete_all_data()

#commands from variances.py

@cli.command(name='u3')
def update_all_actuals_and_variances():
    print('Command U3: Update actual and variance numbers for Monthly Budget and Monthly Income')
    line_print()
    variances = Variance()
    variances.update_all_actuals_and_variances()
    print('All monthly actuals and variances have been updated successfully!')

#commands from export_data.py
@cli.command(name='e1')
def export_total_data():
    export_all_data()

@cli.command(name='e2')
def export_total_data():
    export_yearly_data()

@cli.command(name='e3')
def export_total_data():
    export_monthly_data()

#commands from import_data.py
@cli.command(name='i1')
def import_expenses():
    import_data=ImportData()
    import_data.import_all_expenses()

@cli.command(name='i2')
def import_expenses():
    import_data=ImportData()
    import_data.import_all_income()

if __name__ == '__main__':
    cli()
