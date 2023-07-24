from models import Budget, Expense, Income, IncomeType, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy import extract, func
from helpers import current_year, current_month, get_all

class Variance:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()
    
    def monthly_expenses_by_category(self, month, year):
        expenses_by_category = self.session.query(Budget.category, func.sum(Expense.amount)).\
            join(Expense).\
            filter(extract('month', Expense.date) == month,
                   extract('year', Expense.date) == year).\
            group_by(Budget.category).all()
        
        return {category: total_expenses for category, total_expenses in expenses_by_category}
    
    def monthly_income_by_type(self, month, year):
        income_by_type = self.session.query(IncomeType.name, func.sum(Income.amount)).\
            join(Income).\
            filter(extract('month', Income.date) == month,
                   extract('year', Income.date) == year).\
            group_by(IncomeType.name).all()
        
        return {income_type: total_income for income_type, total_income in income_by_type}

    def calculate_budget_actual_and_variance(self, budget_category):

        expenses_by_category = self.monthly_expenses_by_category(current_month, current_year)

        if budget_category.category in expenses_by_category:
            actual = expenses_by_category[budget_category.category]
        else:
            actual = 0

        variance = budget_category.budget - actual
        budget_category.actual = actual
        budget_category.variance = variance
        self.session.commit()
    
    def calculate_income_type_actual_and_variance(self, income_type):

        income_by_type = self.monthly_income_by_type(current_month, current_year)

        if income_type.name in income_by_type:
            actual = income_by_type[income_type.name]
        else:
            actual = 0

        variance = actual - income_type.expected
        income_type.actual = actual
        income_type.variance = variance
        self.session.commit()
    
    def update_all_actuals_and_variances(self):
        print('Command U3: Update actual and variance numbers for Monthly Budget and Monthly Income')
        print("-----------------------------------")
        for budget in get_all(self.session, Budget):
            self.calculate_budget_actual_and_variance(budget)
        
        for income_type in get_all(self.session, IncomeType):
            self.calculate_income_type_actual_and_variance(income_type)

