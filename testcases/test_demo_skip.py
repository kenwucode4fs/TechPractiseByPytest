# -*- coding: utf-8 -*-

"""
@File:         test_demo_skip
@Description:  
@Author:       kenwu
@Date:         2024/3/9
@Email: 370483689@qq.com
"""
import pytest


class TestDemoSkip:
    """
    测试跳过案例方法
    """
    workage2 = 5
    workage3 = 20

    @pytest.mark.skip(reason="无理由跳过")
    def test_demo1(self):
        print("我被跳过了")

    @pytest.mark.skipif(workage2 < 10, reason="工作经验少于10年跳过")
    def test_demo2(self):
        print("由于经验不足，我被跳过了")

    @pytest.mark.skipif(workage3 < 10, reason="工作经验少于10年跳过")
    def test_demo3(self):
        print("由于经验过关，我被执行了")

    def test_demo4(self):
        print("我没有跳过条件，所以我被执行了")
