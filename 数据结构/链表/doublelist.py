from singlelist import *


class DNode(LNode):
    """ create a node"""

    def __init__(self, elem):
        super().__init__(elem)  # 此处必须为一个next_区别函数内联
        self.prev = None


class DoubleList(object):
    """create a doublelist"""

    def __init__(self):
        self.__head = None  # 初始化头结点

    def IsEmpty(self):
        """判断是否为空"""
        return self.__head is None

    def length(self):
        # 得到列表的长度

        num = 0
        cur = self.__head

        while cur:
            num += 1
            cur = cur.next

        return num

    def travel(self):

        cur = self.__head

        while cur:
            print("Elements:", cur.elem)
            cur = cur.next

    def add(self, item):
        """头插法"""
        # 1.创建节点
        node = DNode(item)
        if self.IsEmpty():  # 无节点
            self.__head = node
        else:

            # 连接node 节点
            node.next = self.__head
            self.__head.prev = node
            # 重新定义头部
            self.__head = node


if __name__ == "__main__":
    ll = DoubleList()
    ll.add(4)
    ll.add(5)
    ll.add(6)
    ll.travel()
