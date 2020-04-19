class DLNode:
    """
    定义双向链表的结点
    """

    def __init__(self, elem, ):
        self.elem = elem
        self.next = None
        self.prev = None


class DLList:
    """
    创建双向链表
    """

    def __init__(self):

        self._head = None  # 定义头结点

    def is_empty(self):
        """是否为空"""

        return self._head is None

    def get_length(self):
        """获得链表的长度"""

        if self.is_empty():
            # print("链表为空！")
            return 0
        count = 0
        cur = self._head
        while cur:
            count += 1
            cur = cur.next
        return count

    def show(self):
        """输出双向链表的结点元素"""

        if self.is_empty():
            print("空链表")
            return
        cur = self._head
        while cur:
            print("当前结点的元素值：", cur.elem)
            cur = cur.next

    def add_head(self, elem):
        """头插法"""

        # 1.创建结点
        node = DLNode(elem=elem)
        #  2.链表为空
        if self.is_empty():
            self._head = node
        #  3.链表不为空
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node  # 4.定义新的头结点

    def append(self, elem):
        """尾插法"""

        # 1.创建结点
        node = DLNode(elem=elem)
        # 2.链表为空
        if self.is_empty():
            self._head = node
        #  3.链表不为空
        else:
            cur = self._head
            while cur.next:
                cur = cur.next

            # 4. 尾部插入数据
            cur.next = node
            node.prev = cur

    def insert(self, pos, elem):
        """指定位置插入数据"""

        if pos > self.get_length():
            print("非法位置插入数据！！！")
            return
        #  1.判断特殊条件
        if pos == 1:
            self.add_head(elem)
        elif pos == self.get_length():
            self.append(elem)
        else:
            node = DLNode(elem)
            cur = self._head
            while pos and cur.next:
                pos -= 1
                cur = cur.next
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def search(self, elem):
        """查找某个元素"""

        if self.is_empty():
            print("空链表，请先输入数据！")
            return
        else:
            cur = self._head
            index = 0
            pos = []  # 记录查找数值在链表中的位置

            while cur:
                index += 1  # 记录位置
                if cur.elem == elem:
                    pos.append(index)
                cur = cur.next
            if len(pos) == 0:
                print("未查找到指定元素！")
            else:
                print("数据所处于的位置：", pos)

    def del_node(self, elem):
        """删除指定元素"""


        flag = 0  # 记录删除点元素
        if self.is_empty():
            print("空链表，请先输入数据！")
            return

        cur = self._head
        #  1. 判断头结点
        if cur.elem == elem:
            if cur.next is None:
                self._head = None
            else:  # 2.TODO 这有点问题
                self._head = cur.next
                self._head.prev = None
        else:
            while cur.next:
                #  3.删除中间节点
                if cur.elem == elem:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    flag += 1
                #  4.最后一个结点删除
                cur = cur.next

            if cur.elem == elem:
                cur.prev.next = None  # 指向为空
                cur.prev = None
                flag += 1
            if flag == 0:
                print("所删除的元素不在链表中！")


class TestModule:
    """
    测试类
    """

    def __init__(self, list1=None):
        self.list1 = list1

    def test_add(self, list1=None):
        """测试添加操作"""

        self.list1.add_head(478)
        self.list1.add_head(465)
        self.list1.add_head(45)
        self.list1.append(78)
        self.list1.append(12)
        self.list1.append(79)
        self.list1.show()

    def test_del(self):
        """测试删除操作"""
        print("原始数据:")
        self.list1.show()
        print("--" * 10)

        print("首部删除元素：")
        self.list1.del_node(45)
        self.list1.show()
        print("--" * 10)

        print("中间删除元素：")
        self.list1.del_node(78)
        self.list1.show()

        print("--" * 10)
        print("尾部删除元素：")
        self.list1.del_node(79)
        self.list1.show()

        print("--" * 10)
        print("删除不存在的元素：")
        self.list1.del_node(1212)
        print("--" * 10)
        self.list1.show()

    def test_insert(self):
        """测试插入操作"""

        print("原始数据:")
        self.list1.show()
        print("--" * 10)

        print("首部添加元素：")
        self.list1.insert(1, 100)
        self.list1.show()
        print("--" * 10)

        print("中间添加元素：")
        self.list1.insert(4, 456456)
        self.list1.show()

        print("--" * 10)
        print("尾部添加元素：")
        index = self.list1.get_length()
        self.list1.insert(index, 11111)
        self.list1.show()

        print("--" * 10)
        print("非法位置添加元素：")
        self.list1.insert(1111, 1212)
        self.list1.show()


if __name__ == "__main__":
    dllist = DLList()
    test = TestModule(dllist)
    print("测试添加模块：")
    test.test_add()

    # print("--"*10)
    # print("测试插入模块：")
    # test.test_insert()

    print("--" * 10)
    print("测试删除模块：")
    test.test_del()
