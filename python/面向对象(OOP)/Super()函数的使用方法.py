# -*- coding: utf-8 -*-
# @Time    : 2022/8/7 上午9:50
# @Author  : gavin
# @FileName: Super()行数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281#
"""
目的：
    在开发中如果父类中的方法满足不了子类的需求，而又需要保留父类中的方法时，就需要在
子类中对相应的方法进行重写扩展，在需要调用父类中同名的方法时就可以使用super()函数来
实现，super()其实就相当于创建了一个对象。
"""


class AA:

    def __init__(self, name, type):
        self.a = "A类实例化!"
        self.name = name
        self.type = type

    def fun_A(self):
        print("我是你爸爸！")
        print(self.a)


class BB(AA):

    def __init__(self, name, type, date):
        super(BB, self).__init__(name, type)
        self.date = date
        self.b = "B实例化！"

    def fun_A(self):
        super().fun_A()


class A:

    def __init__(self):
        print("A")


class B:

    def __init__(self):
        print("B")


class C(A, B):

    def __init__(self):
        super(C, self).__init__()
        print("C")


class D(B, A):

    def __init__(self):
        super(D, self).__init__()
        print("D")


if __name__ == "__main__":
    # bb = B("小张", "学生", "20220807")
    # bb.fun_A()
    # print(bb.a)
    # super(B, bb).fun_A()
    # print(B.mro())
    print(A.mro())
    print(B.mro())
    print(C.mro())
    print(D.mro())
    print("C实例化")
    c = C()
    print("D实例化")
    d = D()
