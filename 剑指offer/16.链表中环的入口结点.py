# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 下午9:29
# @Author  : gavin
# @FileName: 16.链表中环的入口结点.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
	给定一个链表，返回链表开始入环的第一个节点。如果链表无环，则返回null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索
引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识
环的情况，并不会作为参数传递到函数中。说明：不允许修改给定的链表。

进阶：
你是否可以使用 O(1) 空间解决此题？

解题方法：
（1）栈
时间复杂度：O(N)
空间复杂度：O(N)
（2）快慢指针
时间复杂度：O(N)
空间复杂度：O(1)
"""


class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:

    def detectCycle(self, head: ListNode) -> ListNode:

        slow, fast = head, head
        while True:
            if not fast or not fast.next: return None
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break

        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast
