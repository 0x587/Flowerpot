from DB import base, engine
from sqlalchemy import Column, Float, Integer, DateTime
from datetime import datetime


class Record:
    record_id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(DateTime)


class StateRecord(Record, base):
    __tablename__ = 'state_records'
    """
    Some attribute
    """
    air_temperature = Column(Float)
    air_humidity = Column(Float)
    soil_temperature = Column(Float)
    soil_humidity = Column(Float)

    def __init__(self, air_temperature=0, air_humidity=0, soil_temperature=0, soil_humidity=0):
        self.air_temperature = air_temperature
        self.air_humidity = air_humidity
        self.soil_temperature = soil_temperature
        self.soil_humidity = soil_humidity
        self.datetime = datetime.now()

    def __repr__(self):
        return 'State record in %s' % self.datetime


class DrenchedRecord(Record, base):
    __tablename__ = 'drenched_records'
    water_size = Column(Integer)

    def __init__(self, water_size):
        self.water_size = water_size

    def __repr__(self):
        return 'record in %s' % self.datetime


base.metadata.create_all(engine)
