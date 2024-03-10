# -*- coding: utf-8 -*-

"""
@File:         yaml_util
@Description:  
@Author:       kenwu
@Date:         2024/3/10
@Email: 370483689@qq.com
"""
import yaml


def read_yaml(yaml_path):
    """
    读取yaml文件
    :param yaml_path:
    :return:
    """
    with open(yaml_path, encoding="utf-8") as f:
        value = yaml.safe_load(f)
        return value


def append_yaml(yaml_path, data):
    """
    yaml文件追加写入
    :param yaml_path:
    :param data:
    :return:
    """
    with open(yaml_path, encoding="utf-8", mode="a+") as f:
        yaml.safe_dump(data, stream=f, allow_unicode=True)


def write_yaml(yaml_path, data):
    """
    yaml文件覆盖写入
    :param yaml_path:
    :param data:
    :return:
    """
    with open(yaml_path, encoding="utf-8", mode="w") as f:
        yaml.safe_dump(data, stream=f, allow_unicode=True)


def clear_yaml(yaml_path):
    """
    清空yaml
    :param yaml_path:
    :return:
    """
    with open(yaml_path, encoding="utf-8", mode="w") as f:
        f.truncate()
