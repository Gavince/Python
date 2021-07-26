# -*- coding: utf-8 -*-
# @Time    : 2021/7/24 上午10:26
# @Author  : gavin
# @FileName: 111.反转链表.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你单链表的头指针 head 和两个整数left和right ，其中left <= right。请你反转从位置 eft到位
置 right 的链表节点，返回 反转后的链表。

示例：
输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]

解题方法：
穿针引线
时间复杂度：O(N)
空间复杂度:O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        # 申请哑节点
        dummmy = ListNode(0)
        dummmy.next = head
        # 记录
        count = 1
        pre = dummmy
        # 找到开头节点
        while pre.next and count < left:
            pre = pre.next
            count += 1

        cur = pre.next
        tail = cur
        # 局部翻转
        while cur and count <= right:
            nxt = cur.next
            # 节点插入连接
            cur.next = pre.next
            pre.next = cur
            # tail节点始终未变，只有指向在变换
            tail.next = nxt
            # 移动
            cur = nxt
            count += 1

        return dummmy.next
