# -*- coding: utf-8 -*-

"""
@File:         test_demo8_web_step
@Description:  
@Author:       kenwu
@Date:         2024/3/10
@Email: 370483689@qq.com
"""
import allure


@allure.epic("项目名称：Allure Web测试用例步骤")
@allure.feature("模块：Web测试用例步骤")
class TestWebStep:
    """
    WEB测试中的测试用例步骤实践
    """

    @allure.story("接口：登陆接口的步骤")
    @allure.title("用例1_1：登陆接口的测试步骤")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("WEB登陆页面的测试：测试正常登陆")
    @allure.link(url="http://www.baidu.com/", name="百度登陆页面")
    def test_case_1_1(self):
        """
        测试用例步骤正确性
        :return:
        """
        print("case1_1: 测试百度登陆页面")
        with allure.step("第一步"):
            print("这是测试用例的第一步")
        with allure.step("第二步"):
            print("这是测试用例的第二步")

    def test_case2_2(self, base_url):
        print(" case2 用例2")

    def test_case2_3(self):
        print(" case2 用例3")
