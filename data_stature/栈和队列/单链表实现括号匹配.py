class Node:
    """栈节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class LStack:
    """创建顺序栈"""

    def __init__(self):
        """初始化栈顶指针"""
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self, elem):
        """压栈"""

        node = Node(elem)
        if self.is_empty():
            self._top = node
        else:
            node.next = self._top
            self._top = node

    def pop(self):
        """出栈"""

        if self.is_empty():
            print("空栈！！！")
            return
        pop_elem = self._top.elem
        self._top = self._top.next
        return pop_elem

    def top(self):
        """显示栈顶元素"""

        if self.is_empty():
            print("空栈！！！")
        else:
            return self._top.elem

    def get_length(self):
        """获得栈中元素"""

        stack = []
        if self.is_empty():
            return 0
        else:
            cur = self._top
            while cur:
                stack.append(cur.elem)
                cur = cur.next

        return len(stack)

    def show(self):
        """显示栈数据"""

        stack = []
        if self.is_empty():
            print("空栈！！！")
        else:
            cur = self._top
            while cur:
                stack.append(cur.elem)
                cur = cur.next
        stack.reverse()
        print("Stack is :", stack)


def check_parents(text):
    """检查括号"""
    parents = "{}[]()"
    open_parents = "{[("
    opposite = {"}": "{", "]": "[", ")": "("}

    def parentheses(text):

        i, len_text = 0, len(text)
        while True:
            while i < len_text and text[i] not in parents:
                i += 1
            if i >= len_text:
                return
            yield i, text[i]
            i += 1

    lstack = LStack()
    for i, pr in parentheses(text):
        if pr in open_parents:
            lstack.push(pr)
            lstack.show()

        elif lstack.pop() != opposite[pr]:
            print("括号不比配！")
            return

    if lstack.get_length() == len(text) or lstack.get_length() != 0:
        print("括号不匹配！")
        return

    print("括号匹配真确！")


if __name__ == "__main__":
    text = "((((((("
    check_parents(text)
