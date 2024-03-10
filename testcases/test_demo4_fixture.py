# -*- coding: utf-8 -*-

"""
@File:         test_demo_fixture
@Description:  
@Author:       kenwu
@Date:         2024/3/9
@Email: 370483689@qq.com
"""


class TestApiFixture:
    """
    测试使用固件
    """

    def test_case_01(self, gujian):
        """
        使用固件的时候需要改为固件的别名，
        :param gujian:
        :return:
        """
        print("测试固件使用用例1 :test_case_01")

    def test_case_02(self):
        """
        测试使用固件，不用固件
        :return:
        """
        print("测试使用固件用例2不用固件：test_case_02")

    def test_case_03(self, login):
        print(login)
        print("test_case_03")
