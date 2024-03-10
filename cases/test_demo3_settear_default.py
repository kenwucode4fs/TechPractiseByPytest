# -*- coding: utf-8 -*-

"""
@File:         test_demo_settear_default
@Description:  
@Author:       kenwu
@Date:         2024/3/9
@Email: 370483689@qq.com
"""
import allure


@allure.epic("项目名称：Pytest最佳实践之默认SetupTeardown")
@allure.feature("模块:SetupTeardown")
class TestApiByDefault:
    """
    使用默认的前置后置函数
    """

    def setup_method(self):
        print("\n setup_method => 每个方法《用例》前的操作")

    def teardown_method(self):
        print("\n teardown_method => 每个方法《用例》执行完后的操作")

    def setup_class(self):
        print("\n setup_class => 每个类前的操作")

    def teardown_class(self):
        print("\n teardown_class => 每个类后的操作")

    def test_case_2(self):
        print("\n 使用默认的前置后置函数： test_case_2")
