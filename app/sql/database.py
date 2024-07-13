from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import dotenv
import os

dotenv.load_dotenv()

# Load the credentials and database
creds = "{0}:{1}".format(os.environ.get("DB_USER"), os.environ.get("DB_PASS"))
database = "{0}/{1}".format(os.environ.get("DB_HOST"), os.environ.get("DB_DATABASE"))

database_url = "mysql+mysqlconnector://" + creds + "@" + database
engine = create_engine(database_url, echo=True)  # Set echo to True for debugging

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
