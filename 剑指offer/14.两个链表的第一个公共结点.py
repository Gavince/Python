# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 下午8:50
# @Author  : gavin
# @FileName: 14.两个链表的第一个公共结点.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
输入两个链表，找出它们的第一个公共结点

解决方案：
1. 暴力搜索
No Recommend
2.使用栈从后向前找出第一个不相等的结点
A:1 2 5 6
公共结点---->10 11 55 88
B:2 4 8 9

3. 交替遍历指针
p1 -> --->......p1=p2
p2 --> ---->......return p1
实例：
a:1 2 3 4  10 10 10
b:0 7 8 9 6 5 2  10 10 10
c(公共部分): 10 10 10
a + c + b = b + c + a
"""


class Solution:

    def FindFristCommonNode(self, pHead1, pHead2):

        res_set = {}
        # 加入
        while pHead1:
            res_set.add(pHead1)
            pHead1 = pHead1.next
        # 对比
        while pHead2:
            if pHead2 in res_set:
                return pHead2
            pHead2 = pHead2.next

    def FindFristCommonNode1(self, pHead1, pHead2):

        stack1 = []
        stack2 = []
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next
        while stack1 and stack2 and stack1[-1] == stack2[-1]:
            res = stack1.pop()
            stack2.pop()
        return res

    def FindFristCommonNode2(self, pHead1, pHead2):

        if pHead1 is None or pHead2 is None:
            return None
        p1 = pHead1
        p2 = pHead2
        while p1 != p2:
            p1 = pHead2 if p1 is None else p1.next
            p2 = pHead1 if p2 is None else p2.next
        return p1


if __name__ == "__main__":
    obj = Solution()
