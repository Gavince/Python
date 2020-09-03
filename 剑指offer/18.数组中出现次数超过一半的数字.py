# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 下午9:33
# @Author  : gavin
# @FileName: 18.数组中出现次数超过一半的数字.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
解决方案：
1.字典{}

"""


class Solution:

    @staticmethod
    def MoreThanHalfNum_Solution(numbers):

        count_dic = {}
        num_len = len(numbers)
        for item in numbers:
            if item in count_dic:
                count_dic[item] += 1
            else:
                count_dic[item] = 1

            if count_dic[item] > (num_len >> 1):
                return item

        return 0

    @staticmethod
    def MoreThanHalfNum_Solution1(numbers):
        """基于排序算法"""
        length = len(numbers)

        if length == 0:
            return 0
        elif length == 1:
            return numbers[0]
        else:
            numbers.sort()
            num = numbers[int(length >> 1)]  # 中间位置的数据
            if numbers.count(num) > (length >> 1):
                return num
            return 0


if __name__ == "__main__":
    obj = Solution()
    array = [1, 5, 2, 5, 5, 5, 5, 5, 6, 7, 5]
    print("Item:", obj.MoreThanHalfNum_Solution(array))
    print("Item:", obj.MoreThanHalfNum_Solution1(array))
