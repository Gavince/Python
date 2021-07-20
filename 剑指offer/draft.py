import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def levelOrder(self, root):

        deque = collections.deque(root)
        res = []
        while deque:
            tmp = []
            for _ in range(len(deque)):
                node = deque.popleft()
                tmp.append(node.val)
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)

            res.append(tmp)

        return res
