# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 下午9:21
# @Author  : gavin
# @FileName: 13.复杂链表的复制.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
输入一个复杂链表（每个节点中有节点值，以及两个指针，**一个指向下一个节点，另一个特殊指针指向任意一个节点**），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空。

解决方案：
A---  a***  --->B  ***>b
A.next.random = a.random.next
"""


class RandomListNode:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


class Solution:

    def clone(self, phead):

        if phead is None:
            return None

        # 复制结点(插入结点的思想)
        ptemp = phead
        while ptemp:
            node = RandomListNode(ptemp.val)
            node.next = ptemp.next
            ptemp.next = node
            ptemp = node.next

        # 复制random指针
        ptemp = phead

        while ptemp:
            if ptemp.random:
                ptemp.next.random = ptemp.random.next
            ptemp = ptemp.next.next

        #  分离拆解
        ptemp = phead
        newhead = phead.next
        newtemphead = phead.next

        while ptemp:
            ptemp.next = ptemp.next.next
            if newtemphead.next:
                newtemphead.next = ptemp.next.next
                newtemphead = newtemphead.next
            ptemp = ptemp.next

        return newhead

if __name__ == '__main__':
    n1 = RandomListNode(1)
    n2 = RandomListNode(2)
    n3 = RandomListNode(3)
    n4 = RandomListNode(4)
    n5 = RandomListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    obj = Solution()
    new_head = obj.clone(n1)
    while new_head:
        print(new_head.val)
        new_head = new_head.next












