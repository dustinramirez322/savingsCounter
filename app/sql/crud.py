from sqlalchemy.orm import sessionmaker
import models
import database

engine = database.engine


def post_new(amount, deposit_type):
    Session = sessionmaker(bind=engine)
    session = Session()
    # determine which table to insert the new data into based of the deposit type
    if deposit_type == 'sdp':
        new_data = models.sdp(**amount)
    if deposit_type == 'certificate':
        new_data = models.certificate(**amount)
    if deposit_type == 'tbill':
        new_data = models.tbill(**amount)
    if deposit_type == 'vanguard':
        new_data = models.vanguard(**amount)
    if deposit_type == 'ExtraMortgage':
        new_data = models.ExtraMortgage(**amount)
    if deposit_type == 'schwab':
        new_data = models.schwab(**amount)


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


def get_type_total(deposit_type):
    Session = sessionmaker(bind=engine)
    session = Session()
    deposit_list = []
    # Get all the deposits currently in the selected table type
    if deposit_type == 'sdp':
        answer = session.query(models.sdp).all()
    if deposit_type == 'certificate':
        answer = session.query(models.certificate).all()
    if deposit_type == 'tbill':
        answer = session.query(models.tbill).all()
    if deposit_type == 'vanguard':
        answer = session.query(models.vanguard).all()
    if deposit_type == 'ExtraMortgage':
        answer = session.query(models.ExtraMortgage).all()
    if deposit_type == 'schwab':
        answer = session.query(models.schwab).all()

    # Create a list of all deposits
    for a in answer:
        deposit_list.append(float(a.amount))
    session.commit()
    session.close()
    # Return the sum of all deposits in the list and round the float to two decimal places
    return round(sum(deposit_list), 2)



def update_type_total(deposit_type, total):
    Session = sessionmaker(bind=engine)
    session = Session()
    if deposit_type == 'sdp':
        record = session.query(models.sdp).filter(models.sdp.date == "2025-12-31").one_or_none()
        record.sdp = total
    if deposit_type == 'certificate':
        record = session.query(models.certificate).filter(models.certificate.date == "2025-12-31").one_or_none()
        record.certificate = total
    if deposit_type == 'tbill':
        record = session.query(models.tbill).filter(models.tbill.date == "2025-12-31").one_or_none()
        record.tbill = total
    if deposit_type == 'vanguard':
        record = session.query(models.vanguard).filter(models.vanguard.date == "2025-12-31").one_or_none()
        record.vanguard = total
    if deposit_type == 'ExtraMortgage':
        record = session.query(models.ExtraMortgage).filter(models.ExtraMortgage.date == "2025-12-31").one_or_none()
        record.ExtraMortgage = total
    if deposit_type == 'schwab':
        record = session.query(models.schwab).filter(models.schwab.date == "2025-12-31").one_or_none()
        record.schwab = total
    session.commit()
    session.close()


def get_current_total():
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(models.total).count()
    total_rows = int(str(rows))
    totals = session.query(models.total).order_by('total')
    current_total = str(totals[total_rows-1].total)
    session.commit()
    session.close()
    return current_total


def update_total(total_update):
    Session = sessionmaker(bind=engine)
    session = Session()
    new_data = models.total(**total_update)

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

