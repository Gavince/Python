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

        if node is None:
            return 0

        return self.get_tree_height(node.left)

    def get_right_height(self, node):

        if node is None:
            return 0

        return self.get_tree_height(node.right)

    def get_tree_height(self, node):

        if node is None:
            return 0

        return max(self.get_left_height(node.left), self.get_left_height(node.right)) + 1

    def add_node(self, val):
        """BST添加"""

        node = TreeNode(val)

        if self.root is None:
            self.root = node
            return

        queue = [self.root]

        while queue:
            tmp_node = queue.pop(0)

            if node.val < tmp_node.val:
                if tmp_node.left is None:
                    tmp_node.left = node
                    return
                else:
                    queue.append(tmp_node.left)

            if node.val >= tmp_node.pop(0):
                if tmp_node.right is None:
                    tmp_node.right = node
                    return
                else:
                    queue.append(tmp_node.right)

    def left_rotate(self, node):
        """RR型"""

        if node is None:
            return

        new_node = copy.deepcopy(node)
        new_node.left = node.left
        new_node.right = node.right.left

        node.val = node.right.val
        node.right = node.right.right
        node.left = new_node

    def right_rotate(self, node):
        """LL型"""

        if node is None:
            return

        new_node = copy.deepcopy(node)
        new_node.right = node.right
        new_node.left = node.left.right

        node.val = node.left.val
        node.left = node.left.left
        node.right = new_node

    def jude_node(self, node):

        if self.get_right_height(node) - self.get_left_height(node) > 1:
            if node.right and self.get_left_height(node.right) > self.get_right_height(node.right):
                self.right_rotate(node.right)
                self.left_rotate(self.root)

            else:
                self.left_rotate(self.root)

        if self.get_right_height(node) - self.get_left_height(node) < 1:
            if node.left and self.get_right_height(node.left) > self.get_left_height(node.left):
                self.left_rotate(node.left)
                self.right_rotate(self.root)
            else:
                self.right_rotate(self.root)




