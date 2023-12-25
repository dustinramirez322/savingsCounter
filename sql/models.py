from sqlalchemy import Column, DECIMAL, DATE, Integer
from database import Base


# Define the ExtraMortage DB class
class ExtraMortgage(Base):
    __tablename__ = "ExtraMortgage"

    date = Column(DATE, primary_key=True)
    year = Column(Integer)
    amount = Column(DECIMAL)
    ExtraMortgage = Column(DECIMAL)


# Define the ShortTerm DB class
class ShortTerm(Base):
    __tablename__ = "ShortTerm"

    date = Column(DATE, primary_key=True)
    year = Column(Integer)
    amount = Column(DECIMAL)
    ShortTerm = Column(DECIMAL)