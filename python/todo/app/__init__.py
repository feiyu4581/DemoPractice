# coding=utf-8
from __future__ import absolute_import
from flask import Flask
import config

def create_app():
    flask_app = Flask(__name__, instance_relative_config=True)

    flask_app.config.from_object(config)
    flask_app.config.from_pyfile('config.py')

    from app.index.views import index
    flask_app.register_blueprint(index, url_prefix='/')

    return flask_app
