# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 下午4:25
# @Author  : gavin
# @FileName: 递归二叉树遍历.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281

"""
二叉树是一种非常重要的数据结构，很多其它数据结构都是基于二叉树的基础演变而来的。
对于二叉树，有深度遍历和广度遍历，深度遍历有前序、中序以及后序三种遍历方法，广
度遍历即我们平常所说的层次遍历。因为树的定义本身就是递归定义，因此采用递归的方
法去实现树的三种遍历不仅容易理解而且代码很简洁，
"""


class Node:
    """结点"""

    def __init__(self, val, left_child=None, right_child=None):
        self.val = val
        self.left_child = left_child
        self.right_child = right_child


class Tree:
    """构建二叉树"""

    def __init__(self, root=None):
        self.root = root

    def add(self, val):
        """添加树节点实现完全二叉树"""
        node = Node(val)

        if self.root is None:
            self.root = node
            return

        #  使用队列来实现节点存储
        queue = [self.root]
        while queue:
            tmp_node = queue.pop(0)  # 先进先出
            #  左子树
            if tmp_node.left_child is None:
                tmp_node.left_child = node
                return
            else:
                queue.append(tmp_node.left_child)
            #  右子树
            if tmp_node.right_child is None:
                tmp_node.right_child = node
                return
            else:
                queue.append(tmp_node.right_child)

    ## 递归实现三种遍历
    def pre_order(self, node):
        """前序遍历"""
        if node is None:
            return
        print(node.val, end=" ")
        self.pre_order(node.left_child)
        self.pre_order(node.right_child)

    def in_order(self, node):
        """中序遍历"""
        if node is None:
            return
        self.in_order(node.left_child)
        print(node.val, end=" ")
        self.in_order(node.right_child)

    def post_order(self, node):
        """后序遍历"""
        if node is None:
            return
        self.post_order(node.left_child)
        self.post_order(node.right_child)
        print(node.val, end=" ")

    def bre_order(self):
        """层序遍历"""
        if self.root is None:
            return None

        queue = [self.root]
        while queue:
            tmp_node = queue.pop(0)
            print(tmp_node.val, end=" ")
            if tmp_node.left_child is not None:
                queue.append(tmp_node.left_child)
            if tmp_node.right_child is not None:
                queue.append(tmp_node.right_child)


if __name__ == "__main__":
    tree = Tree()
    for i in range(1, 9):
        tree.add(i)
    print("层序遍历：", end=" ")
    tree.bre_order()
    print("\n前序遍历：", end="")
    tree.pre_order(tree.root)
    print("\n中序遍历：", end=" ")
    tree.in_order(tree.root)
    print("\n后序遍历：", end=" ")
    tree.post_order(tree.root)
