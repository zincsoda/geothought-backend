import unittest
from src.main import get_db_session
from src.main import handler
from src.database_wrapper import prepare_test_database
from src.database_wrapper import DatabaseWrapper
from src.models import create_tables

def setup_module():
    test_db_url = prepare_test_database()
    db_wrapper = DatabaseWrapper(test_db_url)
    db_engine = db_wrapper.get_db_engine()
    create_tables(db_engine)

class TestMainFunction(unittest.TestCase):

    def test_1_get_db_session(self):
        assert get_db_session({}) != None

    def test_2_post_thought(self):
        event = {
            "method": "POST",
            "geohash": "test_hash",
            "coordinates": "coordinates",
            "message": "message in a bottle"
        }

        response = handler(event, None)
    
    def test_2_bad_post_thought(self):
        event = {
            "method": "POST",
            "geohash": "test_hash"
        }

        response = handler(event, None)        

    def test_3_get_thoughts(self):
        event = {
            "method": "GET"
        }        
        response = handler(event, None)
        assert response["geothoughts"][0]["geohash"] == "test_hash"
        assert response["geothoughts"][0]["coordinates"] == "coordinates"
        assert response["geothoughts"][0]["message"] == "message in a bottle"
