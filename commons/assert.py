# -*- coding: utf-8 -*-

"""
@File:         assert
@Description:  
@Author:       kenwu
@Date:         2024/3/10
@Email: 370483689@qq.com
"""
from jsonpath import jsonpath


class Assert:
    """
    自定义断言
    """

    @classmethod
    def assert_response(cls, assert_list: list, api_response: dict):
        """

        :param assert_list: 断言规则
        :param api_respinse: 接口返回值
        :return:
        """
        new_assert_list = []
        for i in assert_list:
            print(i)
            # 定义判断标志的位置
            compare_position = None
            compare_valuelist = []
            assert_contion = ''
            # 断言规则：相等== 、包含 in 、不等于!=、不包含!in
            # if '@==@' in i:
            #     compare_position = i.find('@==@')
            #     assert_contion = "=="
            #     assert_str = i.split('@==@')
            # elif '@in@' in i:
            #     compare_position = i.find('@in@')
            #     assert_contion = "in"
            #     assert_str = i.split('@in@')
            # elif '@!=@' in i:
            #     compare_position = i.find('@!=@')
            #     assert_contion = "!="
            #     assert_str = i.split('@!=@')
            # elif '@!in@' in i:
            #     compare_position = i.find('@!in@')
            #     assert_contion = "!in"
            #     assert_str = i.split('@!in@')


if __name__ == '__main__':
    a = {
        'assert_expression': [{'eq': [1, 'select title from case_test where i=1']}, {'eq': ['cc', 'dad']},
                              {'in': [12, '123']}, {'nin': ['$.lpl.ig', '123']}, {'ne': ['$.lpl.ig', '123']},
                              {'in': ['ig', '$.lpl.ig']}, {'eq': ['a', '$.dad']},
                              {'eq': ['$.lpl.ig', 'select title from case_test where i=1']},
                              {'eq': ['$.lpl.ig', '$.dad']},
                              {'eq': ['select title from case_test where i=1',
                                      'select title from case_test where i=2']}]}
