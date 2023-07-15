from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
DB_URL = 'sqlite:///budget_planner.db'

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable= False)
    budget = Column(Float, default=0.0)

    expenses = relationship('Expense', back_populates='category')


class Expense(Base):
    __tablename__ = 'expenses'

    id = Column (Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    amount = Column(Float, nullable=False)

    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='expenses')


class Income(Base):
    __tablename__ = 'income'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable = False)
    amount = Column(Float, nullable= False)


engine = create_engine(DB_URL)
Base.metadata.create_all(engine)
