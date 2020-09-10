# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 上午7:39
# @Author  : gavin
# @FileName: 22.重建二叉树.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和
中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和
中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

解决方案:
递归
"""

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def reConstructBinaryTree(self, pre, tin):
        """
        :param pre: 前序遍历结果
        :param tin: 中序遍历结果
        :return:
        """

        if not pre or not tin:
            return None
        if len(pre) is not len(tin):
            return None

        # 根节点为前序遍历的第一个值
        val = pre[0]
        root = TreeNode(val)
        pos = tin.index(val)
        tin_left = tin[:pos]
        tin_right = tin[pos + 1:]

        pre_left = pre[1:pos + 1]
        pre_right = pre[pos + 1:]

        # 递归遍历
        left_node = self.reConstructBinaryTree(pre_left, tin_left)
        right_node = self.reConstructBinaryTree(pre_right, tin_right)
        root.left = left_node
        root.right = right_node

        return root

    def reConstructBinaryTree1(self, pre, tin):

        if len(pre) == 0:
            return None
        else:
            pos = tin.index(pre[0])

        root = TreeNode(pre[0])
        root.left = self.reConstructBinaryTree1(pre[1:pos+1], tin[:pos])
        root.right = self.reConstructBinaryTree1(pre[pos+1:], tin[pos+1:])

        return root


if __name__ == "__main__":
    obj = Solution()
    array_pre = [1, 2, 4, 7, 3, 5, 6, 8]
    array_tin = [4, 7, 2, 1, 5, 3, 8, 6]
    root = obj.reConstructBinaryTree(array_pre, array_tin)
