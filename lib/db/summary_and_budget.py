from models import Category, Expense, Income, IncomeType, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

class Budget:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def set_budget(self):
        total_income = float(input("Enter your expected monthly income: $"))

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

class Summary:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()


    def view_monthly_budget(self):
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