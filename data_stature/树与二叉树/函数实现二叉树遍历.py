# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 下午4:26
# @Author  : gavin
# @FileName: 函数实现二叉树遍历.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281

class Node:
    """
    二叉树节点
    """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def in_order(root):
    """中序遍历"""
    if root is None:
        return None

    stack = []  # 使用栈保存数据
    tmp_node = root
    while tmp_node or stack:
        while tmp_node:  # 进栈
            stack.append(tmp_node)
            tmp_node = tmp_node.left

        #  出栈
        node = stack.pop()
        print(node.val, end=" ")
        tmp_node = node.right


def pre_order(root):
    """前序遍历"""
    if root is None:
        return None

    stack = []  # 使用栈保存数据
    tmp_node = root
    while tmp_node or stack:
        while tmp_node:  # 进栈
            print(tmp_node.val, end=" ")
            stack.append(tmp_node)
            tmp_node = tmp_node.left

        #  出栈
        node = stack.pop()
        tmp_node = node.right


def post_order(root):
    """后序遍历"""
    if root is None:
        return None

    stack = []
    tmp_node = root
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
                # print("父节点：%d\n"%node.val, end=" ")


if __name__ == "__main__":
    t1 = Node(1)
    t2 = Node(2)
    t3 = Node(3)
    t4 = Node(4)
    t5 = Node(5)
    t6 = Node(6)
    t7 = Node(7)
    t8 = Node(8)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    t6.right = t8
    print("先序遍历：")
    pre_order(t1)
    print("\n中序遍历：")
    in_order(t1)
    print("\n后序遍历：")
    post_order(t1)



