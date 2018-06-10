# coding=utf-8
from __future__ import absolute_import

from app import create_app
from app.ext import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# import unittest
import os


app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)


@manager.command
def create_all():
    db.create_all()


@manager.command
def runserver():
    app.secret_key = os.urandom(24)
    app.run()


manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
