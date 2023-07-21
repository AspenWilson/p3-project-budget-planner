import click
from welcome import Welcome
from add_data import AddData
from delete_data import DeleteData
from update_data import UpdateData
from variances import Variance
from budget import SetBudget
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

@cli.command(name='2')
def set_budget():
    budget = SetBudget()
    budget.set_budget()

#commands from summaries.py

@cli.command(name='3')
def monthly_summary():
    summaries = MonthSummary()
    summaries.view_monthly_summary()

#commands from add_data

@cli.command(name='4')
def add_expense():
    add_data = AddData()
    add_data.add_expense()

    variances = Variance()
    variances.update_all_actuals_and_variances()

@cli.command(name='5')
def add_income():
    add_data = AddData()
    add_data.add_income()

    variances = Variance()
    variances.update_all_actuals_and_variances()

@cli.command(name='6')
def add_expense_category():
    add_data = AddData()
    add_data.add_expense_category()

@cli.command(name='7')
def add_income_type():
    add_data = AddData()
    add_data.add_income_type()

#commands from update_data.py

@cli.command(name='8')
def update_income():
    update_data = UpdateData()
    update_data.update_income()

    variances = Variance()
    variances.update_all_actuals_and_variances()

@cli.command(name='9')
def update_expense():
    update_data = UpdateData()
    update_data.update_expense()

    variances = Variance()
    variances.update_all_actuals_and_variances()

#commands from delete_data.py

@cli.command(name='10')
def delete_expense():
    delete_data = DeleteData()
    delete_data.delete_expense()

@cli.command(name='11')
def delete_income():
    delete_data = DeleteData()
    delete_data.delete_income()

@cli.command(name='14')
def delete_expense_category():
    delete_data = DeleteData()
    delete_data.delete_expense_category()

@cli.command(name='15')
def delete_income_type():
    delete_data = DeleteData()
    delete_data.delete_income_type()

@cli.command(name='16')
def delete_seed_data():
    delete_data = DeleteData()
    delete_data.delete_seed_data()



#commands from variances.py

@cli.command(name='12')
def update_all_actuals_and_variances():
    variances = Variance()
    variances.update_all_actuals_and_variances()

#commands from export_data.py
@cli.command(name='13')
def export_all_data():
    export_category()
    export_expenses()
    export_income()
    export_income_types()
    print("Data exported successfully to the output_directory folder.")

if __name__ == '__main__':
    cli()
