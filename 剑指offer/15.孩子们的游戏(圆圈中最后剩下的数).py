# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 下午8:42
# @Author  : gavin
# @FileName: 15.孩子们的游戏(圆圈中最后剩下的数).py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
有个游戏是这样的：首先，让小朋友们围成一个大圈。然后，随机指定一个数 m，让编号为 0 的小朋友开始报数
。每次喊到 m-1 的那个小朋友要出列唱首歌，然后可以在礼品箱中任意的挑选礼物，并且不再回到圈中，从他的
下一个小朋友开始，继续0…m-1报数…这样下去…直到剩下最后一个小朋友，可以不用表演，并且拿到终极大奖。请
你试着想下，哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从 0 到 n-1 ) 如果没有小朋友，请返回 -1

解决方案：

"""
import sys

sys.setrecursionlimit(1000000)


class Solution:

    def LastRemaining_Solution(self, n: int, m: int):
        """
        :param n:小孩数
        :param m: 指定编号
        :return:
        """
        if n < 1:
            return -1

        start = 0
        final = -1
        indexlist = list(range(n))  # 构造

        while indexlist:
            #  剔除位置
            k = (start + m - 1) % n
            n -= 1
            final = indexlist.pop(k)
            # print("final", final)
            #  删除上一元素之后，向前对其
            start = k
        return final

    def LastRemaining_Solution1(self, n: int, m: int):

        if n == 0:
            return -1
        if n == 1:
            return 0
        return (self.LastRemaining_Solution(n - 1, m) + m) % n


if __name__ == "__main__":
    obj = Solution()
    print(obj.LastRemaining_Solution(5, 3))
    print(obj.LastRemaining_Solution1(1, 5))
