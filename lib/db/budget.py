from models import Budget, Expense, Income, IncomeType, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

class Budget:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def set_budget(self):
        total_income = float(input("Enter your expected monthly income: $"))

        budgets = self.session.query(Budget).all()
        total_budget = 0

        for category in budgets:
            percent = float(input(f"Enter the percentage of income to allocate for {budget.category}: "))
            budget = (percent/100) * total_income
            total_budget += budget
            budget.budget = budget
            self.session.commit()
        
        remaining_budget = total_income - total_budget
        if remaining_budget < 0:
            print("Insufficient budget. The allocated percentage exceeds the total income.")
        else:
            print(f"\nRemaining budget after allocations: ${remaining_budget:.2f}\n")
