class Node:
    """
    定义node节点
    """
    # 记录创建的节点数目
    count = 0

    def __init__(self, elem):
        self.elem = elem
        self.next = None
        Node.count += 1

    def __del__(self):
        Node.count -= 1


class CSlist:
    """
    创建循环单链表
    """

    def __init__(self):
        self.__head = None

    def is_empty(self):
        """判断空"""
        return self.__head is None

    @staticmethod
    def get_length():
        """获得数据的长度"""
        print("创建的数据节点数目为：", Node.count)
        return Node.count

    def add_head(self, elem):
        """头插法"""

        #  1. 申请插入节点
        node = Node(elem)

        #  2. 判断是否只有头结点
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            cur = self.__head
            #  3.找到链表的结尾
            while cur.next != self.__head:
                cur = cur.next
            #  4. 插入node 节点
            node.next = self.__head
            cur.next = node
            self.__head = node  # 重新找到头结点

    def del_data(self, elem):
        """删除指定数据的节点"""

        #  1. 判断是否为节点
        if self.is_empty():
            print("请先添加数据！！！")
            return
        # 寻找指定数据的节点
        cur = self.__head
        if cur.elem == elem:
            #  2.0 直接在第一次就找到了数据节点
            #  此时先要删除头结点
            #  2.1判断数据是否只有头结点
            if cur.next != self.__head:
                # 2.2 第一个节点非空
                while cur.next != self.__head:
                    cur = cur.next
                #  2.3 删除节点
                self.__head = self.__head.next
                cur.next = self.__head
            else:
                self.__head = None
        else:
            # 3.0 在中间找到元素节点和尾部找到节点
            # 3.1 遍历
            pre = self.__head
            while cur.next != self.__head:
                if cur.elem == elem:
                    pre.next = cur.next
                    #  继续寻找下一个可以删除的结点
                    pre = cur
                    cur = cur.next
                else:
                    pre = cur
                    cur = cur.next
            # 3.2 此时退出层循环,在尾部查找数据
            if cur.elem == elem:
                pre.next = self.__head
            else:
                print("所查找的数据未存入！！！")
                return

    def add_rear(self, elem):
        """尾插法"""
        #  1. 申请节点
        node = Node(elem)

        #  2.判断节点是否为单一节点
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def travel(self):
        """遍历整个链表"""

        #  1.判断是否为空节点
        if self.is_empty():
            print("空链表！")
            return 0
        #  2. 设置遍历指针
        cur = self.__head
        while cur.next != self.__head:  # 保证遍历不会进入死循环
            print("Current data is :", cur.elem)
            cur = cur.next
        print("Current data is :", cur.elem)  # 输出最后一个结点元素

    def insert_data(self, pos, elem):
        """插入数据"""

        #  0.判断插入位置是否合法
        index = self.get_length()
        if (pos < 1) or (int(pos) > index):
            print("插入位置错误！")
            return

        #  1.插入点在链表的开头（头插法）
        if pos == 1:
            self.add_head(elem)

        #  2.插入点在链表的末尾（尾插法）
        elif pos == (self.get_length()):
            self.add_rear(elem)

        #  3.插入点在链表的中间
        else:
            cur = self.__head
            node = Node(elem)

            # 3.1 查找指点位置
            while pos:
                pos -= 1
                cur = cur.next

            # 3.2 插入节点
            node.next = cur.next
            cur.next = node


class TestModule:
    """
    测试模块
    """

    def test_add(self):
        """测试插入模块"""

        print("插入数据显示：")
        clist.add_head(12)
        clist.add_head(45)
        clist.add_head(455)
        clist.add_rear(100)
        clist.add_rear(45)
        clist.travel()

    def test_del(self):
        """测试删除模块"""

        print("原始数据：")
        clist.travel()
        clist.del_data(45)
        print("删除指定元素（45）：")
        clist.travel()
        print("删除第一个结点元素：")
        clist.del_data(455)
        clist.travel()
        print("删除最后一个结点元素：")
        clist.del_data(100)
        clist.travel()
        print("删除链表最后一个元素：")
        clist.del_data(12)
        clist.travel()


if __name__ == "__main__":
    clist = CSlist()
    test = TestModule()
    test.test_add()
    test.test_del()

