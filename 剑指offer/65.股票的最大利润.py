# -*- coding: utf-8 -*-
# @Time    : 2021/5/3 上午9:24
# @Author  : gavin
# @FileName: 65.股票的最大利润.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

示例：
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

解题方法：
动态规划
"""


class Solution:
    def maxProfit(self, prices) -> int:
        cost, profit = float("+inf"), 0
        for price in prices:
            # 低谷
            cost = min(cost, price)
            # 利润最大化
            profit = max(profit, price - cost)

        return profit