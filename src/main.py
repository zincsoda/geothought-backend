from src.geothoughts import Geothoughts
from src.database_wrapper import DatabaseWrapper
from src.database_wrapper import prepare_test_database
import os
from src.models import create_tables

def get_db_session(event):

    if 'running_in_aws' in os.environ:
        try:
            pg_db_url = 'postgresql+pg8000://%s:%s@%s:%s/%s' % (
                    os.environ['pg_username'],
                    os.environ['pg_password'],
                    os.environ['pg_hostname'],
                    os.environ['pg_port'],
                    os.environ['pg_database']
                )
        except Exception as e:
            print "Error getting postgres enviornment variables: ", e
            return None 
        db_wrapper = DatabaseWrapper(pg_db_url)
    else:
        # We assume that the test database and tables are already created
        test_db_url = prepare_test_database(reset=False)
        db_wrapper = DatabaseWrapper(test_db_url)

    return db_wrapper.get_session()

def handler(event, context):

    print event

    # TODO: Return correct errors
    session = get_db_session(event)
    if not session:
        return "Error, no http_method available"
    geothoughts = Geothoughts(session)

    if 'method' in event:
        http_method = event['method']
    else:
        return "Error, no http_method available"

    if http_method == 'GET':

        # TODO: Get thoughts for geohash

        thoughts = geothoughts.get_all()
        return {"geothoughts": thoughts}

    if http_method == 'POST':

        try: 
            geohash = event['body']['geohash']
            coordinates = event['body']['coordinates']
            message = event['body']['message']
        except Exception as e:
            print "Error getting required parameters from body: ", e
            return "500 Error creating a record"
        else:
            geothoughts.add(geohash, coordinates, message)
