#!/usr/bin/python
# -*-encoding=utf8 -*-
# @Author         : imooc
# @Email          : imooc@foxmail.com
# @Created at     : 2018/11/30
# @Filename       : response.py
# @Desc           :
# -*- coding: utf-8 -*-
import urllib
import urllib.request as request
import urllib.error as error
import json

# 状态码
class ReturnCode:
    RESOURCES_NOT_EXISTS = None
    SUCCESS = 0
    RESOURCES_NOT_FOUND = -102
    FAILED = -100
    UNAUTHORIZED = -500
    BROKEN_AUTHORIZED_DATA = -501
    WRONG_PARMAS = -101


    @classmethod
    def message(cls, code):
        if code == cls.SUCCESS:
            return 'success'
        elif code == cls.FAILED:
            return 'failed'
        elif code == cls.UNAUTHORIZED:
            return 'unauthorized'
        elif code == cls.WRONG_PARMAS:
            return 'wrong params'
        elif code == cls.RESOURCES_NOT_FOUND:
            return 'resources not found'
        else:
            return ''


def wrap_json_response(data=None, code=None, message=None):
    response = {}
    if not code:
        code = ReturnCode.SUCCESS
    if not message:
        message = ReturnCode.message(code)
    if data:
        response['data'] = data
        response['result_code'] = code
        response['message'] = message
    return response

class CommonResponseMixin(object):
    @classmethod
    def wrap_json_response(data=None, code=None, message=None):
        response = {}
        if not code:
            code = ReturnCode.SUCCESS
        if not message:
            message = ReturnCode.message(code)
        if data:
            response['data'] = data
            response['result_code'] = code
            response['message'] = message
        return response
