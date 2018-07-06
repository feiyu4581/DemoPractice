# coding=utf-8
from __future__ import absolute_import

from app.tranlation import _

class BaseResponse(dict):
    code = 0
    message = 'Successful'

    def __init__(self, message=None):
        super(BaseResponse, self).__init__(message=message)

        self.update({
            'code': self.code,
            'message': message or _(self.message)
        })


class MessageResponse(BaseResponse):
    message = 'ok'
