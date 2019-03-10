from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()
engine = create_engine('sqlite:///F:\File\Flowerpot\Flowerpot\down_read\LocalCacheDB\DB.db')
Session = sessionmaker(bind=engine)
# 创建Session类实例
session = Session()
import down_read.LocalCacheDB.classes
