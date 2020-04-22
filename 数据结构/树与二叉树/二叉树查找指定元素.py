# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 上午11:50
# @Author  : gavin
# @FileName: 二叉树查找指定元素.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


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

    def bre_search(self, val):
        """查找指定数据的父亲结点"""
        print("层序！！！")
        if self.root.val == val:  # 根节点无父亲节点
            return self.root

        # 层序遍历，寻找节点
        queue = [self.root]

        while queue:
            tmp_node = queue.pop(0)
            print("层序！！！")
            if tmp_node.left_child and tmp_node.left_child.val == val:
                return tmp_node.left_child
            print("层序！！！")
            if tmp_node.right_child and tmp_node.right_child.val == val:
                return tmp_node.right_child

            #  往下一层进行寻找
            if tmp_node.left_child:
                queue.append(tmp_node.left_child)
            if tmp_node.right_child:
                queue.append(tmp_node.right_child)

        return None

    def pre_search(self, node, val):
        """先序遍历"""

        if node is None:
            return
        print("前序！！！")
        if node.val == val:
            return node
        left_part = self.pre_search(node.left_child, val)
        if left_part:
            return left_part
        right_part = self.pre_search(node.right_child, val)
        if right_part:
            return right_part

        return None

    def in_search(self, node, val):
        """中序查找"""
        if node is None:
            return

        left_part = self.in_search(node.left_child, val)
        if left_part:
            return left_part
        print("中序！！！")
        if node.val == val:
            return node
        right_part = self.in_search(node.right_child, val)
        if right_part:
            return right_part

        return None

    def post_search(self, node, val):
        """后序查找"""
        if node is None:
            return

        left_part = self.post_search(node.left_child, val)
        if left_part:
            return left_part
        right_part = self.post_search(node.right_child, val)
        if right_part:
            return right_part
        print("后序！！！")
        if node.val == val:
            return node

        return None


if __name__ == "__main__":
    tree = Tree()
    for i in range(10):
        tree.add(i)

    # 查询某元素的父亲节点
    print(tree.bre_search(4).val)
    print(tree.pre_search(tree.root, 4).val)
    print(tree.in_search(tree.root, 4).val)
    print(tree.post_search(tree.root, 4).val)