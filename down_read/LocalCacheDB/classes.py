from down_read.DB import base, engine
from sqlalchemy import Column, Float, Integer, DateTime
from datetime import datetime


class StateRecord(base):
    __tablename__ = 'states'
    """
    Some attribute
    """
    record_id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(DateTime)
    temperature = Column(Float)
    humidity = Column(Float)
    light = Column(Float)

    def __init__(self, light=0, date_time=None):
        self.light = light
        if date_time is None:
            self.datetime = datetime.now()
        else:
            self.datetime = date_time

    def __repr__(self):
        return 'State record in %s' % self.datetime


base.metadata.create_all(engine)
