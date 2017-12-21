import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Geothought(Base):  
    __tablename__ = 'geothoughts'
    id = Column(Integer, primary_key=True)
    geohash = Column(String)
    coordinates = Column(String)
    message = Column(String)
    
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

def create_tables(db_engine):
	Base.metadata.create_all(db_engine)