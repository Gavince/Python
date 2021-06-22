# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 下午4:58
# @Author  : gavin
# @FileName: 108. 把二叉树搜索树装换为累加树.py.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（
Greater Sum Tree），使每个节点 node的新值等于原树中大于或等于node.val
的值之和。

解题方法：
二叉搜索树中序遍历
时间复杂度：O(n)
空间复杂度：O(n)
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.num = 0

    def convertBST(self, root):
        def dfs(root):
            if root is None:
                return None

            dfs(root.left)
            root.val += self.num
            self.num = root.val
            dfs(root.right)
            return root

        return dfs(root)
