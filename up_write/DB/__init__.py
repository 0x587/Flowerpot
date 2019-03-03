from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


base = declarative_base()
engine = create_engine("mysql+pymysql://root:python0408@cdb-ozn291s9.gz.tencentcdb.com:10089/Flowerpot", max_overflow=5)
Session = sessionmaker(bind=engine)
# 创建Session类实例
session = Session()
import up_write.DB.classes
