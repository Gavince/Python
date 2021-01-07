# -*- coding: utf-8 -*-
# @Time    : 2020/9/11 上午7:41
# @Author  : gavin
# @FileName: 26.判断是否是二叉搜索树的后序遍历序列结果.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281

"""
问题描述：
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,
否则输出No。假设输入的数组的任意两个数字都互不相同。

解决方案：

"""


class Solution:

    def VerifySquenceOfBST(self, squence):
        if len(squence) == 0:
            return False

        root = squence.pop()
        lefttree = []
        righttree = []

        for i in range(len(squence)):
            if squence[i] < root:
                lefttree.append(squence[i])
            else:
                break
        for i in range(len(lefttree), len(squence) - 1):
            if squence[i] <= root:
                return False
            righttree.append(squence[i])

        # 叶子结点
        if len(lefttree) <= 1:
            left = True
        else:
            left = self.VerifySquenceOfBST(lefttree)
        if len(righttree) <= 1:
            right = True
        else:
            right = self.VerifySquenceOfBST(righttree)

        return left and right
