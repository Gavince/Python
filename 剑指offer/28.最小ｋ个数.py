# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 上午7:42
# @Author  : gavin
# @FileName: 28.最小ｋ个数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
    输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这
8个数字，则最小的4个数字是1,2,3,4,。

解决方案：
(1) heapq
    构建堆，heapq构造的是小顶堆，即堆顶元素最小，因此为了构造大顶堆
，需要将元素都加负号，来颠倒他们的大小关系，相反数的小顶堆，就相当于
原来数的大顶堆。求前K个最大的数，用小顶堆，K个小的数，用大顶堆。
(2) quick sort
未优化：所有数字先有序化，后截取指定区间内的数字
时间复杂度：O(nlogn)
空间复杂度：O(n)
优化：旨在k区间内进行寻找
若 k = l，我们就找到了最小的 k 个数，就是左侧的数组；
若 k<l，则最小的 k 个数一定都在左侧数组中，我们只需要对左侧数组递归
地 parition 即可；
若 k>l，则左侧数组中的 l 个数都属于最小的 k 个数，我们还需要在右侧
数组中寻找最小的 k-l 个数，对右侧数组递归地 partition 即可。

时间复杂度：O(n)
空间复杂度：o(logn)

"""
import heapq  # 默认构建最大堆，即父节点的值大于其任意子节点的值


class Solution:

    def getLeastNumbersfForHeap(self, arr, k):
        """"获取最小k个数字"""

        if k == 0:
            return list()

        # 构建最大堆
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)

        for i in range(k, len(arr)):
            if hp[0] <= -arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        res = [-x for x in hp]

        return res

    def getLeastNumbersForSort(self, numbs, k):

        def quickSort(nums, start, end):
            """"快速排序法"""

            if start >= end:
                return list()

            low = start
            high = end
            mid = nums[start]

            while low < high:
                while low < high and nums[high] >= mid:
                    high -= 1
                nums[low] = nums[high]
                while low < high and nums[low] < mid:
                    low += 1
                nums[high] = nums[low]
            # 交换基准
            nums[low] = mid
            quickSort(nums, start, low - 1)
            quickSort(nums, low + 1, end)
        quickSort(numbs, 0, len(numbs) - 1)

        return numbs[:k]


if __name__ == "__main__":
    numbers = [1, 5, 2, 4, 9, 7, 3]
    obj = Solution()
    print(obj.getLeastNumbersfForHeap(arr=numbers, k=3))
    print(obj.getLeastNumbersForSort(numbs=numbers, k=3))