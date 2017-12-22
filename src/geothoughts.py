from src.models import Geothought

class Geothoughts:

    def __init__(self, session):
        self.session = session

    def add(self, geohash, lat, lng, message):
        new_thought = Geothought(geohash=geohash,
                                 lat=lat,
                                 lng=lng,
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
        result = self.session.query(Geothought).filter(Geothought.geohash == geohash)
        geothoughts = []
        for row in result:
            geothoughts.append(row.as_dict())
        return geothoughts