# coding=utf-8
from __future__ import absolute_import

# Flask
DEBUG = False

# Database
SQLALCHEMY_DATABASE_URI = 'postgresql://zhengxiang@127.0.0.1:5432/dl'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = False

# Session
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = False  # TODO 当值为 True 的时候，postman 不会存储cookie了
SESSION_TYPE = 'redis'
SESSION_PERMANENT = True
SESSION_REDIS_HOST = 'localhost'
SESSION_REDIS_PORT = 6379

# Cache
CACHE_TYPE = 'redis'
CACHE_KEY_PREFIX = 'redis-cache:'
CACHE_REDIS_url = 'redis://localhost:6379'
CACHE_DEFAULT_TIMEOUT = 5 * 60
