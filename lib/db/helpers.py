from models import Budget, Expense, Income, IncomeType, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import extract, func
from datetime import datetime


Session = sessionmaker(bind=engine)
session = Session()

#defining constants to use in other folders
all_categories = session.query(Budget).all()
all_expenses = session.query(Expense).all()
all_income_types = session.query(IncomeType).all()
all_income_entries = session.query(Income).all()

current_year = datetime.now().year
current_month = datetime.now().month

line_print = lambda: print("-----------------------------------")

#defining functions to use in other folders

#filtering functions

def get_existing_category(session, category_name):
    return session.query(Budget).filter_by(category=category_name).first()

def get_existing_income_type(session, income_type_name):
    return session.query(IncomeType).filter_by(name=income_type_name).first()

def get_existing_entry(session, modal, key):
    return session.query(modal).get(key)

def get_total_expenses(session, month, year):
    total_expenses = session.query(func.sum(Expense.amount)).filter(extract('month',Expense.date) == month, extract('year', Expense.date) == year).scalar()
    return total_expenses or 0.0

def get_total_income(session, month, year):
    total_income = session.query(func.sum(Income.amount)).filter(extract('month', Income.date) == month, extract('year', Income.date) == year).scalar()
    return total_income or 0.0

#data entry functions

def date_entry(input_prompt='Enter the date (YYYY-MM-DD): '):
    while True:
        date_str = input(input_prompt)
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            break
        except ValueError:
            print('Invalid date format. Please use the format YYYY-MM-DD.')
    
    return date

def amount_entry(input_prompt):
    while True:
        amount_str = input(input_prompt)
        try:
            amount = float(amount_str)
            break
        except ValueError:
            print('Invalid input. Please enter a valid number.')
    return amount

#session commits 

def add_and_commit(session, obj, msg1):
    session.add(obj)
    session.commit()
    print(msg1)
    print(msg2)

def commit_and_msg(session, msg1, msg2):
    session.commit()
    print(msg1)
    print(msg2)

def delete_and_commit(session, obj, msg):
    session.delete(obj)
    session.commit()
    print(msg)


