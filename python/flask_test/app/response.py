# coding=utf-8
from __future__ import absolute_import

class BaseResponse(dict):
    code = 1
    message = 'Successful'

    def __init__(self, message=None):
        super(BaseResponse, self).__init__(message=message)

        self.update({
            'code': self.code,
            'message': message or self.message
        })


class MessageResponse(BaseResponse):
    message = 'ok'
