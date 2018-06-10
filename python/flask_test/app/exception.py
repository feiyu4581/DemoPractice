# coding=utf-8
from __future__ import absolute_import


class BaseException(Exception):
    status_code = 200
    code = -1
    message = 'Error Code'
    kwargs = {}

    def __init__(self, message=None, **kwargs):
        super(BaseException, self).__init__()

        self.kwargs = kwargs
        if message:
            self.message = message

    def to_dict(self):
        res = {
            'code': self.code,
            'message': self.message
        }

        res.update(self.kwargs)
        return res


class SessionExpired(BaseException):
    message = 'Session Expired'


class LoginError(BaseException):
    message = 'Wrong Login/Password'


class MessageException(BaseException):
    pass
