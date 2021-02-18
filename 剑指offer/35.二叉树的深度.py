# -*- coding: utf-8 -*-
# @Time    : 2021/2/15 上午9:16
# @Author  : gavin
# @FileName: 35.二叉树的深度.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径
，最长路径的长度为树的深度。
例如：
给定二叉树 [3,9,20,null,null,15,7]，
深度: 3

解法：
(1)后续遍历DFS
二叉树的深度=max(左子树的深度，右子树的深度) + 1
(2)层序遍历(BFS)
每一层的结点单独进行遍历，并设置计数
"""


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        """后序遍历"""

        if not root: return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth1(self, root: TreeNode) -> int:

        if not root: return None
        queue, res = [root], 0
        while queue:
            tmp = []
            # 每一层单独进行遍历
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
            res += 1
        return res
