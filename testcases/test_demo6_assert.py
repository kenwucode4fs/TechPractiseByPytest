# -*- coding: utf-8 -*-

"""
@File:         test_demo_assert
@Description:  
@Author:       kenwu
@Date:         2024/3/9
@Email: 370483689@qq.com
"""


class TestAssert:
    """
    断言测试。
    """

    def test_case_01(self, base_url):
        print("用例1 :{0}".format(base_url))
        assert "www" in base_url

    def test_case_02(self, base_url):
        print("用例2：{0}".format(base_url))
        assert "wwww" == base_url

    def test_case_03(self):
        print("用例3")
