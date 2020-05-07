# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 上午9:36
# @Author  : gavin
# @FileName: 二叉搜索树.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySortTree:
    """构建二叉搜索树"""

    def __init__(self):
        self.root = None

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

    def insert(self, node, val):
        """插入元素（递归）"""

        if node is None:
            node = TreeNode(val)
            node.left = node.right = None
        else:
            #  递归左右结点实现，并返回值进行构建树
            if val < node.val:
                node.left = self.insert(node.left, val)
            elif val > node.val:
                node.right = self.insert(node.right, val)

        return node

    def pre_order(self, node):
        """前序遍历"""

        if node is None:
            return

        print(node.val, end=" ")
        self.pre_order(node.left)
        self.pre_order(node.right)

    def find(self, node, val):
        """查找结点(递归)"""

        if node is None:
            return

        if val < node.val:
            return self.find(node.left, val)
        elif val > node.val:
            return self.find(node.right, val)
        return node

    @staticmethod
    def iter_find(node, val):
        """查找结点(迭代)"""

        while node:
            if val > node.val:
                node = node.right
            elif val < node.val:
                node = node.left
            else:  # node.val == val
                return node

        return None

    def find_min(self, node):
        """找出最小的值(递归),左小右大原则"""

        if node is None:  # 空BST
            return

        elif node.left is None:
            return node
        else:
            return self.find_min(node.left)

    @staticmethod
    def find_max(node):
        """找出最大值(迭代)"""

        if node:
            while node.right:  # 遍历最右边的结点
                node = node.right
        return node

    def del_node(self, node, val):
        """删除结点"""

        if node is None:
            print("删除元素暂未找到")

        elif val < node.val:
            node.left = self.del_node(node.left, val)
        elif val > node.val:
            node.right = self.del_node(node.right, val)
        else:
            if node.left and node.right:  # 删除结点具有两个子结点
                tmp = self.find_min(node.right)  # 找寻右子树的最小结点值
                node.val = tmp.val  # 把结点元素的置换
                node.right = self.del_node(node.right, node.val)
            else:
                tmp = node
                #  有一个子结点或无子结点删除
                if node.left is None:  # 有右孩子或无子结点
                    node = node.right
                elif node.right is None:  # 有左孩子或无子节点
                    node = node.left
                del tmp

        return node


if __name__ == "__main__":
    bst = BinarySortTree()
    array = [7, 3, 10, 12, 5, 1, 9, 2]
    for x in array:
        bst.add_node(x)
    print("BST先序遍历：", end=" ")
    bst.pre_order(bst.root)
    print("\nBST最小结点值：", bst.find_min(bst.root).val)
    print("BST最大结点值：", bst.find_max(bst.root).val)
    print("BST测试删除操作")
    print("*"*40)
    print("BST删除结点(右左右孩子)：", end=" ")
    bst.del_node(bst.root, 7)
    bst.pre_order(bst.root)
    print("\nBST删除结点(有一个子孩子)：", end=" ")
    bst.del_node(bst.root, 1)
    bst.pre_order(bst.root)
    print("\nBST删除结点(无子孩子)：", end=" ")
    bst.del_node(bst.root, 12)
    bst.pre_order(bst.root)
    print()
    print("*" * 40)
    print("BST重新插入结点(7)：", end=" ")
    bst.insert(bst.root, 7)
    bst.pre_order(bst.root)