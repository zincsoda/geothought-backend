import unittest
from src.database_wrapper import DatabaseWrapper
from src.geothoughts import Geothoughts
from src.models import Geothought
from src.database_wrapper import prepare_test_database
from src.models import create_tables

def setup_module():

    test_db_url = prepare_test_database()
    db_wrapper = DatabaseWrapper(test_db_url)
    db_engine = db_wrapper.get_db_engine()
    create_tables(db_engine)

    session = db_wrapper.get_session()

    global geothoughts
    geothoughts = Geothoughts(session)

class TestGeothoughts(unittest.TestCase):

    def test_can_add_geothought(self):
        geothoughts.add("geohash_1", "1234, 1234", "A test message")
        geothoughts.add("geohash_2", "1234, 1234", "A test message")
        geothoughts.add("geohash_1", "1234, 1234", "A test message")

    def test_get_all(self):
        thoughts = geothoughts.get_all()
        assert len(thoughts) == 3

    def test_get_all_for_geohash(self):
        thoughts = geothoughts.get_all_for_geohash('geohash_1')
        assert len(thoughts) == 2