# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 下午9:11
# @Author  : gavin
# @FileName: 86.合并二叉树.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节
点合并后的新值，否则不为NULL的节点将直接作为新二叉树的节点。

解题方法：
两棵二叉树同时先序遍历
时间复杂度：O(min(m, n))
空间复杂度：O(min(m, n))

注意：
需要建立新一个二叉树来存储合并后的结果
"""


class TreeNode:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Solution:

    def mergeTrees(self, t1, t2):
        """合并两个二叉树"""

        def dfs(t1, t2):
            if not (t1 and t2):
                return t1 if t1 else t2
            # 合并节点
            merge = TreeNode(t1.val + t2.val)
            merge.left = dfs(t1.left, t2.left)
            merge.right = dfs(t1.right, t2.right)

            return merge

        return dfs(t1, t2)
