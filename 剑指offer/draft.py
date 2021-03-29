class Solution:

    def isBalanced(self, root) -> bool:
        """判断一颗树是否为平二叉树"""

        def hight(root):
            """求解树的高度"""

            if root is None:
                return 0
            left_hight = hight(root.left)
            right_hight = hight(root.right)
            if left_hight == -1 or right_hight == -1 or abs(left_hight - right_hight) > 1:
                return -1
            else:
                return max(left_hight, right_hight) + 1

        return hight(root) >= 0

    def findRepeatNumber(self, nums: [int]) -> int:
        """找出任意重复数组"""

        i = 0
        while i < len(nums):
            if i == nums[i]:  # 索引与值相对应
                i += 1
            if nums[i] == nums[nums[i]]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        return -1

    def test(self, nums: []) -> int:

        dic = set
        for num in nums:
            if num in dic: return num
            dic.add(num)

        return -1

    def constrctArr(self, a):
        """构建数组乘积"""

        b, tmp = len(a)*[1], 1

        #  下三角
        for i in range(1, len(a)):
            b[i] = a[i-1]*b[i-1]

        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i+1]  # 上三角
            b[i] *= tmp  # 上下相乘

        return b

    def isMatch(self, s: str, p: str) -> bool:

        # 匹配数目不一致
        if not p: return not s
        first_match = bool(s and p[0] in {".", s[0]})
        if len(p) >= 2 and p[1] == "*":
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1], p)
        else:
            return first_match and self.isMatch(s[1], p[1])


if __name__ == "__main__":
    obj = Solution()
