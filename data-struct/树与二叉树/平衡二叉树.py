# -*- coding: utf-8 -*-
# @Time    : 2020/5/10 上午8:54
# @Author  : gavin
# @FileName: 平衡二叉树.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
# python深拷贝　：https://www.runoob.com/w3cnote/python-understanding-dict-copy-shallow-or-deep.html
import copy


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class AVLTree:

    def __init__(self):
        self.root = None

    def get_left_height(self, node):
        """获取左子树高度"""

        if node is None:
            return 0

        return self.get_tree_height(node.left)

    def get_right_height(self, node):
        """获取右子树高度"""

        if node is None:
            return 0

        return self.get_tree_height(node.right)

    def get_tree_height(self, node):
        """获取树高度"""

        if node is None:
            return 0

        return max(self.get_tree_height(node.left), self.get_tree_height(node.right)) + 1

    def add_node(self, val):
        """添加结点"""

        node = TreeNode(val)
        if self.root is None:
            self.root = node
            return

        queue = [self.root]
        while queue:
            temp_node = queue.pop(0)
            # 左子树
            if node.val < temp_node.val:
                if temp_node.left is None:
                    temp_node.left = node
                    return
                else:
                    queue.append(temp_node.left)
            # 右子树
            if node.val >= temp_node.val:
                if temp_node.right is None:
                    temp_node.right = node
                    return
                else:
                    queue.append(temp_node.right)

    @staticmethod
    def left_rotate(node):
        """RR型，左旋"""

        if node is None:
            return

        # 创建新的结点，保存左旋后的结点
        new_node = copy.deepcopy(node)
        new_node.left = node.left
        new_node.right = node.right.left

        # 连接新的左右结点
        node.val = node.right.val
        node.right = node.right.right
        node.left = new_node

    @staticmethod
    def right_rotate(node):
        """LL型，右旋"""

        if node is None:
            return
        # 创建新的结点，保存左旋后的结点
        new_node = copy.deepcopy(node)
        new_node.right = node.right
        new_node.left = node.left.right

        # 连接新的左右结点
        node.val = node.left.val
        node.left = node.left.left
        node.right = new_node

    def jude_node(self, node):
        """判断二叉树是否平衡"""

        # 　1.右子树高于左子树，
        if self.get_right_height(node) - self.get_left_height(node) > 1:
            if node.right and self.get_left_height(node.right) > self.get_right_height(node.right):
                # RL型，右旋后左旋
                self.right_rotate(node.right)
                self.left_rotate(self.root)
            else:
                self.left_rotate(self.root)

            return

        # 2.左子树高于右子树
        if self.get_left_height(node) - self.get_right_height(node) > 1:
            if node.left and self.get_right_height(node.left) > self.get_left_height(node.left):
                # LR型，左旋后右旋
                self.left_rotate(node.left)
                self.right_rotate(self.root)
            else:
                self.right_rotate(self.root)

    def in_order(self, node):

        if node is None:
            return

        self.in_order(node.left)
        print(node.val, end=" ")
        self.in_order(node.right)

    def pre_order(self, node):

        if node is None:
            return

        print(node.val, end=" ")
        self.pre_order(node.left)
        self.pre_order(node.right)


if __name__ == "__main__":

    node_array1 = [4, 3, 6, 5, 7, 8]
    node_array2 = [10, 12, 8, 9, 7, 6]
    node_array3 = [10, 11, 7, 6, 8, 9]
    node_array4 = [10, 7, 16, 14, 17, 13, 15]
    node_arrays = [node_array1, node_array2, node_array3, node_array4]
    names = ["RR", "LL", "LR", "RL"]
    for name, node_array in zip(names,node_arrays):
        avg = AVLTree()
        for x in node_array:
            avg.add_node(x)
        print(name + "未平衡：", end=" ")
        avg.in_order(avg.root)
        print()
        print(name + "平衡后：", end=" ")
        avg.jude_node(avg.root)
        avg.pre_order(avg.root)
        print()
    # avg.in_order(avg.root)
    # print("\n左子树", avg.get_left_height(avg.root))
    # print("右子树", avg.get_right_height(avg.root))
    # print("树高度", avg.get_tree_height(avg.root))

