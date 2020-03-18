class DLNode:
    """双向链表的结点"""
    count = 0

    def __init__(self, elem):
        self.item = elem
        self.prev = None
        self.next = None
        DLNode.count += 1


class DLink:
    """双向循环链表"""
    def __init__(self):
        self._head = None

    def remove(self):
        pass

    def add_head(self, elem):
        # 头插法
        node = DLNode(elem)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def add_tail(self, elem):
        """尾插法"""
        node = DLNode(elem)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, index, elem):
        node = DLNode(elem)
        if index<0 or index > self.get_length():
            print("索引错误！")
            return
        if index == 1:
            self.add_head(elem)
        elif index == self.get_length():
            self.add_tail(elem)
        else:
            i = 1
            cur = self._head
            p = None
            while i < index:
                i += 1
                p = cur
                cur = cur.next
            node.next = cur
            cur.prev = node
            node.prev = p
            p.next = node

    def is_empty(self):
        return self._head is None

    def get_length(self):
        return DLNode.count

    def show(self):
        """输出数据"""
        if self.is_empty():
            print("空！")
        else:
            cur = self._head
            while cur:
                print(cur.item)
                cur = cur.next


if __name__ == "__main__":
    link = DLink()
    for i in range(10):
        link.add_head(i)
    for i in range(10, 20):
        link.add_tail(i)
    link.insert(1, 100)
    link.insert(23, 10440)
    print(link.get_length())
    link.show()