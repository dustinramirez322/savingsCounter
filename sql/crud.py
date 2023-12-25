from sqlalchemy.orm import sessionmaker
import sys
import dotenv
import os

dotenv.load_dotenv()

sys.path.insert(0, os.environ.get("SYS_PATH"))
import models
import database

engine = database.engine

def post_new(input, type):
    Session = sessionmaker(bind=engine)
    session = Session()
    if type == 'ShortTerm':
        new_data = models.ShortTerm(**input)
    if type == 'ExtraMortgage':
        new_data = models.ExtraMortgage(**input)

    try:
        session.add(new_data)
        session.commit()
        session.close()

    except Exception as e:
        print(e)
        session.close()
        pass


def get_total(type):
    Session = sessionmaker(bind=engine)
    session = Session()
    list = []
    if type == 'ShortTerm':
        answer = session.query(models.ShortTerm).all()
    if type == 'ExtraMortgage':
        answer = session.query(models.ExtraMortgage).all()
    for a in answer:
        list.append(float(a.amount))
    session.commit()
    session.close()
    return round(sum(list), 2)
