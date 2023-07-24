from models import Budget, Expense, Income, IncomeType, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from helpers import all_categories, all_income_types, get_existing_entry, line_print, delete_and_commit

class DeleteData:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def delete_income(self):
        print('Command D2: Delete an income entry')
        line_print()

        income_id = int(input("Enter the ID of the income you want to delete: "))

        income = get_existing_entry(self.session, Income, income_id)
        
        if income:
            print(f"Income entry details: {income}")
            choice = input("Are you sure to want to delete this entry? y/n: ")
            
            if choice == 'y':
                delete_and_commit(self.session, income, f"Income with ID {income_id} deleted successfully!")
            else: 
                print('Income entry deletion cancelled by user.')
        else:
            print(f"Income with ID {income_id} not found.")

    def delete_expense(self):
        print('Command D1: Delete an expense entry')
        line_print()

        expense_id = int(input("Enter the ID of the expense you want to delete:"))

        expense = get_existing_entry(self.session, Expense, expense_id)
        if expense:
            print(f"Expense entry details: {expense}")
            choice = input("Are you sure to want to delete this entry? y/n: ")
            
            if choice == 'y':
                delete_and_commit(self.session, expense, f"Expense with ID {expense_id} deleted successfully!")
            else:
                print('Expense entry deletion cancelled by user.')
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
            print('Operation cancelled. Seed data was not deleted.')
    
    def delete_expense_category(self):
        print('Command D3: Delete an expense category')
        line_print()

        print(f'All expense categories: {all_categories}')
        expense_category_id = int(input("Enter the ID of the expense category you'd like to delete: "))

        category = get_existing_entry(self.session, Budget, expense_category_id)
        
        if category:
            print(f'{category}')
            choice = input('WARNING: You are about to delete an expense category. This action cannot be undone. You should ensure there are no expenses currently tagged to this category. Are you sure you want to delete? y/n: ')
            
            if choice == 'y':
                delete_and_commit(self.session, category, f"Expense category {category} deleted successfully!")
            else:
                print('Expense category deletion cancelled by user.')
        else:
            print(f"Expense category with ID {expense_category_id} not found.")
    
    def delete_income_type(self):
        print('Command D4: Delete an income type')
        line_print()

        print(f"Current income types: {all_income_types}")
        income_type_id = int(input("Enter the ID of the income type you'd like to delete: "))

        income_type = get_existing_entry(self.session, IncomeType, income_type_id)
        
        if income_type:
            print(f'{income_type}')
            choice = input('WARNING: You are about to delete an income type. This action cannot be undone. You should ensure there are no income entries currently tagged to this income type. Are you sure you want to delete? y/n: ')
            
            if choice == 'y':
                delete_and_commit(self.session, income_type,f"Income type {income_type} deleted successfully!")
            else:
                print('Expense category deletion cancelled by user.')
        else:
            print(f'Income type with ID {income_type_id} not found.')