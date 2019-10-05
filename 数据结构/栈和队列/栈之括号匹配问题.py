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


def check_parents(text):
    """检查括号"""
    parents = "()[]{}"
    open_parents = "([{"
    opposite = {")": "(", "]": "[", "}": "{"}

    def parentheses(text):
        i, text_len = 0, len(text)

        # 遍历字符
        while True:
            while i < text_len and text[i] not in parents:
                i += 1
            if i >= text_len:
                return
            yield text[i], i  # 弹出括号
            i += 1  # 保证数据继续向后遍历

    st = SStack()  # 创建一个顺序栈对象

    for pr, i in parentheses(text):
        print(pr, i)
        if pr in open_parents:
            st.push(pr)
            st.show()
        elif st.pop() != opposite[pr]:
            print("存在不匹配的括号!!!")
            st.show()
            return False
    st.show()
    print("所有括号匹配正确!")
    return True


if __name__ == "__main__":
    text = "{[sahdashd()j][dasj，，，，dk(sdadas)]}"
    check_parents(text)
