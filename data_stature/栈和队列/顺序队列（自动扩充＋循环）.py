class SQueue:
    """
    自定义一个列表类
    遵循原则：先进先出
    """

    def __init__(self, init_len=8):
        """初始化队列参数"""

        self._len = init_len
        self._elems = [0]*self._len  # 初始化队列
        self._head = 0  # 记录队头位置
        self._num = 0 # 记录先存元素的数据

    def is_empty(self):
        """判断为空"""

        return self._num == 0

    def peek(self):
        """查看队列头部元素"""

        if self.is_empty():
            print("空队列！")
            return
        return self._elems[self._head]

    def unqueue(self):
        """出队"""

        if self.is_empty():
            return
        e = self._elems[self._head]
        self._head = (self._head + 1)%self._len  # 更新头部位置
        self._num -= 1
        return e

    def enqueue(self, e):
        """入队"""
        if self._len == self._num:  # 此时需要扩充队的存储大小
            self.__expand()
        self._elems[(self._head + self._num)%self._len] = e
        self._num += 1

    def __expand(self):
        """扩充存储"""
        # 1.保存就得存储数据
        old_len = self._len
        self._len *= 2
        new_elems = [0]*self._len
        #  2.转移数据
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head+i)%old_len]

        self._elems, self._head = new_elems, 0

    def show(self):
        print("Queeze",self._elems)


if __name__ == "__main__":
    queue = SQueue()
    print(SQueue.__dict__)
    # queue.enqueeze(1)
    queue.show()
    for i in range(8):
        queue.enqueue(i)
    queue.show()
    queue.unqueue()
    queue.unqueue()
    queue.unqueue()
    queue.show()


    queue.enqueue(100)
    queue.show()
    queue.enqueue(1212)
    queue.show()
    queue.enqueue(1414)
    queue.show()
    queue.enqueue(1515)
    queue.show()






