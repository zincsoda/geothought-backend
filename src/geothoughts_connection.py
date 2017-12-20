from sqlalchemy import create_engine  
from sqlalchemy import Column, String, Integer 
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

base = declarative_base()

class Geothought(base):  
    __tablename__ = 'geothoughts'
    id = Column(Integer, primary_key=True)
    geohash = Column(String)
    coordinates = Column(String)
    message = Column(String)
    
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class GeothoughtConnection:

    def __init__(self, username, password, host, port, database):
        url = 'postgresql+pg8000://{}:{}@{}:{}/{}'
        url = url.format(username,
                         password,
                         host,
                         port,
                         database)
        db = create_engine(url)
        
        Session = sessionmaker(db)  
        self.session = Session()

    def create_table(self):
        base.metadata.create_all(db)

    def add(self, geohash, coordinates, message):
        new_thought = Geothought(geohash=geohash,
                                 coordinates=coordinates,
                                 message=message)
        self.session.add(new_thought)  
        self.session.commit()

    def get_all(self):
        result = self.session.query(Geothought)
        geothoughts = []
        for row in result:
            geothoughts.append(row.as_dict())
        return geothoughts

    def get_all_for_geohash(self, geohash):
        pass


if __name__=="__main__":
    conn = GeothoughtConnection('aws_postgres',
                                'password',
                                'postgres-instance.c4ogucrzk5k0.ap-northeast-1.rds.amazonaws.com',
                                '5432',
                                'postgres')
    #conn.add("cepwsg", "1234, 12345", "A view of Shenzhen, HK Island and Pat Heung")
    #conn.add("cepwsg", "1234, 12345", "Best place for a motorbike")
    conn.get_all()