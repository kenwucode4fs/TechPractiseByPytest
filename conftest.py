# -*- coding: utf-8 -*-

"""
@File:         conftest
@Description:  
@Author:       kenwu
@Date:         2024/3/9
@Email: 370483689@qq.com
"""
import pytest


# 语法规则： @pytest.fixture(scope="作用域",params="参数化",autouse="自动执行",ids="参数别名",name="装饰器别名")
# fixture作用域参数：scope："function" (作用于函数)," class"  (作用于类), "module"  (作用于模块), "session" (作用于会话)
# 首先我们需要知道conftest.py文件的名字是固定形式，不可改变
# conftest.py文件主要就是用来存储我们的Fixture，然后我们会根据该文件的不同位置来判断可以使用的方法
# conftest可以在不同的目录级别下创建，如果我们在根目录下创建，那么所有case都会使用到该Fixture
# 但是如果我们在testcases文件夹下的某个模块文件下创建conftest.py，那么它的作用范围就只包含在该目录下


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