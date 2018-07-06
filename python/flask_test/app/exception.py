# coding=utf-8
from __future__ import absolute_import

from app.tranlation import _

class BaseException(Exception):
    status_code = 200
    code = -1
    _message = lambda self: _('Error Code')
    kwargs = {}
    
    @property
    def message(self):
        if callable(self._message):
            return self._message()

        return self._message

    def __init__(self, message=None, **kwargs):
        super(BaseException, self).__init__()

        self.kwargs = kwargs
        if message:
            self._message = message

    def to_dict(self):
        res = {
            'code': self.code,
            'message': self.message
        }

        res.update(self.kwargs)
        return res


class SessionExpired(BaseException):
    _message = lambda self: _('Session Expired')


class LoginError(BaseException):
    _message = lambda self: _('Wrong Login/Password')


class MessageException(BaseException):
    pass
