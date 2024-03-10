# # This is a sample Python script.
#
# # Press ⌃F5 to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


import pytest
import time
import os
import allure


# @allure.feature('test_success')
# def test_success():
#     """this test succeeds"""
#     assert True
#
#
# @allure.feature('test_failure')
# def test_failure():
#     """this test fails"""
#     assert False
#
#
# @allure.feature('test_skip')
# def test_skip():
#     """this test is skipped"""
#     pytest.skip('for a reason!')
#
#
# @allure.feature('test_broken')
# def test_broken():
#     raise Exception('oops')


if __name__ == '__main__':
    pytest.main()
    # pytest.main(["-vsm product_manage"])

    time.sleep(10)
    # 通过 os.system 向系统终端输入指令 allure generate 表示生成 html 报告，
    # ./allureTemps 表示用来生成html的JSON临时文件目录
    # ./reports 表示html文件生成目录
    # --clean 表示生成前清空之前的文件
    os.system("allure generate ./allureresults -o ./reports --clean")
    os.system("allure open ./reports")
