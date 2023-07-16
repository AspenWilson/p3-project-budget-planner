from models import Category, Expense, Income, engine
from sqlalchemy.orm import sessionmaker

class BudgetCLI:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def view_budget(self):
        categories = self.session.query(Category).all()

        for category in categories:
            print(f'{category.name}: Budget - ${category.budget:.2f}')
            print('Expenses')
            
            expenses = category.expenses
            if expenses:
                for expense in expenses:
                    print(f'\t{expense.name}: ${expense.amount:.2f}')
            else:
                print('\tNo expenses for this category.')
            
            print() 
    
    def add_expense(self):
        name = input('Enter the name of the expense: ')
        amount = float(input('Enter the amount for the expense: '))
        category_name = input('Enter the category for the expense: ')

        category = self.session.query(Category).filter_by(name=category_name).first()
        if category:
            expense = Expense(name=name, amount=amount, category=category)
            self.session.add(expense)
            self.session.commit()
            print('Expense added successfully!')
        else:
            print('Category not found. Please ensure the category exists.') 
    
    def add_income(self):
        name = input('Enter the name of the income: ')
        amount = float(input('Enter the amount for the income: '))


        self.session.add(expense)
        self.session.commit()
        print('Income added successfully!')

    
    def set_budget(self):
        category_name = input('Enter the category name for which you want to set the budget: ')
        new_budget = float(input('Enter the new budget amount: '))

        category = self.session.query(Category).filter_by(name=category_name).first()
        if category:
            category.budget = new_budget
            self.session.commit()
            print(f'Budget for {category_name} has been updated to ${new_budget:.2f}')
        else:
            print('Category not found. Please ensure the category exists.') 
    
