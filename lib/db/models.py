from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()
DB_URL = 'sqlite:///budget_planner.db'

class Budget(Base):
    __tablename__ = 'monthly_budget'

    id = Column(Integer, primary_key=True)
    category = Column(String(100), unique=True, nullable= False)
    budget = Column(Float, default=0.0)
    actual = Column(Float, default=0.0)
    variance = Column(Float, default=0.0)

    expenses = relationship('Expense', back_populates='category')

    def __repr__(self):
        return f'{self.category} (ID: {self.id})' 

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column (Integer, primary_key=True)
    date = Column(Date, nullable=False)
    name = Column(String(100), nullable=False)
    amount = Column(Float, nullable=False)

    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='expenses')

    def __repr__(self):
        return f'Expense #{self.id}: {self.name}, ' + \
            f'Amount: ${self.amount:.2f}, ' + \
            f'Date: {self.date}, ' + \
            f'Category: {self.category}'

class IncomeType(Base):
    __tablename__ = 'income_type'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    expected = Column(Float, default=0.0)
    actual = Column(Float, default=0.0)
    variance = Column(Float, default=0.0)

    incomes = relationship('Income', back_populates='income_type')

    def __repr__(self):
        return f'{self.name} (ID: {self.id})'

class Income(Base):
    __tablename__ = 'income'

    id = Column(Integer, primary_key=True)
    date = Column(Date,nullable=False)
    name = Column(String(100), nullable = False)
    amount = Column(Float, nullable= False)

    income_type_id = Column(Integer, ForeignKey('income_type.id'))
    
    income_type = relationship('IncomeType', back_populates='incomes')

    def __repr__(self):
        return f'Income #{self.id}: {self.name}, ' + \
            f'Amount: ${self.amount:.2f}, ' + \
            f'Date: {self.date}, ' + \
            f'Type: {self.income_type}'


engine = create_engine(DB_URL)
Base.metadata.create_all(engine)
