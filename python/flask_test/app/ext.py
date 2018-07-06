# coding=utf-8
from __future__ import absolute_import

from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_login import LoginManager
from flask_session import Session
from flask_principal import Principal
from flask_babelex import Babel, Domain
from flask_caching import Cache

import os

db = SQLAlchemy()
api = Api()
login_manager = LoginManager()
session = Session()
principal = Principal()

domain = Domain(os.path.join(os.getcwd(), 'translations/'))
babel = Babel(default_domain=domain)

cache = Cache()
