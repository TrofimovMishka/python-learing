class PositionOfISS:
    def __init__(self, latitude, longitude, timestamp):
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude

    def get_timestamp(self):
        return self.timestamp
