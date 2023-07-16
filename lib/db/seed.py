import random
from faker import Faker 
from models import Category, Expense, Income, engine, Base
from datetime import datetime
from sqlalchemy.orm import sessionmaker

fake = Faker()
Session = sessionmaker(bind=engine)
session = Session()

def generate_seed_data():
    categories = ['Food', 'Transportation', 'Housing', 'Utilities', 'Entertainment']
    
    category_instances = []

    for category_name in categories:
        category = Category(
            name=category_name, 
            budget=random.randint(100, 1000)
        )

        session.add(category)
        category_instances.append(category)

    for _ in range(20):
        expense = Expense(
            name=fake.text(max_nb_chars=20), 
            amount=random.uniform(5, 100),
            category=random.choice(category_instances),
            date=fake.date_time_this_decade(tzinfo=None)
        )

        session.add(expense) 

    for _ in range(5):
        income = Income(
            name=fake.job(), 
            amount=random.uniform(500, 3000),
            date=fake.date_time_this_decade(tzinfo=None)
        )

        session.add(income)
    
    session.commit()

if __name__ == '__main__':
    generate_seed_data()

