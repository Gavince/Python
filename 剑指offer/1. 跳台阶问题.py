# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 下午2:42
# @Author  : gavin
# @FileName: 1. 跳台阶问题.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281

"""
问题描述1：一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果
解决方案：
当n=0 0
n=1 1
n=2 2
n=3 3
n=4 5
．．．．．．
所以，符合斐波那契数列f(n) = f(n-1) + f(n-2)

问题描述2：一只青蛙一次可以跳上1级台阶，也可以跳上2级,更可以一次跳上n级台阶
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果
解决方案：
n = 0 0
n = 1 1
n = 2 2
n = 3 4
．．．．．．
所以，f(n) = 2f(n-1)
"""


class Solution:

    def jump_floor(self, n: int):
        """
        :param n: 台阶
        :return: 多少种跳法
        """

        if n == 0 or n == 1 or n == 2:
            return n
        if n >= 3:
            result = [1, 2]
            for i in range(2, n):
                result.append(result[i-1] + result[i-2])

            return result[-1]

    def jump_floor1(self, n: int):

        if n == 0 or n == 1 or n == 2:
            return n

        if n > 2:
            a = 2
            b = 1
            ret = 0
            for i in range(3, n + 1):
                ret = a + b
                b = a
                a = ret

        return ret

    def jump_floor2(self, n: int):

        if n == 0 or n == 1:
            return n

        if n > 2:
            max_val = 1
            temp = 1
            for i in range(2, n + 1):
                temp = 2 * max_val
                max_val = temp

        return temp

    def jump_floor3(self, n: int):

        if n == 0 or n == 1:
            return n

        return 2 * self.jump_floor3(n - 1)


if __name__ == "__main__":
    obj = Solution()
    print("The floor nums:", obj.jump_floor(4))
    print("The floor nums:", obj.jump_floor1(4))

    print("The floor(v2) nums:", obj.jump_floor2(4))
    print("The floor(v1) nums:", obj.jump_floor3(4))
