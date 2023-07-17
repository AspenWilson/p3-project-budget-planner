from models import Category, Expense, Income, IncomeType, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

class BudgetCLI:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def welcome_message(self):
        print("Welcome to your Budget Planner CLI!")
        print("-----------------------------------")
        print("You have many options to choose from to help you set and maintain your budget:")
        print("--> View: This shows you your current budgets, broken out by category.")
        print("--> Add_Expense: This is where you can add a new expense.")
        print("--> Add_Income: This is where you can add income.")
        print("--> Set_Budget: This is where you can set the budget for each category based on a percentage of your monthly income.")
        print("--> Summary: This is where you can see a brief summary of your total income, total expenses, and your remaining budget.")
        print("--> Delete_Expense: This is where you can delete an expense using the expense ID.")

#views and summaries

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

    def summary(self):
        total_income = sum([income.amount for income in self.session.query(Income).all()])
        total_expenses = sum([expense.amount for expense in self.session.query(Expense).all()])

        print (f"\nTotal Income: ${total_income:.2f}")
        print (f"Total Expenses: ${total_expenses:.2f}")
        print (f"Remaining Budget: ${total_income - total_expenses:.2f}\n")


#add records

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
        
        category = self.session.query(Category).filter_by(name=category_name).first()
        if category:
            expense = Expense(name=name, amount=amount, date=date, category=category)
            self.session.add(expense)
            self.session.commit()
            print('Expense added successfully!')
        else:
            print('Category not found. Please ensure the category exists.') 
    
    def add_income(self):
        name = input('Enter the name of the income: ')
        
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

        self.session.add(income)
        self.session.commit()
        print('Income added successfully!')

    def add_expense_category(self):
        category_name = input('Enter the name of the new expense category: ')

        existing_category = self.session.query(Category).filter_by(name=category_name).first()
        if existing_category:
            print('Category already exists. Please choose a different name or use existing category.')
            print(f'Current expense categories: {self.session.query(Category).all()}')
            return

        category = Category(name=category_name)
        self.session.add(category)
        self.session.commit()
        print('Category added successfully!')
        print(f'Updated expense categories: {self.session.query(Category).all()}')
    
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
        if remaining_budget < 0:
            print("Insufficient budget. The allocated percentage exceeds the total income.")
        else:
            print(f"\nRemaining budget after allocations: ${remaining_budget:.2f}\n")
    
#delete records

    def delete_income(self):
        income_id = int(input("Enter the ID of the income you want to delete: "))

        income = self.session.query(Income).get(income_id)
        if income:
            self.session.delete(income)
            self.session.commit()
            print(f"Income with ID {income_id} deleted successfully!")
        else:
            print(f"Income with ID {income_id} not found.")

    def delete_expense(self):
        expense_id = int(input("Enter the ID of the expense you want to delete:"))

        expense = self.session.query(Expense).get(expense_id)
        if expense:
            self.session.delete(expense)
            self.session.commit()
            print(f"Expense with ID {expense_id} deleted successfully!")
        else:
            print(f"Expense with ID {expense_id} not found.")

#update records

    def update_expense(self):
        expense_id = int(input("Enter the ID of the expense entry you want to update: "))

        expense = self.session.query(Expense).get(expense_id)
        if expense is None:
            print(f"Expense entry with ID {expense_id} not found.")
            return
        else:
            print(f"Expense details: {expense}")
            amount_str = input('Enter the updated amount for this expense entry: $')
            try:
                amount = float(amount_str) 
            except ValueError:
                print('Invalid amount. Please enter a valid number.')
                return
        
        expense.amount = amount
        self.session.commit()
        print(f"Expense with ID {expense_id} amount updated to ${amount} successfully.")
        print(f"Updated expense details: {expense}")

    def update_income(self):
        income_id = int(input("Enter the ID of the income entry you want to update: "))

        income = self.session.query(Income).get(income_id)
        if income is None:
            print(f"Income entry with ID {income_id} not found.")
            return
        else:
            print(f"Income details: {income}")
            amount_str = input('Enter the updated amount for this income entry: $')
            try:
                amount = float(amount_str) 
            except ValueError:
                print('Invalid amount. Please enter a valid number.')
                return
        
        income.amount = amount
        self.session.commit()
        print(f"Income with ID {income_id} amount updated to ${amount} successfully.")
        print(f"Updated income details: {income}")

    
