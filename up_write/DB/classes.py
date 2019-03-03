from up_write.DB import base, engine
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

    def __init__(self, light=0):
        self.light = light
        self.datetime = datetime.now()

    def __repr__(self):
        return 'State record in %s' % self.datetime


base.metadata.create_all(engine)
