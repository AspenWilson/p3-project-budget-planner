from models import Budget, Expense, Income, IncomeType, engine
from variances import Variance
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from helpers import all_categories, all_income_types

class UpdateData:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def update_expense(self):
        expense_id = int(input("Enter the ID of the expense entry you want to update: "))

        expense = self.session.query(Expense).get(expense_id)
        if expense is None:
            print(f"Expense entry with ID {expense_id} not found.")
            return
        else:
            print(f"Expense details: {expense}")
            update_to = int(input('Which part of this entry would you like to update? Enter 1 for the date, 2 for the amount, 3 for the category, and 4 for the description: '))

            if update_to == 1:
                date_str = input('Enter the updated date (YYYY-MM-DD) for this expense entry: ')
                try:
                    date = datetime.strptime(date_str, '%Y-%m-%d')
                    expense.date = date  
                except ValueError:
                    print('Invalid date format. Please use the format YYYY-MM-DD.')
                    return

            if update_to == 2:
                amount_str = input('Enter the updated amount for this expense entry: $')
                try:
                    amount = float(amount_str)
                    expense.amount = amount
                except ValueError:
                    print('Invalid amount. Please enter a valid number.')
                    return

            if update_to == 3:
                print(f'Available expense categories: {all_categories}')
                new_category= input('Enter the new category for this expense entry: ')

                category = self.session.query(Budget).filter_by(category=new_category).first()
                if category:
                    expense.category = category
                else:
                    print('Invalid expense category. Please enter a valid category or create a new category by using the command python cli.py 6.')
                    return

            if update_to == 4:
                new_description = input('Enter the new description for this expense entry: ')
                expense.description = new_description

        self.session.commit()
        print(f"Expense with ID {expense_id} updated successfully.")
        print(f"Updated expense details: {expense}")

    def update_income(self):
        income_id = int(input("Enter the ID of the income entry you want to update: "))

        income = self.session.query(Income).get(income_id)
        if income is None:
            print(f"Income entry with ID {income_id} not found.")
            return
        else:
            print(f"Income details: {income}")
            update_to = int(input('Which part of this entry would you like to update? Enter 1 for the date, 2 for the name, 3 for the amount, and 4 for the income type: '))

            if update_to == 1:
                date_str = input('Enter the updated date (YYYY-MM-DD) for this income entry: ')
                try:
                    date = datetime.strptime(date_str, '%Y-%m-%d')
                    income.date = date  
                except ValueError:
                    print('Invalid date format. Please use the format YYYY-MM-DD.')
                    return

            if update_to == 2:
                new_name = input('Enter the new name for this income entry: ')
                income.name = new_name

            if update_to == 3:
                amount_str = input('Enter the updated amount for this income entry: $')
                try:
                    amount = float(amount_str)
                    income.amount = amount
                except ValueError:
                    print('Invalid amount. Please enter a valid number.')
                    return

            if update_to == 4:
                print(f'Available income types: {all_income_types}')
                new_income_type= input('Enter the new income type for this income entry: ')

                income_type = self.session.query(IncomeType).filter_by(name=new_income_type).first()
                if income_type:
                    income.income_type = income_type
                else:
                    print('Invalid income type. Please enter a valid income type or create a new income type by using the command python cli.py 7.')
                    return
            
            if update_to > 4:
                print('Invalid entry. Please select from the available options.')
                return

        self.session.commit()
        print(f"Income with ID {income_id} updated successfully.")
        print(f"Updated income details: {income}")
    
    def update_expected_income(self):

        for income_source in all_income_types:
            expected_income = float(input(f"Enter your expected monthly income from {income_source}: $"))
            income_source.expected = expected_income
            self.session.commit()
            print(f"Expected income for {income_source} has been successfully updated to ${expected_income}!")