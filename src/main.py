from src.geothoughts import Geothoughts
from src.database_wrapper import DatabaseWrapper
from src.database_wrapper import setup_local_database_url
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
        test_db_url = setup_local_database_url(reset=False)
        db_wrapper = DatabaseWrapper(test_db_url)

    return db_wrapper.get_session()

def handler(event, context):

    print event

    session = get_db_session(event)
    if not session:
        error_response = {
            "status_code": '400',
            "body": { "error": 'Unable to retrieve database session' },
            "headers": {'Content-Type': 'application/json'}
        }
        return error_response
    
    geothoughts = Geothoughts(session)

    if 'method' not in event:
        print "No HTTP method present in request"
        error_response = {
            "status_code": '400',
            "body": { "error": 'No HTTP method present in request' },
            "headers": {'Content-Type': 'application/json'}
        }
        return error_response

    http_method = event['method']

    if http_method == 'GET':

        # TODO: Get thoughts for specific geohash

        thoughts = geothoughts.get_all()
        success_response = {
            "status_code": '200',
            "body": { "geothoughts": thoughts },
            "headers": {'Content-Type': 'application/json'}
        }
        return success_response

    if http_method == 'POST':

        try:
            geohash = event['body']['geohash']
            coordinates = event['body']['coordinates']
            message = event['body']['message']
        except Exception as e:
            print "Error parsing request body: ", e
            error_response = {
                "status_code": '400',
                "body": { "error": 'Invalid request body: %s' % e},
                "headers": {'Content-Type': 'application/json'}
            }
            return error_response
        try:
            geothoughts.add(geohash, coordinates, message)
        except Exception as e:
            print "Error parsing request body: ", e
            error_response = {
                "status_code": '400',
                "body": { "error": 'Error saving data: %s' % e},
                "headers": {'Content-Type': 'application/json'}
            }
            return error_response
        
        success_response = {
            "status_code": '201',
            "headers": {'Content-Type': 'application/json'}
        }
        return success_response
