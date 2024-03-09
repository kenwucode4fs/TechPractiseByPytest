# -*- coding: utf-8 -*-

"""
@File:         test_demo
@Description:  
@Author:       kenwu
@Date:         2024/3/9
@Email: 370483689@qq.com
"""
import pytest


class TestDemoMark:
    """
    测试Pytest.INI中的MARK分组
    """

    @pytest.mark.user_manage
    def test_demo1(self):
        """
        用户管理测试用例1
        :return:
        """
        print('用户管理测试用例1： user_manage_test1')

    @pytest.mark.product_manage
    def test_demo2(self):
        """
        产品管理测试用例1
        :return:
        """
        print('产品管理测试用例1：producet_manage_test1')

    @pytest.mark.user_manage
    @pytest.mark.product_manage
    def test_demo3(self):
        """
        管理测试用例
        :return:
        """
        print('管理测试用例：manage_test1')
