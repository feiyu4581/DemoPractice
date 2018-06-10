# coding=utf-8
from __future__ import absolute_import

from flask import request, current_app, session
from flask_restful import Resource
from flask_login import login_user, current_user, logout_user, login_required
from flask_principal import Identity, AnonymousIdentity, identity_changed

from app.auth.model import User, Role
from app.exception import LoginError
from app.response import MessageResponse
from app.permisson import admin_permission
from app.exception import MessageException
from app.ext import db


class UserResource(Resource):
    @login_required
    def get(self):
        return {'hello': 'fds'}

    def post(self):
        name = request.json.get('name')
        login = request.json.get('login')
        password = request.json.get('password')

        user = User.query.filter_by(login=login).first()
        if user:
            raise MessageException('Repeated User')
        
        user = User(id=1, name=name, login=login, is_active=True)
        user.password = user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return MessageResponse('Register Ok')

    def put(self):
        role_names = request.json.get('roles')
        roles = Role.query.filter(Role.name.in_(role_names)).all()

        current_user.roles = roles

        db.session.commit()


class SessionResource(Resource):

    @admin_permission.require(403)
    def get(self):
        return {
            'error': 'ok'
        }

    def post(self):
        login, password = request.json.get('login'), request.json.get('password')

        if login and password:
            user = User.query.filter_by(login=login).first()
            if user and user.check_password(password):
                login_user(user)

                identity_changed.send(current_app._get_current_object(),
                                      identity=Identity(user.id))

                return MessageResponse('Login Success')

        raise LoginError()

    def delete(self):
        logout_user()

        for key in ('identity.name', 'identity.auth_type'):
            session.pop(key, None)

        identity_changed.send(current_app._get_current_object(),
                              identity=AnonymousIdentity())

        return MessageResponse('Logout Success')
