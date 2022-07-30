# -*- coding: utf-8 -*-
# @Time    : 2020/5/1 下午3:04
# @Author  : gavin
# @FileName: 哈夫曼树构建.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


import operator


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class HuffmanTree:

    @staticmethod
    def create_huffman_tree(array):
        """创建huffman树"""

        # 创建结点
        nodes = []
        for item in array:
            nodes.append(TreeNode(item))

        # 排序，构建哈夫曼树
        while len(nodes) > 1:
            temp = operator.attrgetter("val")
            nodes.sort(key=temp)

            # 选择最小的两个权值结点
            left_node = nodes.pop(0)
            right_node = nodes.pop(0)

            # 创建新的结点
            parent_node = TreeNode(left_node.val + right_node.val)
            parent_node.left = left_node
            parent_node.right = right_node

            # 加入序列进行比较
            nodes.append(parent_node)
        return nodes[0]

    def pre_order(self, node):

        if node is None:
            return

        print(node.val, end=" ")
        self.pre_order(node.left)
        self.pre_order(node.right)


if __name__ == "__main__":
    li = [1, 5, 3, 9, 8 ,6]
    htree = HuffmanTree()
    root = htree.create_huffman_tree(li)
    htree.pre_order(root)