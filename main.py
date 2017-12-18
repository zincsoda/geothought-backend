def handler(event, context):
    data =[
        {
            "geohash": "cepwsg",
            "coords": "123,123",
            "message": "A view of Shenzhen, HK Island and Pat Heung"
        },
        {
            "geohash": "cepwsg",
            "coords": "123,123",
            "message": "I walk here every weekend"
        }
    ]
    return {"geothoughts": data}

if __name__=="__main__":
  print handler(None, None)