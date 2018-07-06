from sanic import Sanic
from gino.ext.sanic import Gino
from sanic_babel import Babel


db = Gino()


def create_app():
    application = Sanic(__name__)
    application.config.from_pyfile('config.py')

    db.init_app(application)
    Babel(application, configure_jinja=False)

    from app import service
    from app import model
    from app import controller

    return application
