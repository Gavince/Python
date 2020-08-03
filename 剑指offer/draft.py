"""
问题描述：
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

解决方案：
1. 暴力遍历
2. sorted
3.冒泡排序分类
知识点：
a & 1 = 1 奇数 a、1二进制与运算结果 *0000001
"""


class Solution:

    def sort1(self, li):

        new_li = []

        for i in range(len(li)):
            if li[i] & 1 == 1:  # 奇数
                new_li.append(li[i])

        for j in range(len(li)):
            if li[j] & 1 == 0:  # 偶数
                new_li.append(li[j])

        return new_li

    def sort2(self, li):

        return sorted(li, key=lambda x: x % 2, reverse=True)  # reverse 奇偶翻转位置

    def reorder(self, li):

        for i in range(len(li) - 1):  # n-1次比较
            flag = False
            for j in range(len(li) - 1, i, -1):
                if li[j] % 2 == 1 and li[j - 1] % 2 == 0:  #后奇前偶，做交换
                    li[j], li[j - 1] = li[j - 1], li[j]
                    flag = True
            if flag is False:
                break
        return li

    def reorder1(self, li):

        for i in range(len(li)-1):
            flag = False
            for j in range(len(li)-1-i):
                if li[i] % 2 == 0 and li[i+1] % 2 == 1:
                    li[i], li[i+1] = li[i+1], li[i]
                    flag = True
            if flag is False:
                break

        return li


if __name__ == "__main__":
    obj = Solution()
    array = [1, 2, 9, 5, 6, 8, 7, 3, 12]
    print("原数据：", array)
    print("排序： ", obj.sort1(array))
    print("排序： ", obj.sort2(array))
    print("排序： ", obj.reorder(array))
    print("排序： ", obj.reorder1(array))