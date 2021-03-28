class Solution:

    def isBalanced(self, root) -> bool:
        """判断一颗树是否为平二叉树"""

        def height(root):
            """求解树的高度"""
            if root is None: return 0
            leftHight = height(root.left)
            rightHight = height(root.right)
            if leftHight == -1 or rightHight == -1 or abs(leftHight - rightHight) > 1:
                return -1
            else:
                # 树左右结点高度不能超过１
                return max(leftHight, rightHight) + 1

        return height(root) >= 0


if __name__ == "__main__":
    obj = Solution()
