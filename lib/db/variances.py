from models import Budget, Expense, Income, IncomeType, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

class Variance:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()
    
    def calculate_budget_actual_and_variance(self, budget_category):
        actual = sum(expense.amount for expense in budget.expenses)
        variance = budget.budget - actual
        budget.actual = actual
        budget.variance = variance
        self.session.commit()
    
    def calculate_income_type_actual_and_variance(self, income_type):
        actual = sum(income_type.expected for income in income_type.incomes)
        variance = income_type.expected - actual
        income_type.actual = actual
        income_type.variance = variance
        self.session.commit()
    
    def update_all_actuals_and_variances(self):
        budgets = self.session.query(Budget).all()
        for budget in budgets:
            self. calculate_budget_actual_and_variance(budget)
        
        all_income_types = self.session.query(IncomeType).all()
        for income_type in all_income_types:
            self.calculate_income_type_actual_and_variance(income_type)
