# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 下午9:29
# @Author  : gavin
# @FileName: 16.链表中环的入口结点.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

解决方案：
栈~
"""


class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:

    def EntryNodeOfLoopCollections(self, pHead):
        """链表环中第一个入口结点"""
        if pHead is None:
            return

        cur = pHead
        stack = []
        while cur:
            if cur not in stack:
                stack.append(cur)
                cur = cur.next
            else:
                return cur

        return None


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)
    g = ListNode(7)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = c

    obj = Solution()
    print(obj.EntryNodeOfLoopCollections(a).val)
