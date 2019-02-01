from DB import base, engine
from sqlalchemy import Column, Float, Integer, DateTime
from datetime import datetime


class Record(base):
    __tablename__ = 'records'
    """
    Some attribute
    """
    record_id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(DateTime)
    air_temperature = Column(Float)
    air_humidity = Column(Float)
    soil_temperature = Column(Float)
    soil_humidity = Column(Float)
    luminance = Column(Float)

    def __init__(self):
        self.datetime = datetime.now()

    def __repr__(self):
        return 'date:%s' % self.datetime


base.metadata.create_all(engine)
