# coding=utf-8
from __future__ import absolute_import
from passlib.hash import pbkdf2_sha256

from app.ext import db, login_manager
from app.exception import SessionExpired
from flask_login import UserMixin, AnonymousUserMixin, current_user
from sqlalchemy.sql import expression


users_roles = db.Table('users_role',
    db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('roles.id')))


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    name = db.Column(db.String(90), unique=True)
    description = db.Column(db.String(28))

    def __repr__(self):
        return '<Model Role {}>'.format(self.name)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    name = db.Column(db.String(64))
    login = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(255))

    is_active = db.Column(db.Boolean(), server_default=expression.text('True'), nullable=False)  # 这里使用 expression.true() 似乎不起作用

    roles = db.relationship(
        'Role',
        secondary=users_roles,
        backref=db.backref('users', lazy='dynamic')
    )

    def set_password(self, password):
        return pbkdf2_sha256.hash(password)

    def check_password(self, password):
        return pbkdf2_sha256.verify(password, self.password)

    def is_authenticated(self):
        return not isinstance(self, AnonymousUserMixin)

    def is_anonymous(self):
        return isinstance(self, AnonymousUserMixin)

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<Model User {}>'.format(self.name)


@login_manager.user_loader
def load_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        return user


@login_manager.unauthorized_handler
def unauthorized():
    raise SessionExpired()
