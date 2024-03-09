# -*- coding: utf-8 -*-

"""
@File:         test_demo_order
@Description:  
@Author:       kenwu
@Date:         2024/3/9
@Email: 370483689@qq.com
"""

import pytest


class TestApiOrder:
    """
    测试用例执行顺序
    """

    def test_case_01(self):
        print("用例1")

    @pytest.mark.run(order=1)
    def test_case_02(self):
        print("用例2")

    @pytest.mark.run(order=2)
    def test_case_03(self):
        print("用例3")

    @pytest.mark.run(order=-1)
    def test_case_04(self):
        print("用例4")

    @pytest.mark.run(order=-2)
    def test_case_05(self):
        print("用例5")

    @pytest.mark.run(order=-5)
    def test_case_06(self):
        print("用例6")
