# -*- coding: utf-8 -*-

"""
@File:         test_demo_assert
@Description:  
@Author:       kenwu
@Date:         2024/3/9
@Email: 370483689@qq.com
"""
import allure


@allure.epic("项目名称：Pytest最佳实践之Assert")
@allure.feature("模块:Assert")
class TestAssert:
    """
    断言测试。
    """

    @allure.story("接口:base_url校验")
    @allure.title("用例1：base_url校验 用例命名方式1")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("用例描述方式第一种方式：在用例定义上方")
    def test_case_01(self, base_url):
        print("用例1 :{0}".format(base_url))
        assert "www" in base_url

    @allure.story("接口:base_url校验")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_case_02(self, base_url):
        allure.dynamic.title("用例2：base_url校验 用例命名方式2")
        allure.dynamic.description("用例描述第二种方式：在用例内部进行描述")
        print("用例2：{0}".format(base_url))
        assert "wwww" == base_url

    @allure.story("接口:常规接口校验")
    @allure.severity(allure.severity_level.NORMAL)
    def test_case_03(self):
        print("用例3")
