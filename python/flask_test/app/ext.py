# coding=utf-8
from __future__ import absolute_import

from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_login import LoginManager
from flask_session import Session
from flask_principal import Principal

db = SQLAlchemy()
api = Api()
login_manager = LoginManager()
session = Session()
principal = Principal()
