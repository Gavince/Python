# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 下午3:52
# @Author  : gavin
# @FileName: 2.二维数据查找.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281

"""
问题描述：
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数,形式如下:
1  2  3  4
2  3  4  5
6  7  8  9
10 11 12 13
解决方案：
考虑时间复杂度
"""


class Solution:

    def find(self, array, target):
        """不考虑时间复杂度，暴力搜索, T(O)=n^2"""

        for i in range(len(array)):
            for j in range(len(array[i])):
                if array[i][j] == target:
                    return True
        return False

    def find1(self, array, target):
        """T(O) = n"""
        nrows = len(array)
        ncols = len(array[0])
        # 定义维度
        r = nrows - 1
        i = 0
        j = ncols - 1
        flag = False

        while i <= r and j >= 0:  # 右上角进行查找
            if array[i][j] == target:  # 正确查找
                flag = True
                break
            if array[i][j] > target:  # 目标值可能存在于左边
                j -= 1
            if array[i][j] < target:  # 目标值可能存在于底部
                i += 1

        return flag


if __name__ == "__main__":
    Array = [[1, 2, 3, 4],
             [2, 3, 4, 5],
             [6, 7, 8, 9],
             [10, 11, 12, 13]]
    obj = Solution()
    print("Existing:", obj.find(Array, 100))
    print("Existing:", obj.find1(Array, 0))