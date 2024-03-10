# -*- coding: utf-8 -*-

"""
@File:         paramsetting
@Description:  
@Author:       kenwu
@Date:         2024/3/10
@Email: 370483689@qq.com
"""
from jsonpath import jsonpath


class ParamSetting:
    """
    增加用例请求中的参数处理。如变量替换以及变量依赖等
    """
    access_value = {}

    @classmethod
    def data_is_replace(cls, data):
        """
        请求参数data 和提取参数extract_key
        :param data:
        :return: 返回参数是否需要被替换
        """
        if data is None:
            return False
        for k, v in data.items():
            if '$.' in v:
                return True
        return False

    @classmethod
    def parameter_setting(cls, data: dict, type='get'):
        """
        { "id": $.tq_data.id,"projectNo": "1234309043","name": $.tq_data.name }
        :param data:
        :param type:
        :return:
        """
        if type == 'save':
            for k, v in data.items():
                cls.access_value[k] = v
            print('参数提取完成后的参数池：{}'.format(cls.access_value))

        if type == 'get':
            for k, v in data.items():
                if '$.' in v:
                    if not jsonpath(cls.access_value, v):
                        return {"错误信息": "未读取到参数"}
                    v = jsonpath(cls.access_value, v)[0]
                    data[k] = v
                    print('转换过的参数：{0}-{1}'.format(k, v))
            for k, v in data.items():
                if 'random' in str(v):
                    data[k] = eval(v)
                    print('转换过的参数：{0}-{1}'.format(k, v))

            return data

    @classmethod
    def extract_value(cls, api_response: dict, extract_key: dict):
        """
        'extract_key': {'id': '$.data.id', 'name': '$.data.name'}
        :param api_response:
        :param extract_key:
        :return:
        """
        extract_value = {}
        for k, v in extract_key.items():
            extract_value[k] = jsonpath(api_response, v)[0]
        return extract_value


if __name__ == '__main__':
    # 测试参数存储
    ParamSetting.parameter_setting({'a': 44, 'a1': 144, 'b': 1, 'g': 'wer'}, 'save')
    # 测试参数读取
    ParamSetting.parameter_setting({'a1': '$.a1', 'b': '$.b'})
