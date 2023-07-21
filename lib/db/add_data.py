from models import Budget, Expense, Income, IncomeType, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from variances import Variance

class AddData:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def add_expense(self):
        description = input('Enter the description for this new expense expense: ')
        
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
        
        categories = self.session.query(Budget).all()
        print(f"Available categories: {categories}")
        category_name = input('Enter the category for the new expense: ')
        
        category = self.session.query(Budget).filter_by(category=category_name).first()
        if category:
            expense = Expense(description=description, amount=amount, date=date, category=category)
            self.session.add(expense)
            self.session.commit()
            print('Expense added successfully!')

            variances = Variance()
            variances.calculate_budget_actual_and_variance(category)
        else:
            print('Category not found. Please ensure the category exists.') 
    
    def add_income(self):
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

        income_type_options = self.session.query(IncomeType).all()
        print(f"Available income types: {income_type_options}")
        income_type_name = input('Enter the income type for the new income entry: ')

        income_type = self.session.query(IncomeType).filter_by(name=income_type_name).first()
        if income_type:
            income = Income(name=name, amount=amount, date=date, income_type=income_type)
        self.session.add(income)
        self.session.commit()
        print('Income added successfully!')

    def add_expense_category(self):
        category_name = input('Enter the name of the new expense category: ')

        existing_category = self.session.query(Budget).filter_by(category=category_name).first()
        if existing_category:
            print('Category already exists. Please choose a different name or use existing category.')
            print(f'Current expense categories: {self.session.query(Budget).all()}')
            return

        new_category = Budget(category=category_name, budget=0, actual=0, variance=0)
        self.session.add(new_category)
        self.session.commit()
        print('Category added successfully!')
        print(f'Updated expense categories: {self.session.query(Budget).all()}')
    
    def add_income_type(self):
        income_type_name = input('Enter the name of the new income type: ')

        existing_income_type = self.session.query(IncomeType).filter_by(name=income_type_name).first()
        if existing_income_type:
            print('Income type already exists. Please choose a different name or use existing category.')
            print(f"Current income types: {self.session.query(IncomeType).all()}")
            return

        new_income_type = IncomeType(name=income_type_name, expected=0, actual=0, variance=0)
        self.session.add(new_income_type)
        self.session.commit()
        print('Income type added successfully!')
        print(f"Updated income types: {self.session.query(IncomeType).all()}")   