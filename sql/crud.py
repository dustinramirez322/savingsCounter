from sqlalchemy.orm import sessionmaker
import sys
import os


# Load the sys path necessary to call other database modules
sysPath = os.getcwd()+'/sql'
sys.path.insert(0, sysPath)
import models
import database

engine = database.engine


def post_new(input, type):
    Session = sessionmaker(bind=engine)
    session = Session()
    # determine which table to insert the new data into based of the deposit type
    if type == 'ShortTerm':
        new_data = models.ShortTerm(**input)
    if type == 'ExtraMortgage':
        new_data = models.ExtraMortgage(**input)

    try:
        # Add the new data to the database
        session.add(new_data)
        session.commit()
        session.close()

    except Exception as e:
        # print error and close the session if it fails
        print(e)
        session.close()
        pass


def get_total(type):
    Session = sessionmaker(bind=engine)
    session = Session()
    list = []
    # Get all the deposits currently in the selected table type
    if type == 'ShortTerm':
        answer = session.query(models.ShortTerm).all()
    if type == 'ExtraMortgage':
        answer = session.query(models.ExtraMortgage).all()
    # Create a list of all deposits
    for a in answer:
        list.append(float(a.amount))
    session.commit()
    session.close()
    # Return the sum of all deposits in the list and round the float to two decimal places
    return round(sum(list), 2)
