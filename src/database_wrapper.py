from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker

class DatabaseWrapper:

    def __init__(self, db_url):

        self.db_engine = create_engine(db_url)
        Session = sessionmaker(self.db_engine)

        # Assuming a single session is created for now
        self.session = Session()

    def get_session(self):
        return self.session

    def get_db_engine(self):
        return self.db_engine