# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 下午8:51
# @Author  : gavin
# @FileName: 0.斐波那契数列.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和
０　１　１　２　３　５　８　... F(n) = F(n-1) + F(n-2)
n > １
"""


class Solution:

    def fibonacci(self, n):
        """递归算法(时间复杂度极高O(n)=２^n)"""
        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        if n > 2:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def fibonacci1(self, n):
        """动态规划问题"""

        if n == 0:
            return 0
        if n == 1:
            return 1
        if n > 1:
            a = 1  # 较大值
            b = 0  # 较小值
            ret = 0
            for i in range(2, n + 1):  # 左闭右开
                ret = a + b
                b = a
                a = ret

            return ret

    def fibonacci2(self, n):
        """列表写法O(n)=n"""

        if n == 0:
            return 0
        if n == 1:
            return 1
        result = [0, 1]
        for i in range(2, n + 1):
            result.append(result[i - 1] + result[i - 2])

        return result[-1]

    def fib(self, n: int) -> int:

        a, b = 0, 1
        for _ in range(n):
            a, b = b, (a + b) % 1000000007
        return a

if __name__ == "__main__":
    obj = Solution()
    print("F1:", obj.fibonacci(10))
    print("F2:", obj.fibonacci1(10))
    print("F3:", obj.fibonacci2(10))
