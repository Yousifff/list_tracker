from list_activity_tracker.data_base_modles.user_model import User
from list_activity_tracker.data_base_modles.db_session import DBSession


def create_user(username: str, password: str):
    session = DBSession.factory()
    user = User()
    user.username = username
    user.password = password

    session.add(user)
    session.commit()
    return user


def get_user_by_username(username: str):
    session = DBSession.factory()
    user = session.query(User).filter(User.username == username).first()
    if not user:
        return None
    return user
