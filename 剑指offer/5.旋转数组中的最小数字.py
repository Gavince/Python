# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 下午4:59
# @Author  : gavin
# @FileName: 5.旋转数组中的最小数字.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0

解决方案:
1. 暴力搜索
2. 二分法
https://zhuanlan.zhihu.com/p/136849860
"""


class Solution:

    def seek(self, array):

        min_num = 0

        for i in range(len(array)):
            if min_num < array[i] and min_num != 0:
                min_num =min_num
                
            else:
                return array[i]

    def find_num(self, RotateArray):

        # 条件1：数组大小为空，返回0
        if not RotateArray:
            return 0

        if len(RotateArray) == 1:
            return RotateArray[0]

        left = 0
        right = len(RotateArray) - 1

        while left <= right:
            middle = (right + left) // 2
            # 真值比左面小，则表示找到相应的数值
            if RotateArray[middle] < RotateArray[middle - 1]:
                return RotateArray[middle]
            # 中值小于右面, 其值在左面
            elif RotateArray[middle] < RotateArray[right]:
                right = middle - 1
            else:
                left = middle + 1

        return 0


if __name__ == "__main__":
    obj = Solution()
    Rl1 = [2, 3, 4, 5, 1]
    Rl2 = [3, 4, 5, 1, 2]
    Rl3 = [4, 5, 1, 2, 3]
    Rl4 = [5, 1, 2, 3, 4]
    print(obj.find_num(Rl1))
    print(obj.find_num(Rl2))
    print(obj.find_num(Rl3))
    print(obj.find_num(Rl4))
    print(obj.find_num([5, 2, 4]))
    print(obj.find_num([5, 1]))
    print(obj.find_num([5]))
    print(obj.find_num([4, 5, 5, 1, 1, 2, 3]))
