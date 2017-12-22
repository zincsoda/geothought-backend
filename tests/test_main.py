import unittest
from src.main import get_db_session
from src.main import handler
from src.database_wrapper import setup_local_database_url
from src.database_wrapper import DatabaseWrapper
from src.models import create_tables

def setup_module():
    db_url = setup_local_database_url()
    db_wrapper = DatabaseWrapper(db_url)
    db_engine = db_wrapper.get_db_engine()
    create_tables(db_engine)

class TestMainFunction(unittest.TestCase):

    def test_1_get_db_session(self):
        assert get_db_session({}) != None

    def test_2_post_thought(self):
        event = {
            "method": "POST",        
            "body": {
                "geohash": "test_hash",
                "lat": "lat",
                "lng": "lng",
                "message": "message in a bottle"
            }
        }

        response = handler(event, None)
    
    def test_2_bad_post_thought(self):
        event = {
            "method": "POST",
            "body": {
                "geohash": "test_hash"
            }
        }

        response = handler(event, None)
        assert response["status_code"] == "400"

    def test_3_get_thoughts(self):
        event = {
            "method": "GET",
        }        
        response = handler(event, None)
        assert response["status_code"] == "200"
        assert response["body"]["geothoughts"][0]["geohash"] == "test_hash"
        assert response["body"]["geothoughts"][0]["lat"] == "lat"
        assert response["body"]["geothoughts"][0]["lng"] == "lng"
        assert response["body"]["geothoughts"][0]["message"] == "message in a bottle"
