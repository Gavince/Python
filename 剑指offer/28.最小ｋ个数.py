# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 上午7:42
# @Author  : gavin
# @FileName: 28.最小ｋ个数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

解决方案：
构建堆，heapq构造的是小顶堆，即堆顶元素最小，因此为了构造大顶堆，需要将元素都加负号，来颠倒他们的大小关系
，相反数的小顶堆，就相当于原来数的大顶堆。求前K个最大的数，用小顶堆，K个小的数，用大顶堆。

参考:
@ 剑指offer（python）最小的k个数：https://blog.csdn.net/guoweimelon/article/details/50904346


"""
import heapq  # 默认构建最小堆，即父节点的值大于其任意子节点的值


class Solution:

    def getLeastNumbers(self, arr, k):

        if k == 0:
            return list()
        # 默认最大堆
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans

print(Solution().getLeastNumbers([3, 2, 1], 2))