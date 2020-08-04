# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 下午9:36
# @Author  : gavin
# @FileName: 10.链表中倒数第k个结点.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
输入一个链表，输出该链表中倒数第k个结点

解决方案：
"""


class Solution:

    def FindKthToTail(self, head, k):

        node = None
        stack = []
        temp = head
        while temp:
            stack.append(temp)
            temp = temp.next
        if len(stack) >= k:  # k值限制
            for i in range(k):  # 倒数第k个结点
                stack.pop()
            return node
        else:
            return None
