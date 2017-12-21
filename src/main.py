from src.geothoughts import Geothoughts

def handler(event, context):

    pg_db_url = 'postgresql://%s:%s@%s:%s/%s' % ('aws_postgres',
         'password',
         'postgres-instance.c4ogucrzk5k0.ap-northeast-1.rds.amazonaws.com',
         '5432',
         'postgres')
    db_wrapper = DatabaseWrapper(pg_db_url)
    session = db_wrapper.get_session()
    geothoughts = Geothoughts(session)

    http_method = event['method']

    if not http_method:
        return "Error, no http_method available"

    if http_method == 'GET':
        thoughts = geothoughts.get_all(_for_geohash('geohash_1'))
        return {"geothoughts": thoughts}

    if http_method == 'POST':
        geohash = 'testing'
        coordinates = '1234'
        message = 'this is a test'
        geothoughts.add(geohash, coordinates, message)