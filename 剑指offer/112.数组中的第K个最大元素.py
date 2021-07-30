# -*- coding: utf-8 -*-
# @Time    : 2021/7/24 上午10:52
# @Author  : gavin
# @FileName: 112.数组中的第K个最大元素.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
题目描述：
    给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。请注意，
你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

解题方法：
快速排序

时间复杂度：O(NlogN)
空间复杂度：O(1)

"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def quickSort(low, high):
            if low >= high:
                return

                # 设置边界条件
            i, j = low, high
            pivot = nums[i]
            while i < j:
                while i < j and nums[j] >= pivot:
                    j -= 1
                nums[i] = nums[j]

                while i < j and nums[i] < pivot:
                    i += 1
                nums[j] = nums[i]
            nums[i] = pivot
            quickSort(low, i - 1)
            quickSort(i + 1, high)

        quickSort(0, len(nums) - 1)

        return nums[-k]