# -*- coding: utf-8 -*-
# @Time    : 2021/5/15 下午5:18
# @Author  : gavin
# @FileName: 76.最长递增子序列.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    　给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。子序列是
由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

解题方法：
（１）动态规划四步走原则
(1)转态定义：dp[i]表示到当前结点i所表示的子序列的长度
(2)转态转移：dp[i] = max(dp[i], dp[j] + 1)，表示为i之前最大的递增子序列
(3)初始值：dp = [1]*len(nums)
(4)返回值：max(dp)
时间复杂度：O(N^2)
空间复杂度：O(N)  dp状态的存储

(2)二分法
时间复杂度：O(NlogN)
空间复杂度：O(1)
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # 动态规划
        if not nums: return 0
        # 定义dp,并设置初始值
        dp = [1] * len(nums)
        # 遍历转态
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    # 更新状态
                    dp[i] = max(dp[i], dp[j] + 1)

        # 输出最长子序列中的任意一个子序列
        max_index = dp.index(max(dp))
        res = [nums[max_index]]
        for i in range(max_index, -1, -1):
            if nums[i] < nums[max_index] and dp[i] == dp[max_index] - 1:
                res.append(nums[i])
                max_index = i
        # 返回值
        return res


if __name__ == "__main__":
    obj = Solution()
    print(obj.lengthOfLIS([10,9,2,5,3,7,101,18]))