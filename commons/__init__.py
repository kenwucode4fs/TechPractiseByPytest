# -*- coding: utf-8 -*-

"""
@File:         __init__.py
@Description:  
@Author:       kenwu
@Date:         2024/3/10
@Email: 370483689@qq.com
"""
from commons.read_file import ReadFile


def request_env_info(env="SIT"):
    """
    增加一个读取环境信息的方法
    :param env: SIT、UAT、PRE、PRD， 默认SIT
    :return:
    """
    env_info = ReadFile.read_yaml("config/environment.yaml")
    # 定义请求信息
    request_info = ''
    if env == "SIT":
        request_info = env_info['SIT']
    if env == "UAT":
        request_info = env_info['UAT']
    if env == "PRE":
        request_info = env_info['PRE']
    return {'ip': request_info['http'] + str(request_info['ip']) + ':' + str(request_info['port']),
            'headers': request_info['headers']}
