class Stack:

    def __init__(self):
        self.stack = []
        self.min_value = []

    def pop(self):

        if not self.stack:
            return None
        if self.stack[-1] == self.min_value[-1]:
            self.min_value.pop()
        else:
            return self.stack.pop()

    def push(self, val):

        self.stack.append(val)

        if self.min_value:
            if self.min_value[-1] >= val:
                self.min_value.append(val)
        else:
            self.min_value.append(val)

    def min(self):
        if not self.stack:
            return None
        else:
            print(self.min_value)
            return self.min_value[-1]

    def top(self):

        if not self.stack:
            return None
        else:
            return self.stack[-1]


if __name__ == "__main__":
    obj = Stack()
    obj.push(6)
    obj.push(7)
    obj.push(5)
    obj.push(8)
    obj.push(4)
    obj.pop()
    obj.pop()
    obj.pop()
    obj.pop()
    obj.pop()

    print(obj.min())
