# -*- coding: utf-8 -*-

"""
@File:         read_file
@Description:  
@Author:       kenwu
@Date:         2024/3/10
@Email: 370483689@qq.com
"""

from pathlib import Path
import yaml


class ReadFile:
    """
    读取文件类
    """
    project_dir = str(Path(__file__).parent.parent) + "/"

    @classmethod
    def read_yaml(cls, path):
        """
        读取yaml文件
        :param path:
        :return:
        """
        path = cls.project_dir + path
        with open(path, 'r', encoding="utf-8") as f:
            content = yaml.safe_load(f)
            return content


if __name__ == '__main__':
    print(ReadFile.project_dir)
    print(ReadFile.read_yaml("files/yaml/yaml_1.yaml"))
