# -*- coding: utf-8 -*-

"""
@File:         test_demo_fixture
@Description:  
@Author:       kenwu
@Date:         2024/3/9
@Email: 370483689@qq.com
"""

import pytest


# 语法规则： @pytest.fixture(scope="作用域",params="参数化",autouse="自动执行",ids="参数别名",name="装饰器别名")
# fixture作用域参数：scope："function" (作用于函数)," class"  (作用于类), "module"  (作用于模块), "session" (作用于会话)


@pytest.fixture(scope="function", name="gujian", autouse=False)
def autotest():
    print("\n autotest =>执行用例前执行固件")
    yield
    print("\n autotest => 执行用例后执行固件")


@pytest.fixture(scope="function", params=["mysql", "redis"])
def login(request):
    """
    测试固件传递参数
    :param request:
    :return:
    """
    print("\n 固件函数前")
    yield request.param  # 通过request 将参数传递出
    print("\n 固件函数后")


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
