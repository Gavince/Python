# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 上午10:50
# @Author  : gavin
# @FileName: 删除二叉树的结点.py
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
        self.flag = False

    def add(self, val):
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

    def pre_order(self, node):
        """前序遍历"""
        if node is None:
            return
        print(node.val, end=" ")
        self.pre_order(node.left_child)
        self.pre_order(node.right_child)

    def del_node(self, node, val):
        """删除节点的同时需要将左右子树都删除"""
        if node is None:
            return
        if node.val == val and node == self.root:
            self.root = None
            self.flag = True
            return

        #  结点中找的数值,左右结点置空
        if node.val == val:
            node.left_child = None
            node.right_child = None
            return node.val

        # 遍历
        left_part = self.del_node(node.left_child, val)
        if left_part:  # 左树查找有返回值
            node.left_child = None  # 查找结点置空
            self.flag = True

        right_part = self.del_node(node.right_child, val)
        if right_part:  # 右树查找有返回值
            node.left_child = None
            self.flag = True
        return None

    def get_parent(self, val):
        """父亲结点"""

        if self.root.val == val:  # 根节点无父亲节点
            return None

        queue = [self.root]
        while queue:
            tmp_node = queue.pop(0)
            if tmp_node.left_child and tmp_node.left_child.val == val:
                return tmp_node
            if tmp_node.right_child and tmp_node.right_child.val == val:
                return tmp_node

            if tmp_node.left_child:
                queue.append(tmp_node.left_child)
            if tmp_node.right_child:
                queue.append(tmp_node.right_child)

    def delete(self, val):
        """删除指定结点"""

        if self.root is None:
            return False

        # 得到删除结点的父亲结点
        parent = self.get_parent(val)

        if parent:
            # 得到删除结点
            del_node = parent.left_child if parent.left_child.val == val else parent.right_child

            if del_node.left_child is None:
                if parent.left_child.val == val:
                    parent.left_child = del_node.right_child
                else:
                    parent.right_child = del_node.right_child
                del del_node
                return True
            elif del_node.right_child is None:
                if parent.left_child.val == val:
                    parent.left_child = del_node.left_child
                else:
                    parent.right_child = del_node.left_child

                del del_node
                return True
            else:  # 左右树都不为空，找寻删除结点左子树中的最左结点与删除结点进行替换
                tmp_pre = del_node
                tmp_next = del_node.right_child
                if tmp_next.left_child is None:
                    tmp_pre.right_child = tmp_next.right_child
                    tmp_next.left_child = del_node.left_child
                    tmp_next.right_child = del_node.right_child
                else:
                    while tmp_next.left_child:  # 寻找左子树
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left_child

                    tmp_pre.left_child = tmp_next.right_child
                    tmp_next.left_child = del_node.left_child
                    tmp_next.right_child = del_node.right_child
                if parent.left_child.val == val:
                    parent.left_child = tmp_next
                else:
                    parent.right_child = tmp_next
                del del_node
                return True
        else:
            return False


if __name__ == "__main__":
    tree = Tree()
    for i in range(10):
        tree.add(i)
    print("删除前树结构：", end=" ")
    tree.pre_order(tree.root)
    # tree.del_node(tree.root, 55)
    # if tree.flag:
    #     print("\n删除后树结构：", end=" ")
    #     tree.pre_order(tree.root)
    # else:
    #     print("\n树中无指定结点！！！")
    if tree.delete(1):
        print("\n删除后树结构：", end=" ")
        tree.pre_order(tree.root)
    else:
        print("未查找到！")
