from src.geothoughts_connection import GeothoughtConnection

def handler(event, context):

    geothoughts = GeothoughtConnection('aws_postgres',
                                'password',
                                'postgres-instance.c4ogucrzk5k0.ap-northeast-1.rds.amazonaws.com',
                                '5432',
                                'postgres')
    http_method = event['method']

    if not http_method:
        return "Error, no http_method available"

    if http_method == 'GET':
        thoughts = geothoughts.get_all()
        return {"geothoughts": thoughts}

    if http_method == 'POST':
        geohash = 'testing'
        coordinates = '1234'
        message = 'this is a test'
        geothoughts.add(geohash, coordinates, message)

if __name__=="__main__":
  print handler(None, None)