import os

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from list_activity_tracker.data_base_modles.user_model import User
class DBSession:
    factory = None
    engine = None


    @staticmethod
    def db_init(db_file):
        if DBSession.factory:
            return

        if not db_file or not db_file.strip():
            raise Exception("Database file not specified")

        connection_string = f"sqlite:///{db_file}"
        engine = sqlalchemy.create_engine(connection_string, echo=False)
        DBSession.engine = engine
        DBSession.factory = sessionmaker(bind=engine)
        Base.metadata.create_all(engine)
