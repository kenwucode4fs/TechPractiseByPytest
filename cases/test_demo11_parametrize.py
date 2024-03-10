# -*- coding: utf-8 -*-

"""
@File:         test_demo11_parametrize
@Description:  
@Author:       kenwu
@Date:         2024/3/10
@Email: 370483689@qq.com
"""
import pytest
import allure
from commons.yaml_util import read_yaml

path_1 = "/Users/kenwu/Documents/TechSet/TechPractiseByPytest/files/yaml/yaml_1.yaml"
path_2 = "/Users/kenwu/Documents/TechSet/TechPractiseByPytest/files/yaml/yaml_4.yaml"


@allure.epic("列表序列化数据驱动")
@allure.feature("数据驱动")
class TestYamlTestCase:

    # 用法一：通过列表序列化执行yaml用例
    @allure.story("yaml数据驱动")
    @allure.title("方式一：通过列表序列化执行yaml用例")
    @allure.description("将用例中的组成放在yaml文件中")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("caseinfo", read_yaml(path_1))
    def test_yaml_testcase_1_1(self, caseinfo):
        print("yaml_testcase用例1")
        print(caseinfo)

    # 用法二：通过列表序列化后解压数据执行yaml用例
    @allure.story("yaml数据驱动")
    @allure.title("方式二：通过列表序列化后解压数据执行yaml用例")
    @allure.description("将数据存放yaml文件中")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("age,name", read_yaml(path_2))
    def test_yaml_testcase_2_1(self, age, name):
        print("yaml_testcase用例2")
        print(age, name)

    # 用法二：通过列表序列化后解压数据执行yaml用例
    @allure.story("yaml数据驱动")
    @allure.title("方式二：通过列表序列化后解压数据执行yaml用例")
    @allure.description("将数据存放yaml文件中")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("age,name", [["age", 1], ["name", "味觉"]])
    def test_yaml_testcase_3_1(self, age, name):
        print("yaml_testcase用例3")
        print(age, name)
