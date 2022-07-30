# -*- coding: utf-8 -*-
# @Time    : 2020/5/4 上午9:32
# @Author  : gavin
# @FileName: 哈夫子曼编码.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
# https://www.cnblogs.com/kubixuesheng/p/4397798.html
# https://blog.csdn.net/ustbbsy/article/details/79637594

import operator
from operator import itemgetter


class TreeNode:

    def __init__(self, val, weight):
        self.val = val
        self.weight = weight
        self.left = None
        self.right = None


class HuffmanTree:
    """构建HuffmanTree"""

    @staticmethod
    def get_nodes(bytes_array):
        """获得字符的频率"""
        nodes = []
        dict = {}

        for x in bytes_array:
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] += 1
        # 排序
        dict_list = sorted(dict.items(), key=itemgetter(0), reverse=True)
        for item in dict_list:
            nodes.append(TreeNode(item[0], item[1]))

        return nodes

    @staticmethod
    def create_huffman_tree(nodes):
        """创建huffman树"""

        while len(nodes)>1:
            nodes.sort(key=operator.attrgetter("weight"))
            left_node = nodes.pop(0)
            right_node = nodes.pop(0)

            #  最小权重结点合并
            parent_node = TreeNode(0, left_node.weight+right_node.weight)
            parent_node.left = left_node
            parent_node.right = right_node
            #  加入新的比较结点
            nodes.append(parent_node)

        return nodes[0]

    def get_codes(self, node, path, temp):
        """获取字符的huffman编码"""

        if node is None:
            return

        #  叶子结点终止，并输出其字符
        if node.left is None and node.right is None:
            temp[str(node.val)] = path
            return temp

        if node.left:
            self.get_codes(node.left, path+"0", temp)
        if node.right:
            self.get_codes(node.right, path + "1", temp)

    def pre_order(self, node):

        if node is None:
            return

        print(node.val, end=" ")
        self.pre_order(node.left)
        self.pre_order(node.right)


if __name__ == "__main__":
    content = "i like like like java do you like a java"
    content_bytes = content.encode("utf-8")
    h = HuffmanTree()
    obj_list = h.get_nodes(content_bytes)
    root = h.create_huffman_tree(obj_list)
    # h.pre_order(root)
    out_put = {}
    h.get_codes(root, "", out_put)
    for key, value in out_put.items():
        print(chr(int(key)), ":", value)