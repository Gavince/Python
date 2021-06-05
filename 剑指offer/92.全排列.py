# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 上午8:02
# @Author  : gavin
# @FileName: 92.全排列.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以
按任意顺序 返回答案。

示例：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


class Solution:

    def permute(self, nums):
        """数组的全排列"""

        res = []

        def dfs(x):
            # 回朔满足
            if x == len(nums) - 1:
                res.append(nums[:])
                return

            dic = set()
            for i in range(x, len(nums)):
                if nums[i] in dic: continue
                dic.add(nums[i])
                # 交换位置
                nums[i], nums[x] = nums[x], nums[i]
                dfs(x + 1)
                nums[i], nums[x] = nums[x], nums[i]

        dfs(0)
        return res


if __name__ == "__main__":
    obj = Solution()
    print(obj.permute([1, 2, 2]))
