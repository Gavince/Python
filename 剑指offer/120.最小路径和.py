# -*- coding: utf-8 -*-
# @Time    : 2021/8/4 下午8:39
# @Author  : gavin
# @FileName: 120.最小路径和.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述:
    给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得
路径上的数字总和为最小。说明：每次只能向下或者向右移动一步。

解题方法:
该题目与礼物的最大值相似,采用动态规划解决
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # grid[i][j]表示当前路径最小值
        # 初始化
        for i in range(1, len(grid)):
            grid[i][0] += grid[i - 1][0]

        for j in range(1, len(grid[0])):
            grid[0][j] += grid[0][j - 1]

        # 状态转移,求解最小路径
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        # 返回状态
        return grid[-1][-1]
