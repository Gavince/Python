# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 上午9:23
# @Author  : gavin
# @FileName: 101.回文子串.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被
视作不同的子串。

解题方法：
中心扩散法（注意偶数扩散和奇数扩散）
时间复杂度:O(N^2)
空间复杂度：O(1)
"""


class Solution:
    def countSubstrings1(self, s: str) -> int:

        def speard(l, r):
            """中心扩散"""
            count = 0
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count

        res = 0
        # 奇数中心扩散
        for i in range(len(s)):
            res += speard(i, i)
        # 偶数中心扩散
        for i in range(len(s) - 1):
            res += speard(i, i + 1)

        return res

    def countSubstrings2(self, s: str) -> int:

        n = len(s)
        ans = 0

        for i in range(2*n - 1):
            l, r = i//2, i//2 + i%2
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                ans += 1
        return ans