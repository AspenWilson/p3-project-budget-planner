from models import Budget, Expense, Income, IncomeType, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import extract, func
from datetime import datetime


Session = sessionmaker(bind=engine)
session = Session()

#defining constants to use in other folders

current_year = datetime.now().year
current_month = datetime.now().month

line_print = lambda: print("-----------------------------------")

#defining functions to use in other folders

#filtering/get functions

def get_all(session, modal):
    return session.query(modal).all()

def get_first(session, model, attribute, value):
    return session.query(model).filter(getattr(model, attribute) == value).first()

def get_existing_entry(session, modal, key):
    return session.query(modal).get(key)

def get_total(session, modal, month, year):
    total = session.query(func.sum(modal.amount)).filter(extract('month', modal.date) == month, extract('year', modal.date) == year).scalar()
    return total or 0.0

#data entry functions

def date_entry(input_prompt):
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

def add_and_commit(session, obj, msg1, msg2):
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


