# -*- coding: utf-8 -*-

"""
@File:         test_demo10_yaml
@Description:  
@Author:       kenwu
@Date:         2024/3/10
@Email: 370483689@qq.com
"""
import allure
from commons.yaml_util import read_yaml, write_yaml, append_yaml, clear_yaml

path_1 = "/Users/kenwu/Documents/TechSet/TechPractiseByPytest/files/yaml/yaml_1.yaml"
path_2 = "/Users/kenwu/Documents/TechSet/TechPractiseByPytest/files/yaml/yaml_2.yaml"
path_3 = "/Users/kenwu/Documents/TechSet/TechPractiseByPytest/files/yaml/yaml_3.yaml"

@allure.epic("项目名称：yaml相关的功能")
@allure.feature("模块：yaml的读写")
class TestYaml:
    """
    测试yaml相关的方法
    """

    @allure.story("yaml的读功能")
    @allure.title("用例1_1：yaml文件读方法成功")
    @allure.description("测试common.yaml_util中yaml读方法正确")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_case_1_1(self):
        """

        :return:
        """
        print("yaml_1用例1：测试读yaml文件成功")
        yaml_datas = read_yaml(path_1)
        print(yaml_datas)
        allure.attach(str(yaml_datas), name="读出的结果")

    @allure.story("yaml的写功能")
    @allure.title("用例2_1：yaml文件覆盖写成功")
    @allure.description("测试common.yaml_util中yaml覆盖写方法正确")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_case_2_1(self):
        """

        :return:
        """
        yaml_datas = {"name1": "味觉1"}
        write_yaml(path_2,yaml_datas)
        print("yaml_2用例1：测试yaml文件覆盖写成功")
        allure.attach(str(yaml_datas), name="写入的结果")

    @allure.story("yaml的写功能")
    @allure.title("用例3_1：yaml文件追加写成功")
    @allure.description("测试common.yaml_util中yaml追加写方法正确")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_case_3_1(self):
        """

        :return:
        """
        yaml_datas = {"name2": "味觉2"}
        append_yaml(path_2,yaml_datas)
        print("yaml_3用例1：测试yaml文件追加写成功")
        allure.attach(str(yaml_datas), name="写入的结果")

    @allure.story("yaml的清空功能")
    @allure.title("用例4_1：yaml文件清空成功")
    @allure.description("测试common.yaml_util中yaml清空方法正确")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_case_4_1(self):
        """

        :return:
        """
        clear_yaml(path_3)
        print("yaml_4用例1：测试yaml文件清空成功")
