from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


base = declarative_base()
engine = create_engine(r'sqlite:///E:\Projects\Flowerpot\DB\DB_data\DB.db')
Session = sessionmaker(bind=engine)
# 创建Session类实例
session = Session()
import DB.classes
