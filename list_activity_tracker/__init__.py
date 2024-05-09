from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        session_factory = SignedCookieSessionFactory("secure")
        config.set_session_factory(session_factory)
        config.include('pyramid_chameleon')
        config.include('.routes')
        config.scan()
    return config.make_wsgi_app()
