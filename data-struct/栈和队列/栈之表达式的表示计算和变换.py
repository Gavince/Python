class Stack:
    """
    创建一个顺序栈
    """
    def __init__(self):
        self._elem = []

    def push(self, elem):
        """压栈"""
        self._elem.append(elem)

    def depth(self):
        """栈长"""
        return len(self._elem)

    def pop(self):
        """出栈"""
        if self.depth() == 0:
            print("栈空！")
        else:
            return self._elem.pop()

    def top(self):
        """查看栈中的元素"""
        if self.depth() == 0:
            print("空栈！")
        else:
            return self._elem[-1]


def suf_exp_evaluator(exp):
    """后缀表达式的计算"""
    st = Stack()
    operations = "*-+/"

    for op in exp:
        if op not in operations:  # 表示运算对象
            op = int(op)
            st.push(op)
            continue

        if st.depth() < 2:
            raise SyntaxError("Short of error!!")

        a = st.pop()
        b = st.pop()
        #  分类讨论运算规则
        if op == "+":
            c = a + b
        elif op == "-":
            c = b - a
        elif op == "*":
            c = b * a
        elif op == "/":
            c = b / a
        else:
            break
        st.push(c)

    if st.depth() == 1:
        return st.pop()
    raise SyntaxError("Extra Syntax!")


if __name__ == "__main__":
    while True:
        try:
            exp = input("Suffix Expression：")
            exp = exp.split()
            print(exp)
            print(suf_exp_evaluator(exp))
        except Exception as ex:
            print("Error Type:{}, Detail:{}:".format(type(ex), ex.args))











