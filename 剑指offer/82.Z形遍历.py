# -*- coding: utf-8 -*-
# @Time    : 2021/5/24 下午2:34
# @Author  : gavin
# @FileName: 82.Z形遍历.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

实例：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I

解题方法：
遍历
时间复杂度：O(n)
空间复杂度：O(n)
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows < 2:
            return s
        # 初始化行存储
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        # 遍历存储
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag

        return "".join(res)

