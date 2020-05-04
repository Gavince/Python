# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 下午2:18
# @Author  : gavin
# @FileName: 线索二叉树.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.ltag = 0  # 0表示指向左子树，１表示指向其前驱结点
        self.rtag = 0  # 0表示指向右子树，１表示指向其后继结点


class ThreadedBinaryTree:

    def __init__(self):
        self.root = None
        self.pre = None

    def add(self, val):
        """增加结点"""
        node = TreeNode(val)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            tmp_node = queue.pop(0)
            if tmp_node.left is None:
                tmp_node.left = node
                return
            else:
                queue.append(tmp_node.left)

            if tmp_node.right is None:
                tmp_node.right = node
                return
            else:
                queue.append(tmp_node.right)

    def in_order(self, node):
        """中序遍历"""
        if node is None:
            return
        self.in_order(node.left)
        print(node.val, end=" ")
        self.in_order(node.right)

    @staticmethod
    def thread_in_order(node):
        """中序遍历线索二叉树"""

        if node is None:
            return
        temp_node = node
        while temp_node:
            # 找到出事的线索起点
            while temp_node.ltag == 0:
                temp_node = temp_node.left

            print(temp_node.val, end=" ")

            while temp_node.rtag == 1:
                temp_node = temp_node.right
                print(temp_node.val, end=" ")
            temp_node = temp_node.right

    def threaded_node(self, node):
        """中序线索结点"""
        if node is None:
            return

        self.threaded_node(node.left)

        # 线索左结点,并且线索化
        if node.left is None:
            node.left = self.pre
            node.ltag = 1
        if self.pre and self.pre.right is None:
            self.pre.right = node
            self.pre.rtag = 1
        self.pre = node  # 结点处理完成之后，保证当前结点为下一个结点的前驱结点

        self.threaded_node(node.right)


if __name__ == "__main__":
    tr = ThreadedBinaryTree()
    # for i in range(10):
    #     tr.add(i)

    t1 = TreeNode(1)
    t2 = TreeNode(3)
    t3 = TreeNode(6)
    t4 = TreeNode(8)
    t5 = TreeNode(10)
    t6 = TreeNode(14)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    tr.in_order(t1)
    # 线索化
    print("线索前：",end=" ", )
    tr.threaded_node(t1)
    # 验证是否线索
    print("\nt5结点：", t5.val)
    print("t5前驱结点：", t5.left.val)
    print("t5后继结点：", t5.right.val)
    print("t5的指示标：", t5.ltag, t5.rtag)
    print("t4的前驱结点：", t4.left)
    print("t3的后继结点：", t3.right)
    print("线索后：", end=" ")
    tr.thread_in_order(t1)
