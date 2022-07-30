class Node:
    """队结点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class LQueue:
    """
    链表队列
    遵循先进后出原则
    """

    def __init__(self):
        self.head = None
        self.tail = None #尾部指针

    def is_empty(self):
        """判断空"""
        return self.head is None

    def enqueue(self, e):
        """入队"""
        if self.is_empty():
            self.tail = Node(e)
            self.head = self.tail
            return
        # 更新节点
        self.tail.next = Node(e)
        self.tail = self.tail.next

    def unqueue(self):
        """出队"""

        if self.is_empty():
            return

        e = self.head.elem
        self.head = self.head.next

        return e

    def peek(self):
        """查看顶部元素"""

        if self.is_empty():
            return

        return self.head.elem

    def show(self):
        """显示化队列"""

        queue = []
        if self.is_empty():
            print("空队列！")
        cur = self.head
        while cur:
            queue.append(cur.elem)
            cur = cur.next

        print("队列：", queue)


if __name__ == "__main__":
    queue = LQueue()
    for i in range(12):
        queue.enqueue(i)
    queue.show()
    for i in range(11):

        queue.unqueue()
    queue.show()
    queue.enqueue(4)
    queue.show()
