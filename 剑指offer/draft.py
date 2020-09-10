class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def Mirror(self, root):

        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        root.left, root.right = root.right, root.left

        self.Mirror(root.left)
        self.Mirror(root.right)

        return root