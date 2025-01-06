from sqlalchemy import Column, DECIMAL, DATE, Integer, VARCHAR
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


class sdp(Base):
    __tablename__ = "sdp"

    date = Column(DATE, primary_key=True)
    year = Column(Integer)
    amount = Column(DECIMAL)
    sdp = Column(DECIMAL)


class certificate(Base):
    __tablename__ = "certificate"

    date = Column(DATE, primary_key=True)
    year = Column(Integer)
    amount = Column(DECIMAL)
    certificate = Column(DECIMAL)


class tbill(Base):
    __tablename__ = "tbill"

    date = Column(DATE, primary_key=True)
    year = Column(Integer)
    amount = Column(DECIMAL)
    tbill = Column(DECIMAL)


class vanguard(Base):
    __tablename__ = "vanguard"

    date = Column(DATE, primary_key=True)
    year = Column(Integer)
    amount = Column(DECIMAL)
    vanguard = Column(DECIMAL)


class schwab(Base):
    __tablename__ = "schwab"

    date = Column(DATE, primary_key=True)
    year = Column(Integer)
    amount = Column(DECIMAL)
    schwab = Column(DECIMAL)


class total(Base):
    __tablename__ = "totals"

    date = Column(DATE, primary_key=True)
    year = Column(Integer)
    amount = Column(DECIMAL)
    type = Column(VARCHAR)
    total = Column(DECIMAL)
