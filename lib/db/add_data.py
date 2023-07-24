from models import Budget, Expense, Income, IncomeType, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from variances import Variance
from helpers import date_entry, amount_entry, add_and_commit, line_print, get_first, get_all

class AddData:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def add_expense(self):
        print('Command A1: Add a new expense entry')
        line_print()

        description = input('Enter the description for this new expense entry: ')
        
        amount = amount_entry('Enter the amount for the new expense: $')
        
        date = date_entry('Enter the date (YYYY-MM-DD) for the new expense: ')
        
        print(f"Available categories: {get_all(self.session, Budget)}")
        category_name = input('Enter the category for the new expense: ')
        
        existing_category = get_first(self.session, Budget, 'category', category_name)
        if existing_category:
            expense = Expense(
                description=description, 
                amount=amount, 
                date=date, 
                category=existing_category
                )

            print(f'New Expense Entry Details: {expense}')
            choice = input("Are you sure you want to add this expense entry? y/n: ")
            
            if choice == 'y':
                add_and_commit(self.session, expense,'Expense entry added successfully!', f'New expense entry details: {expense}')
            else:
                print('Expense entry cancelled by user.')
                return

        else:
            print('Category not found. Please ensure the category exists.') 
    
    def add_income(self):
        print('Command A2: Add a new income entry')
        line_print()

        name = input('Enter a name for this new income entry: ')
        
        amount = amount_entry('Enter the amount for this income entry: $')
        
        date = date_entry('Enter the date (YYYY-MM-DD) for the expense: ')

        print(f"Available income types: {get_all(self,session, IncomeType)}")
        income_type_name = input('Enter the income type for the new income entry: ')

        existing_income_type = get_first(self.session, IncomeType, 'name', income_type_name)
        if existing_income_type:
            income = Income(
                name=name, 
                amount=amount, 
                date=date, 
                income_type=existing_income_type
                )
        
        print(f'New Income Entry Details: {income}')
        choice = input("Are you sure you want to add this income entry? y/n: ")
        
        if choice == 'y':
            add_and_commit(self.session, income,'Income entry added successfully!')
            print(f'New income entry details: {income}')
        else:
            print('Income entry cancelled by user.')
            return

    def add_expense_category(self):
        print('Command A3: Add a new expense category')
        line_print()

        print(f"Current expense categories: {get_all(self.session, Budget)}")
        category_name = input('Enter the name of the new expense category: ')

        existing_category = get_first(self.session, Budget, 'category', category_name)

        if existing_category:
            print('Category already exists. Please choose a different name or use existing category.')
            return

        new_category = Budget(
            category=category_name, 
            budget=0, 
            actual=0, 
            variance=0
            )

        add_and_commit(self.session, new_category,'Category added successfully!')
        print(f'Updated expense categories: {get_all(self.session, Budget)}')
    
    def add_income_type(self):
        print('Command A4: Add a new income type')
        line_print()

        print(f"Current income types: {get_all(self.session, IncomeType)}")
        income_type_name = input('Enter the name of the new income type: ')

        existing_income_type = get_first(self.session, IncomeType, 'name', income_type_name)
        if existing_income_type:
            print('Income type already exists. Please choose a different name or use existing category.')
            return

        new_income_type = IncomeType(
            name=income_type_name, 
            expected=0, 
            actual=0, 
            variance=0
            )

        add_and_commit(self.session, new_income_type,'Income type added successfully!')
        print(f"Updated income types: {get_all(self.session, IncomeType)}")   