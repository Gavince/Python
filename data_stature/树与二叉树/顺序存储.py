# -*- coding: utf-8 -*-
# @Time    : 2020/4/28 上午9:26
# @Author  : gavin
# @FileName: 顺序存储.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
顺序存储：
１）顺序存储只考虑完全二叉树(结点索引以零开头)
２）第ｎ个元素的左子节点２*n + 1
３）第ｎ个元素的右子节点２*n + 2
４）第n个元素的父结点（n-1）/2
"""


class ArrayBinaryTree:

    def __init__(self, array):
        self.array = array

    def pre_order(self, index):
        if self.array is None or len(self.array) == 0:
            print("空数组")
        print(self.array[index], end=" ")

        if (2*index + 1) < len(self.array):
            self.pre_order(2*index + 1)
        if (2*index + 2) < len(self.array):
            self.pre_order(2*index + 2)

    def in_order(self, index):
        if self.array is None or len(self.array) == 0:
            print("空数组")

        if (2*index + 1) < len(self.array):
            self.pre_order(2*index + 1)
        print(self.array[index], end=" ")

        if (2*index + 2) < len(self.array):
            self.pre_order(2*index + 2)

    def post_order(self, index):
        if self.array is None or len(self.array) == 0:
            print("空数组")

        if (2*index + 1) < len(self.array):
            self.pre_order(2*index + 1)
        if (2*index + 2) < len(self.array):
            self.pre_order(2*index + 2)

        print(self.array[index], end=" ")


if __name__ == "__main__":
    atree = ArrayBinaryTree([1, 2, 3, 5, 7, 8])
    atree.pre_order(0)
    print()
    atree.in_order(0)
    print()
    atree.post_order(0)
























