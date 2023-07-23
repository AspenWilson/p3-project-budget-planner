from models import Budget, Expense, Income, IncomeType, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from variances import Variance
from helpers import all_categories, all_income_types

class AddData:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def add_expense(self):
        print('Command A1: Add a new expense entry')
        print("-----------------------------------")
        description = input('Enter the description for this new expense entry: ')
        
        while True:
            amount_str = input('Enter the amount for the new expense: $')
            try:
                amount = float(amount_str)
                break  
            except ValueError:
                print('Invalid amount. Please enter a valid number.')
        
        while True:
            date_str = input('Enter the date (YYYY-MM-DD) for the new expense: ')
            try:
                date = datetime.strptime(date_str, '%Y-%m-%d')
                break 
            except ValueError:
                print('Invalid date format. Please use the format YYYY-MM-DD.')
        
        print(f"Available categories: {all_categories}")
        category_name = input('Enter the category for the new expense: ')
        
        category = self.session.query(Budget).filter_by(category=category_name).first()
        if category:
            expense = Expense(
                description=description, 
                amount=amount, 
                date=date, 
                category=category
                )

            print(f'New Expense Entry Details: {expense}')
            choice = input("Are you sure you want to add this expense entry? y/n: ")
            
            if choice == 'y':
                self.session.add(expense)
                self.session.commit()
                print('Expense added successfully!')
                print(f'New expense entry details: {expense}')
            else:
                print('Expense entry cancelled.')
                return

        else:
            print('Category not found. Please ensure the category exists.') 
    
    def add_income(self):
        print('Command A2: Add a new income entry')
        print("-----------------------------------")
        name = input('Enter a name for this new income entry: ')
        
        while True:
            amount_str = input('Enter the amount for this income entry: $')
            try:
                amount = float(amount_str)
                break  
            except ValueError:
                print('Invalid amount. Please enter a valid number.')
        
        while True:
            date_str = input('Enter the date (YYYY-MM-DD) for the expense: ')
            try:
                date = datetime.strptime(date_str, '%Y-%m-%d')
                break  
            except ValueError:
                print('Invalid date format. Please use the format YYYY-MM-DD.')

        print(f"Available income types: {all_income_types}")
        income_type_name = input('Enter the income type for the new income entry: ')

        income_type = self.session.query(IncomeType).filter_by(name=income_type_name).first()
        if income_type:
            income = Income(
                name=name, 
                amount=amount, 
                date=date, 
                income_type=income_type
                )
        
        print(f'New Income Entry Details: {income}')
        choice = input("Are you sure you want to add this income entry? y/n: ")
        
        if choice == 'y':
            self.session.add(income)
            self.session.commit()
            print('Income added successfully!')
            print(f'New income entry details: {income}')
        else:
            print('Income entry cancelled.')
            return

    def add_expense_category(self):
        print('Command A3: Add a new expense category')
        print("-----------------------------------")
        print(f"Current expense categories: {all_categories}")
        category_name = input('Enter the name of the new expense category: ')

        existing_category = self.session.query(Budget).filter_by(category=category_name).first()
        if existing_category:
            print('Category already exists. Please choose a different name or use existing category.')
            return

        new_category = Budget(
            category=category_name, 
            budget=0, 
            actual=0, 
            variance=0
            )

        self.session.add(new_category)
        self.session.commit()
        print('Category added successfully!')
        print(f'Updated expense categories: {all_categories}')
    
    def add_income_type(self):
        print('Command A4: Add a new income type')
        print("-----------------------------------")
        print(f"Current income types: {all_income_types}")
        income_type_name = input('Enter the name of the new income type: ')

        existing_income_type = self.session.query(IncomeType).filter_by(name=income_type_name).first()
        if existing_income_type:
            print('Income type already exists. Please choose a different name or use existing category.')
            return

        new_income_type = IncomeType(
            name=income_type_name, 
            expected=0, 
            actual=0, 
            variance=0
            )

        self.session.add(new_income_type)
        self.session.commit()
        print('Income type added successfully!')
        print(f"Updated income types: {all_income_types}")   