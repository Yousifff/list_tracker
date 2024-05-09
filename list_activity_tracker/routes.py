import os
from list_activity_tracker.data_base_modles.db_session import DBSession
def includeme(config):

    db_file = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            'db',
            'activity_tracker.db'
        )
    )

    DBSession.db_init(db_file)

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('register','/register')
    config.add_route('login','/login')
    config.add_route('account','/account')
