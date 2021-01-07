class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None


class Solution:

    def HasSubTree(self, pRoot1, pRoot2):

        if pRoot2 is None or pRoot1 is None:
            return None
        return self.isSubTree(pRoot1, pRoot2)

    def isSubTree(self, pRoot1, pRoot2):

        if pRoot2 is None and pRoot1 is None:
            return True
        if pRoot1 is None:
            return False
        if pRoot2 is None:
            return False

        if pRoot1.val == pRoot2.val:
            if pRoot2.left is None and pRoot2.right is None:
                return True
            else:
                if self.isSubTree(pRoot1.left, pRoot2.left) and self.isSubTree(pRoot1.right, pRoot2.right):
                    return True

        return self.isSubTree(pRoot1.left, pRoot2) or self.isSubTree(pRoot1.right, pRoot2)