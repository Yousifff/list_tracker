import sqlalchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from list_activity_tracker.data_base_modles.db_session import Base
import datetime


class User(Base):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,autoincrement=True)
    username = sqlalchemy.Column(sqlalchemy.String,nullable=False,index=True)
    password = sqlalchemy.Column(sqlalchemy.String,nullable=False)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,default=datetime.datetime.now)
    user_tasks = relationship("UserTask",back_populates="user",cascade="all, delete-orphan")


class UserTask(Base):
    __tablename__ = 'tasks'
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True,autoincrement=True)
    tasks = sqlalchemy.Column(sqlalchemy.String,nullable=False)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,ForeignKey('users.id'))

    user = relationship("User",back_populates="user_tasks")