# -*- coding: utf-8 -*-

"""
@File:         test_demo9_web_testcaseattach
@Description:  
@Author:       kenwu
@Date:         2024/3/10
@Email: 370483689@qq.com
"""

import allure


@allure.epic("项目名称：京东登陆")
@allure.feature("模块：京东登陆功能")
class TestCaseAttach:
    """
    测试用例附件上传
    """
    @allure.story("接口：登陆")
    @allure.title("京东登陆用例1-登陆成功-正确的用户名及密码")
    @allure.description("通过输入正确的用户名及密码、验证码， 点击登陆按钮成功")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.link(url="https://passport.jd.com/new/login.aspx",name="京东登陆页面")
    def test_case_1_1(self):
        print("京东登陆用例1")
        with allure.step("第一步： 打开登陆页面"):
            with open(r"/Users/kenwu/Documents/TechSet/TechPractiseByPytest/pics_cases_results/jd_login/loginpage.png", mode="rb") as f:
                content = f.read()
                allure.attach(body=content, name="京东登陆页面截图", attachment_type=allure.attachment_type.PNG)

        with allure.step("第二步：输入用户名"):
            pass
        with allure.step("第三步：输入密码"):
            pass

    def test_case2_2(self, base_url):
        print(" case2 用例2")

    def test_case2_3(self):
        print(" case2 用例3")