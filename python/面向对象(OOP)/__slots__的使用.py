# -*- coding: utf-8 -*-
# @Time    : 2022/8/15 上午8:19
# @Author  : gavin
# @FileName: __slots__的使用.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
    使用 slots 类属性限制实例属性的添加。只允许实例属性具有__slots__指定的属性，在试图为实例添加其
它属性时将报错。注： slots 类属性可以是列表，可以是元组。
"""


class Student:
    """__slot__的使用"""
    __slots__ = ["name", "age", "score"]

    def __init__(self, name, score):
        self.name = name
        self.score = score


if __name__ == "__main__":
    amy = Student("hh", 5)
    amy.age = 31
    print(amy.name, amy.score, amy.age)
    print(amy.__doc__)
