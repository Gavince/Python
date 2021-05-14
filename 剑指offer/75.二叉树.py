# -*- coding: utf-8 -*-
# @Time    : 2021/5/14 上午9:36
# @Author  : gavin
# @FileName: 75.二叉树.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：

给你二叉树的根结点 root ，请你将它展开为一个单链表：
展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链
表中下一个结点，而左子指针始终为 null 。展开后的单链表应该与二叉
树 先序遍历 顺序相同。
"""


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def flatten(self, root: TreeNode) -> None:
        
        preorderlist = list()

        def pre_order(root):
            if root:
                preorderlist.append(root)
                pre_order(root.left)
                pre_order(root.right)

        #
        pre_order(root)
        for i in range(1, len(preorderlist)):
            pre, cur = preorderlist[i - 1], preorderlist[i]
            pre.left = None
            pre.right = cur
