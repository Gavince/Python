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
1. 递归
2. 循环
"""


class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:

    @staticmethod
    def reverse_list(pHead):

        if not pHead or pHead.next is None:
            return pHead

        newHead = None
        cur = pHead
        while cur:
            tmp = cur.next
            cur.next = newHead
            newHead = cur
            cur = tmp

        return newHead


if __name__ == "__main__":
    n1 = ListNode(1)  # 依次实例5个结点
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2  # 依次将结点链接起来，形成一个链表
    n2.next = n3
    n3.next = n4
    n4.next = n5
    head1, head2 = n1, n1
    print("翻转前的链表：", end=" ")
    while head1:
        print(head1.val, end=" ")
        head1 = head1.next

    obj = Solution()
    p = obj.reverse_list(head2)
    print("\n翻转后的链表：", end=" ")
    while p:
        print(p.val, end=" ")
        p = p.next
