class Node:
    """结点"""
    count = 0

    def __init__(self, elem):
        self.elem = elem
        self.next = None
        Node.count += 1


class CList:
    """创建循环链表"""

    def __init__(self):
        self._head = None

    @staticmethod
    def get_length():
        """长度"""
        return Node.count

    def is_empty(self):
        return self._head is None

    def insert_head(self, elem):
        """双向链表的头插法"""

        node = Node(elem)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            cur = self._head
            # 找到最后一结点
            while cur.next != self._head:
                cur = cur.next

            # 首尾相连
            node.next = self._head
            cur.next = node
            self._head = node

    def show(self):
        if self.is_empty():
            print("链表为空！")
            return
        cur = self._head

        # 当有一个结点时
        while cur.next != self._head:
            print(cur.elem)
            cur = cur.next

        # 最后一个结点
        print(cur.elem)

    def insert_rear(self, item):
        """尾部插入"""

        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.next = self._head

    def insert(self, pos, elem):
        """插入三步走原则"""

        if pos<0 or pos>self.get_length():
            print("插入位置错误！")
            return
        if pos == 1:
            self.insert_head(elem)
        elif pos == self.get_length():
            self.insert_rear(elem)
        else:
            index = 1
            node = Node(elem)
            cur = self._head
            while index == pos :
                cur = cur.next
                index += 1
            node.next = cur.next
            cur.next = node

    def remove(self, elem):
        """删除指定的元素"""
        if self.is_empty():
            print("空链表！")
            return

        cur = self._head
        if cur.elem == elem:
            if cur.next != self._head:
                while cur.next != self._head:
                    cur =cur.next
                self._head = self._head.next
                cur.next = self._head
            else:
                self._head = None
        else:
            pre = self._head
            while cur.next != self._head:
                if cur.elem == elem:
                    pre.next = cur.next
                    pre = cur
                    cur = cur.next
                else:
                    pre = cur
                    cur = cur.next
            if cur.elem == elem:
                pre.next = self._head
            else:
                print("删除元素不存在！")
                return


if __name__ == "__main__":
    list = CList()
    for i in range(10):
        # print(i)
        list.insert_rear(i)
    print(list.get_length())
    list.show()
    print("*"*10)
    list.remove(100)
    list.show()