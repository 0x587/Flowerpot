from sqlalchemy import Column, String, Integer, ForeignKey, Float, DateTime, PickleType, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
base = declarative_base()
engine = create_engine(r'sqlite:///F:\File\Flowerpot\Flowerpot\App\DataBase\data.db')
Session = sessionmaker(bind=engine)
# 创建Session类实例
session = Session()


class Record(base):
    __tablename__ = 'records'
    """
    Some attribute
    """
    record_id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(DateTime)


base.metadata.create_all(engine)
