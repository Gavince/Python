# -*- coding: utf-8 -*-
# @Time    : 2021/7/24 上午10:52
# @Author  : gavin
# @FileName: 112.数组中的第K个最大元素.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
题目描述：

解题方法：

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