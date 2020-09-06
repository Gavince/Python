# -*- coding: utf-8 -*-
# @Time    : 2020/9/4 上午8:08
# @Author  : gavin
# @FileName: 21.数组中只出现一次的数字.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述:
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
解决方案:
1. 字典
2.异或
概念：参与运算的两个值，如果两个相应位相同，则结果为0，否则为1。即：0^0=0， 1^0=1， 0^1=1， 1^1=0
"""


class Solution:

    def FindNumsAppearOnce(self, array):
        """寻找只出出现一次的数字"""

        memories = dict()
        for val in array:
            if val not in memories:
                memories[val] = 0  # 初始化
            memories[val] += 1

        result = []
        for key, item in memories.items():
            if item == 1:
                result.append(key)
            else:
                continue

        return result

    def FindNumsAppearOnce1(self, array):
        """异或运算"""

        if not array:
            return []

        temp = 0
        for i in array:
            temp ^= i
        # 寻早第一个为1的二进制位置
        index = 0
        while (temp & 1) == 0:
            temp >>= 1
            index += 1

        # a, b两个数组
        a = b = 0
        for i in array:
            if self.one(i, index):
                a ^= i
            else:
                b ^= i
        return [a, b]

    def one(self, data, index):

        data >>= index
        return data & 1


if __name__ == "__main__":
    li = [1, 2, 2, 5, 5, 7, 1, 8, 7, 6]
    obj = Solution()
    print(obj.FindNumsAppearOnce(li))
    print(obj.FindNumsAppearOnce1([1, 2, 2, 5, 5, 7, 1, 8, 7, 6]))
