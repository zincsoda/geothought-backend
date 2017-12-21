import unittest
from sqlalchemy import create_engine
from src.database_wrapper import DatabaseWrapper
from src.models import create_tables
import os

def prepare_new_test_database():
    sqlite_file = 'test.db'
    if os.path.isfile(sqlite_file):
        os.remove(sqlite_file)
    db_url = 'sqlite:///%s' % sqlite_file
    return db_url

def setup_module():
    global db_wrapper 
    db_url = prepare_new_test_database()    
    db_wrapper = DatabaseWrapper(db_url)

class TestDatabaseWrapper(unittest.TestCase):

    def test_get_session(self):
        assert db_wrapper.get_session() is not None

    def test_get_db_engine(self):
        assert db_wrapper.get_db_engine() is not None

    def test_create_tables(self):
        db_engine = db_wrapper.get_db_engine()
        create_tables(db_engine)