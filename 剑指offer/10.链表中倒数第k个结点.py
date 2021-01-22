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

    # @staticmethod
    # def FindKthToTail(head, k):
    #
    #     if not head or not k:
    #         return None
    #
    #     node = None
    #     stack = []
    #     temp = head
    #     while temp:
    #         stack.append(temp)
    #         temp = temp.next
    #     if len(stack) >= k:  # k值限制
    #         for i in range(k):  # 倒数第k个结点
    #             node = stack.pop()
    #         return node
    #     else:
    #         return None

    def FindKthToTail(self, head, k):
        """双指针，两个指针之间相差k值"""

        former, latter = head, head
        for _ in range(k):
            if not former: return None
            former = former.next

        while former:
            former = former.next
            latter = latter.next

        return latter

