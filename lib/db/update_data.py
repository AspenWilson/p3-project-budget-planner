from models import Category, Expense, Income, IncomeType, engine
from variances import Variance
from sqlalchemy.orm import sessionmaker
from datetime import datetime

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