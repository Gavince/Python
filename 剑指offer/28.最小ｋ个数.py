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

    def GetLeastNumbers_Solution(self, tinput, k):

        maxhead = []
        if k <= 0 or len(tinput) < k or tinput == []:
            return []

        # 　构建堆
        for i in range(k):
            heapq.heappush(maxhead, -tinput[i])

        for i in range(k, len(tinput)):
            if maxhead[0] > -tinput[i]:  # 当输入元素小于堆的最小元素时，则不进行堆内添加,以维持k值最小，如:-8 < -4
                continue
            else:
                heapq.heappushpop(maxhead, -tinput[i])

        result = []

        for i in range(k):
            result.insert(0, -heapq.heappop(maxhead))

        return result


if __name__ == "__main__":
    obj = Solution()
    li = [4, 5, 1, 6, 2, 7, 3, 8]
    print(obj.GetLeastNumbers_Solution(li, 4))
