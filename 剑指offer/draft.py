class TreeNode:

    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def reverse(self, root):
        res = []
        def dfs(root):
            if root is None:
                return

            res.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return res


if __name__ == "__main__":
    a, b, c, d, e, f = [TreeNode(val) for val in [1, 3, 4, 6, 7, 5]]
    a.left, a.right = b, c
    b.left = d
    c.left, c.right = e, f
    obj = Solution()
    print(obj.reverse(a))



