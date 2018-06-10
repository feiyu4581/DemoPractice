# coding=utf-8
from __future__ import absolute_import

from flask import Flask, jsonify
from flask_principal import identity_loaded, RoleNeed, UserNeed
from flask_login import current_user

from app.ext import db, api, login_manager, session, principal
from app.exception import BaseException

def register_database(app):
    from app.auth import model

    db.init_app(app)
    db.app = app


def register_api(app):
    api.init_app(app)
    api.app = app

    from app.auth.api import UserResource, SessionResource

    api.add_resource(UserResource, '/user')
    api.add_resource(SessionResource, '/session')


def register_ext(app):
    login_manager.init_app(app)
    session.init_app(app)
    principal.init_app(app)

    from app import permisson


def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_pyfile('../config.py')

    register_database(flask_app)
    register_api(flask_app)
    register_ext(flask_app)

    @identity_loaded.connect_via(flask_app)
    def on_identity_loaded(sender, identity):
        identity.user = current_user

        if hasattr(current_user, 'id'):
            identity.provides.add(UserNeed(current_user.id))

        if hasattr(current_user, 'roles'):
            for role in current_user.roles:
                identity.provides.add(RoleNeed(role.name))

    @flask_app.errorhandler(BaseException)
    def handle_base_exception(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code

        return response

    return flask_app
