# -*- coding: utf-8 -*-
# @Time    : 2021/7/26 下午1:52
# @Author  : gavin
# @FileName: 113.x的平方根.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    实现int sqrt(int x)函数。计算并返回x的平方根，其中x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

解题方法：
(1)袖珍计算器
时间复杂度：O(1)
空间复杂度：O(1)
(2)二分法
时间复杂度：O(logN)
空间复杂度：O(1)
"""

import math


class Solution:

    def mySqrt1(self, x: int) -> int:
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))

        return ans + 1 if (ans + 1) ** 2 <= x else ans

    def mySqrt2(self, x: int) -> int:
        # 二分查找

        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans