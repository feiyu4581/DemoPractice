# coding=utf-8
from __future__ import absolute_import

from flask_principal import Permission, RoleNeed

admin_permission = Permission(RoleNeed('admin'))
normal_permission = Permission(RoleNeed('normal'))
