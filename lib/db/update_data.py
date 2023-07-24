from models import Budget, Expense, Income, IncomeType, engine
from variances import Variance
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from helpers import get_existing_entry, date_entry, amount_entry, commit_and_msg, line_print, get_first, get_all

class UpdateData:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def update_expense(self):
        print('Command U1: Update an expense entry')
        line_print()

        expense_id = int(input("Enter the ID of the expense entry you want to update: "))

        expense = get_existing_entry(self.session, Expense, expense_id)
        if expense is None:
            print(f"Expense entry with ID {expense_id} not found.")
            return
        else:
            print(f"Expense details: {expense}")
            update_to = int(input('Which part of this entry would you like to update? Enter 1 for the date, 2 for the amount, 3 for the category, and 4 for the description: '))

            if update_to == 1:
                new_date = date_entry('Enter the updated date (YYYY-MM-DD) for this expense entry: ')
                expense.date = new_date

            if update_to == 2:
                amount = amount_entry('Enter the updated amount for this expense entry: $')
                expense.amount = amount

            if update_to == 3:
                print(f'Available expense categories: {get_all(self.session, Budget)}')
                category_name = input('Enter the new category for this expense entry: ')

                existing_category = get_first(self.session, Budget,'category', category_name)
                if existing_category:
                    expense.category = existing_category
                else:
                    print('Invalid expense category. Please enter a valid category or create a new category by using the command python cli.py 6.')
                    return

            if update_to == 4:
                new_description = input('Enter the new description for this expense entry: ')
                expense.description = new_description

        commit_and_msg(self.session,f"Expense with ID {expense_id} updated successfully.", f"Updated expense details: {expense}")

    def update_income(self):
        print('Command U2: Update an income entry')
        line_print()

        income_id = int(input("Enter the ID of the income entry you want to update: "))

        income = get_existing_entry(self.session, Income, income_id)
        if income is None:
            print(f"Income entry with ID {income_id} not found.")
            return
        else:
            print(f"Income details: {income}")
            update_to = int(input('Which part of this entry would you like to update? Enter 1 for the date, 2 for the name, 3 for the amount, and 4 for the income type: '))

            if update_to == 1:
                updated_date = date_entry('Enter the updated date (YYYY-MM-DD) for this income entry: ')
                income.date = updated_date

            if update_to == 2:
                new_name = input('Enter the new name for this income entry: ')
                income.name = new_name

            if update_to == 3:
                amount = amount_entry('Enter the updated amount for this income entry: $')
                income.amount = amount

            if update_to == 4:
                print(f'Available income types: {get_all(self.session, IncomeType)}')
                income_type_name = input('Enter the new income type for this income entry: ')

                existing_income_type = get_first(self.session, IncomeType, 'name', income_type_name)
                if existing_income_type:
                    income.income_type = existing_income_type
                else:
                    print('Invalid income type. Please enter a valid income type or create a new income type by using the command python cli.py 7.')
                    return
            
            if update_to > 4:
                print('Invalid entry. Please select from the available options.')
                return

        commit_and_msg(self.session, f"Income with ID {income_id} updated successfully.", f"Updated income details: {income}")
    
    def update_expected_income(self):
        print('Command U4: Update expected income by income type')
        line_print()

        for income_type in get_all(self.session, IncomeType):
            expected_income = float(input(f"Enter your expected monthly income from {income_type}: $"))
            income_type.expected = expected_income
            commit_and_msg(self.session, "Success!", f"Expected income for {income_type} has been successfully updated to ${expected_income}!")