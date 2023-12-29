from sqlalchemy.orm import sessionmaker
import sys
import os


# Load the sys path necessary to call other database modules
#sysPath = os.getcwd()+'/sql'
#sys.path.insert(0, sysPath)
import models
import database

engine = database.engine


def post_new(amount, deposit_type):
    Session = sessionmaker(bind=engine)
    session = Session()
    # determine which table to insert the new data into based of the deposit type
    if deposit_type == 'ShortTerm':
        new_data = models.ShortTerm(**amount)
    if deposit_type == 'ExtraMortgage':
        new_data = models.ExtraMortgage(**amount)

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


def get_total(deposit_type):
    Session = sessionmaker(bind=engine)
    session = Session()
    deposit_list = []
    # Get all the deposits currently in the selected table type
    if deposit_type == 'ShortTerm':
        answer = session.query(models.ShortTerm).all()
    if deposit_type == 'ExtraMortgage':
        answer = session.query(models.ExtraMortgage).all()
    # Create a list of all deposits
    for a in answer:
        deposit_list.append(float(a.amount))
    session.commit()
    session.close()
    # Return the sum of all deposits in the list and round the float to two decimal places
    return round(sum(deposit_list), 2)
