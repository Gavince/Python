# -*- coding: utf-8 -*-
# @Time    : 2021/2/14 上午10:21
# @Author  : gavin
# @FileName: 36.连续子数组的最大和.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281

class Solution:

    def MaxArray(self, nums):
        """最大子数组之和"""

        for i in range(1, len(nums)):
            nums[i] += max(nums[i-1], 0)

        return max(nums)