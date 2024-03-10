# -*- coding: utf-8 -*-

"""
@File:         request
@Description:  
@Author:       kenwu
@Date:         2024/3/10
@Email: 370483689@qq.com
"""
import json
import requests
from commons import request_env_info
from config.config import Environment


class Request:
    @classmethod
    def get(cls, url):
        """

        :param url:
        :return:
        """
        url = request_env_info(Environment)['ip'] + url
        headers = request_env_info(Environment)['headers']
        result = requests.get(url=url, headers=headers)
        return result

    @classmethod
    def post(cls, url, data):
        """

        :param url:
        :param data:
        :return:
        """
        url = request_env_info(Environment)['ip'] + url
        headers = request_env_info(Environment)['headers']
        result = requests.post(url=url, headers=headers, data=json.dumps(data))
        return result


if __name__ == '__main__':
    Request.get('/regist/user/')
    Request.post('/do/regist/', {'data': 'd123412'})
