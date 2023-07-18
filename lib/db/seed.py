import random
from faker import Faker 
from models import Category, Expense, Income, IncomeType, engine, Base
from datetime import datetime
from sqlalchemy.orm import sessionmaker

fake = Faker()
Session = sessionmaker(bind=engine)
session = Session()

def generate_seed_data():
    categories = ['Food', 'Transportation', 'Housing', 'Utilities', 'Entertainment', 'Travel', 'Gifts', 'Medical', 'Personal', 'Pets']
    
    category_instances = []

    income_types = ['Paycheck', 'Bonus']

    income_type_instances = []

    for category_name in categories:
        category = Category(
            name=category_name, 
            budget=round(random.randint(100, 1000), 2),
            actual = 0.0,
            variance = 0.0
        )

        session.add(category)
        category_instances.append(category)

    for income_type_name in income_types:
        income_type = IncomeType(
            name=income_type_name,
            expected=round(random.randint(100, 1000), 2),
            actual = 0.0,
            variance = 0.0
        )

        session.add(income_type)
        income_type_instances.append(income_type)    

    for _ in range(20):
        expense = Expense(
            name=fake.text(max_nb_chars=15), 
            amount=round(random.uniform(5, 100), 2),
            category=random.choice(category_instances),
            date=fake.date_time_this_decade(tzinfo=None)
        )

        session.add(expense)

    for _ in range(5):
        income = Income(
            name=fake.job(), 
            amount=round(random.uniform(500, 3000), 2),
            date=fake.date_time_this_decade(tzinfo=None),
            income_type=random.choice(income_type_instances)
        )

        session.add(income)
    
    for category in category_instances:
        category.variance = category.budget - category.actual
    
    for income_type in income_type_instances:
        income_type.variance = income_type.expected - income_type.actual
    
    session.commit()

if __name__ == '__main__':
    generate_seed_data()

