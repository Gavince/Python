# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 下午4:24
# @Author  : gavin
# @FileName: 非递归二叉树遍历.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


class Node:
    """定义二叉树节点"""

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    """实现二叉树"""

    def __init__(self):
        self.root = None

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
            if tmp_node.left is None:
                tmp_node.left = node
                return
            else:
                queue.append(tmp_node.left)
            #  右子树
            if tmp_node.right is None:
                tmp_node.right = node
                return
            else:
                queue.append(tmp_node.right)

    def bre_order(self):
        """层序遍历"""
        if self.root is None:
            return None

        queue = [self.root]
        while queue:
            tmp_node = queue.pop(0)
            print(tmp_node.val, end=" ")
            if tmp_node.left is not None:
                queue.append(tmp_node.left)
            if tmp_node.right is not None:
                queue.append(tmp_node.right)

    def in_order(self):
        """中序遍历"""
        if self.root is None:
            return None

        stack = []  # 使用栈保存数据
        tmp_node = self.root
        while tmp_node or stack:
            while tmp_node:  # 进栈
                stack.append(tmp_node)
                tmp_node = tmp_node.left

            #  出栈
            node = stack.pop()
            print(node.val, end=" ")
            tmp_node = node.right

    def pre_order(self):
        """前序遍历"""
        if self.root is None:
            return None

        stack = []  # 使用栈保存数据
        tmp_node = self.root
        while tmp_node or stack:
            while tmp_node:  # 进栈
                print(tmp_node.val, end=" ")
                stack.append(tmp_node)
                tmp_node = tmp_node.left

            #  出栈
            node = stack.pop()
            tmp_node = node.right

    def post_order(self):
        """后序遍历"""
        if self.root is None:
            return None

        stack = []
        tmp_node = self.root
        while tmp_node or stack:
            while tmp_node:
                stack.append(tmp_node)
                tmp_node = tmp_node.left

            #  后序遍历的输出
            node = stack[-1]  # 预先抛出节点，检测所有右端节点是否已经存入
            tmp_node = node.right
            if tmp_node is None:  #
                node = stack.pop()
                print(node.val, end=" ")
                while stack and node == stack[-1].right:  # 输出左右结点之后，输出其根节点
                    node = stack.pop()
                    print(node.val, end=" ")


if __name__ == "__main__":
    tree = Tree()
    for i in range(1, 9):
        tree.add(i)
    print("层序遍历：", end=" ")
    tree.bre_order()
    print("\n前序遍历：", end="")
    tree.pre_order()
    print("\n中序遍历：", end=" ")
    tree.in_order()
    print("\n后序遍历：", end=" ")
    tree.post_order()
