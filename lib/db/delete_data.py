from models import Budget, Expense, Income, IncomeType, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

class DeleteData:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

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
    
    def delete_seed_data(self):
        response = input('Are you sure you want to delete all seed data? (y/n): ')
        if response.lower() == 'y':
            self.session.query(Expense).delete()
            self.session.query(Income).delete()
            self.session.query(Budget).delete()
            self.session.query(IncomeType).delete()
            self.session.commit()
            print('Seed data has been deleted.')
        else:
            print('Operation canceled. Seed data was not deleted.')
