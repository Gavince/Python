# -*- coding: utf-8 -*-
# @Time    : 2021/8/2 下午10:10
# @Author  : gavin
# @FileName: 119.K 个一组翻转链表.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你一个链表，每k个节点一组进行翻转，请你返回翻转后的链表。
k是一个正整数，它的值小于或等于链表的长度。如果节点总数不是k的
整数倍，那么请将最后剩余的节点保持原有顺序。
进阶：
你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

解题方法：
时间复杂度：O(N)
空间复杂度：O(N)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverse(self, head, tail):

        pre = tail.next
        cur = head
        while pre != tail:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nxt = tail.next
            head, tail = self.reverse(head, tail)
            pre.next = head
            tail.next = nxt
            pre = tail
            head = tail.next

        return hair.next
