# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 上午9:18
# @Author  : gavin
# @FileName: 31.对称二叉树.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的
    1
  2   2
3  4 4  3
"""


class Solution:
    
    def isSymmetric(self, root):

        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return recur(root.left, root.right) if root else True
