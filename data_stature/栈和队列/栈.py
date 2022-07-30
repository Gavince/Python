class SStack:
    """
    创建一个栈类(原则：FILO)
    """

    def __init__(self):
        self._elems = []

    def is_empty(self):
        """判断空"""
        return self._elems == []

    def top(self):
        """显示最后一个元素"""
        if self.is_empty():
            print("栈空！！！")
        else:
            return self._elems[-1]

    def push(self, elem):
        """添加元素"""
        self._elems.append(elem)

    def pop(self):
        """删除元素"""
        if self.is_empty():
            print("栈空！！！")
        else:
            return self._elems.pop()  # 默认pop出栈底元素

    def show(self):
        print("SStack :", self._elems)


class Node:
    """
    链表结点
    """

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class LStack:
    """
    创建一个链表栈(原则：FILO)
    """

    def __init__(self):
        self._top = None

    def is_empty(self):
        """判断空"""
        return self._top is None

    def pop(self):
        """表头删除栈顶元素()"""
        if self.is_empty():
            print("空栈！！！")
        else:
            self._top = self._top.next

    def top(self):
        """查看栈顶结点"""
        if self.is_empty():
            print("空栈！！！")
        else:
            return self._top.elem

    def push(self, elem):
        """表头栈顶添加元素"""

        # 1.创建结点
        node = Node(elem)
        # 2.判断结点类型
        if self.is_empty():
            self._top = node
        else:
            node.next = self._top
            self._top = node

    def show(self):
        """显示栈"""
        stack = []

        if self.is_empty():
            print("栈空！！！")
        else:
            cur = self._top
            while cur:
                stack.append(cur.elem)
                cur = cur.next
            print("Stack :", stack)


if __name__ == "__main__":
    #  # １．顺序栈
    # sstack = SStack()
    # sstack.pop()
    # sstack.push(1)
    # sstack.push(2)
    # sstack.push(3)
    # sstack.show()
    # print("Top:",sstack.top())
    # sstack.pop()
    # sstack.show()
    #  2.链表栈
    lstack = LStack()
    lstack.push(1)
    lstack.push(2)
    lstack.push(3)
    print("Top:",lstack.top())
    lstack.show()
    lstack.pop()
    lstack.show()
    lstack.pop()
    lstack.show()


