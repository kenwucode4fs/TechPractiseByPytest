# -*- coding: utf-8 -*-

"""
@File:         test_demo7_link
@Description:  
@Author:       kenwu
@Date:         2024/3/10
@Email: 370483689@qq.com
"""

import allure


@allure.epic("项目名称：Allure链接相关测试")
@allure.feature("模块：链接")
class TestLink:
    """
    demo测试link跳转：接口访问链接、BUG链接、测试用例链接
    """

    @allure.link(url="https://www.baidu.com/", name="百度首页链接")
    @allure.issue(url="https://cn.bing.com/", name="BUG链接")
    @allure.testcase(url="https://cn.bing.com/", name="测试用例链接")
    @allure.story("接口：链接跳转")
    @allure.title("测试用例1：链接相关应用正确")
    @allure.description("通过测试用例1 测试allure的link、issue、testcase相关跳转")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_case_1_1(self):
        print("case test interface link")

    def test_case_1_2(self, base_url):
        print("case 2")
