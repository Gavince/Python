# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 下午9:42
# @Author  : gavin
# @FileName: 11.链表翻转.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
输入一个链表，反转链表后，输出新链表的表头

解决方案：
1.迭代法
2.递归法
"""


class Solution:

    def reverseList1(self, pHead):
        """链表的翻转"""

        cur, pre = pHead, None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        return pre

    def reverseList2(self, head: ListNode) -> ListNode:
        """递归的方式"""

        if head is None or head.next is None:
            return head

        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return node
