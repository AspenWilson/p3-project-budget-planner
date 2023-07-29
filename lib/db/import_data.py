import pandas as pd 
from models import Expense, Income, Budget, IncomeType, engine
from sqlalchemy.orm import sessionmaker
from helpers import commit_and_msg, line_print, get_first
import datetime

class ImportData:

    expenses_csv_file_path = '/Users/aspen/Downloads/Budget Planner CLI - Import_Expenses (1).csv' #Update this to your specific file path
    income_csv_file_path = '/Users/aspen/Downloads/Budget Planner CLI - Import_Income (1).csv' #Update this to your specific file path

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def import_all_expenses(self):

        df = pd.read_csv(ImportData.expenses_csv_file_path)

        total_rows = len(df)

        print('Command I1: Import expenses')
        line_print()
        choice = input("Have you checked your import file and made sure that all entries are correct and there are no duplicates? y/n: ")

        if choice.lower() == 'y':    
            for index, row in df.iterrows():
                category_name = row['Category Name']
                category = get_first(self.session, Budget, 'category', category_name)

                if category:
                    date = datetime.datetime.strptime(row['Date'], '%Y-%m-%d').date()

                    expense = Expense(
                        description = row['Expense Description'],
                        amount = row['Amount'],
                        date = date,
                        category = category
                    )
                    self.session.add(expense)
                else:
                    print(f"Expense category '{category_name}' not found. Skipping expense entry.")

            self.session.commit()
            print(f'Success! {total_rows} expenses have been imported. You may now delete these lines from your import file.')
        
        else:
            print('Import cancelled by user. Double check your import file and run this command again.')
        
    def import_all_income(self):

        df = pd.read_csv(ImportData.income_csv_file_path)

        total_rows = len(df)

        print('Command I2: Import income')
        line_print()
        choice = input("Have you checked your import file and made sure that all entries are correct and there are no duplicates? y/n: ")

        if choice.lower() == 'y':    
            for index, row in df.iterrows():
                income_type = row['Income Type']
                existing_income_type = get_first(self.session, IncomeType, 'name', income_type)

                if existing_income_type:
                    date = datetime.datetime.strptime(row['Date'], '%Y-%m-%d').date()

                    income = Income(
                        name = row['Income Name'],
                        amount = row['Amount'],
                        date = date,
                        income_type = existing_income_type
                    )
                    self.session.add(income)
                else:
                    print(f"Income type '{income_type}' not found. Skipping income entry.")

            self.session.commit()
            print(f'Success! {total_rows} income entries have been imported. You may now delete this lines from your import file.')
            
        
        else:
            print('Import cancelled by user. Double check your import file and run this command again.')