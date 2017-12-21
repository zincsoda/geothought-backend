from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
import os

def prepare_test_database(reset=True):
    sqlite_file = 'test.db'
    if reset:
        if os.path.isfile(sqlite_file):
            os.remove(sqlite_file)
    db_url = 'sqlite:///%s' % sqlite_file
    return db_url

class DatabaseWrapper:

    def __init__(self, db_url):

        self.db_engine = create_engine(db_url)
        Session = sessionmaker(self.db_engine)

        # FIXME: Assuming a single session is created for now
        self.session = Session()

    def get_session(self):
        return self.session

    def get_db_engine(self):
        return self.db_engine