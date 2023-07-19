from models import Budget, Expense, Income, IncomeType, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

class AddData:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def add_expense(self):
        name = input('Enter the name of the expense: ')
        
        while True:
            amount_str = input('Enter the amount for the expense: $')
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

        category_name = input('Enter the category for the expense: ')
        
        category = self.session.query(Budget).filter_by(name=category_name).first()
        if category:
            expense = Expense(name=name, amount=amount, date=date, category=category)
            self.session.add(expense)
            self.session.commit()
            print('Expense added successfully!')
        else:
            print('Category not found. Please ensure the category exists.') 
    
    def add_income(self):
        name = input('Enter a name for this income entry: ')
        
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

        self.session.add(income)
        self.session.commit()
        print('Income added successfully!')

    def add_expense_category(self):
        category_name = input('Enter the name of the new expense category: ')

        existing_category = self.session.query(Budget).filter_by(name=category_name).first()
        if existing_category:
            print('Category already exists. Please choose a different name or use existing category.')
            print(f'Current expense categories: {self.session.query(Budget).all()}')
            return

        category = Budget(name=category_name)
        self.session.add(category)
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

        new_income_type = IncomeType(name=income_type_name)
        self.session.add(new_income_type)
        self.session.commit()
        print('Income type added successfully!')
        print(f"Updated income types: {self.session.query(IncomeType).all()}")   