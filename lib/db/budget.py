from models import Budget, Expense, Income, IncomeType, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from helpers import all_categories

class SetBudget:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def set_budget(self):
        print('Command 2: Set your monthly budget by category, based on expected income')
        print("-----------------------------------")
        total_income = float(input("Enter your expected total monthly income: $"))

        total_budget = 0
        remaining_percent = 100

        for budget in all_categories:
            percent = float(input(f"Enter the percentage of income to allocate for {budget.category}: "))
            remaining_percent -= percent
            print(f"Remaining percentage of budget: {remaining_percent}%.")
            new_budget = (percent/100) * total_income
            total_budget += new_budget
            budget.budget = new_budget
            self.session.commit()
        
        remaining_budget = total_income - total_budget
        if remaining_budget < 0:
            print("Insufficient budget. The allocated percentage exceeds the total income.")
        else:
            print(f"\nRemaining budget after allocations: ${remaining_budget:.2f}\n")
