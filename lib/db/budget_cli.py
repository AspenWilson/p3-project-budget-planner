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


        self.session.add(income)
        self.session.commit()
        print('Income added successfully!')

    
    def set_budget(self):
        total_income = float(input("Enter your total income: $"))

        categories = self.session.query(Category).all()
        total_budget = 0

        for category in categories:
            percent = float(input(f"Enter the percentage of income to allocate for {category.name}: "))
            budget = (percent/100) * total_income
            total_budget += budget
            category.budget = budget
            self.session.commit()
        
        remaining_budget = total_income - total_budget
        print(f"\nRemaining budget after allocations: ${remaining_budget:.2f}\n")

    def summary(self):
        total_income = sum([income.amount for income in self.session.query(Income).all()])
        total_expenses = sum([expense.amount for expense in self.session.query(Expense).all()])

        print (f"\nTotal Income: ${total_income:.2f}")
        print (f"Total Expenses: ${total_expenses:.2f}")
        print (f"Remaining Budget: ${total_income - total_expenses:.2f}\n")

    def delete_expense(self):
        expense_id = int(input("Enter the ID of the expense you want to delete:"))

        expense = self.session.query(Expense).get(expense_id)
        if expense:
            self.session.delete(expense)
            self.session.commit()
            print(f"Expense with ID {expense_id} deleted successfully!")
        else:
            print(f"Expense with ID {expense_id} not found.")


    
