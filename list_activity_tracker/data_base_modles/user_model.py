import sqlalchemy
from list_activity_tracker.data_base_modles.db_session import Base
import datetime


class User(Base):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,autoincrement=True)
    username = sqlalchemy.Column(sqlalchemy.String,nullable=False,index=True)
    password = sqlalchemy.Column(sqlalchemy.String,nullable=False)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,default=datetime.datetime.now)