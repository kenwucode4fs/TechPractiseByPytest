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
from commons.paramsetting import *


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

    @classmethod
    def read_case(cls, path):
        """
        一个用例文件的读取生成器
        :param path:
        :return:
        """
        case_data = cls.read_yaml(path)
        for k, v in case_data.items():
            case_name = k
            if v['is_run']:
                v['case_name'] = case_name
                if ParamSetting.data_is_replace(v['data']):
                    v['data'] = ParamSetting.parameter_setting(v['data'])
                yield v


if __name__ == '__main__':
    print(ReadFile.project_dir)
    print(ReadFile.read_yaml("files/yaml/yaml_1.yaml"))
    case_list = ReadFile.read_case("cases/test.yaml")
    for i in case_list:
        print(i)
