class Node(object):
    """
    定义节点　
    """
    # 定义类属性,用来记录创建的结点数目
    count = 0

    def __init__(self, elem):
        self.elem = elem
        self.next = None
        Node.count += 1

    def __del__(self):
        Node.count -= 1


class LList(object):
    """
    创建单链表
    """

    def __init__(self):
        """初始化头结点"""
        self._head = Node(None)

    def init_list(self, data):
        """创建单链表"""
        self._head = Node(data[0])
        p = self._head

        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def is_empty(self):
        """判断是否为空"""
        p = self._head

        if p is None:
            print("Empty!!!")
            return 1
        else:
            return 0

    def get_length(self):
        """获得链表的长度"""
        if self.is_empty():
            print("Length is 0")
            return 0

        p = self._head
        num = 0
        while p:
            num += 1
            p = p.next
        return num

    def read_list(self):
        """读取单链表"""
        if self.is_empty():
            print("未录入数据！！！")
            return 0
        p = self._head
        while p:
            print("Elem is :", p.elem)
            p = p.next

    def insert_node(self, i, num):
        """插入数据节点"""
        if i > self.get_length():
            print("插入节点索引错误！！！")
            return 0

        # 寻找节点
        p = self._head
        index = 1
        if i == 1:
            node = Node(num)
            node.next = self._head
            self._head = node
            return 0
        else:
            while index < i:
                p = p.next
                index += 1
            # 插入节点
            node = Node(num)
            node.next = p.next
            p.next = node

    def del_node(self, i):
        """删除节点"""
        if i > self.get_length():
            print("删除索引节点错误！！！")
            return 0

        p = self._head
        index = 1
        if i == 1:
            self._head = p.next
            return 0
        else:
            while index < i:
                index += 1
                pre = p  # 保存上一个节点
                p = p.next  # 遍历数据节点
            pre.next = p.next

    def reverse(self):
        """单链表的翻转"""

        p = self._head
        self._head = None
        while p:
            q = p
            p = p.next  # 循环遍历
            q.next = self._head
            self._head = q


class TestModule():
    """测试单链表的模块"""

    def __init__(self, data=[], node=None):
        self.data = data
        self.node = node
        print("执行测试程序！")

    def test_del(self):
        """ 测试删除操作"""
        self.node.init_list(self.data)
        #  1. 测试删除模块
        print("删除前的数据：")
        self.node.read_list()
        #  1.１ 删除头节点
        self.node.del_node(1)
        print("删除头结点:")
        self.node.read_list()
        #  1.2 删除未节点
        print("删除前的数据：")
        self.node.read_list()
        print("删除尾节点：")
        self.node.del_node(4)
        self.node.read_list()
        #  1.3 删除中间节点
        print("删除前的数据：")
        self.node.read_list()
        print("删除中间节点：")
        self.node.del_node(2)
        self.node.read_list()

    def test_insert(self):
        """测试插入算法"""

        self.node.init_list(self.data)
        print("原始数据：")
        self.node.read_list()
        #  1. 头插
        print("头插：")
        self.node.insert_node(1, 100)
        self.node.read_list()
        #  2. 尾插
        print("尾插：")
        self.node.insert_node(6, 666)
        self.node.read_list()
        #  3. 指定位置插入
        print("中间插：")
        self.node.insert_node(2, 455)
        self.node.read_list()

    def test_reverse(self):
        """测试翻转模块"""
        self.node.init_list(self.data)
        print("原始数据：")
        self.node.read_list()
        self.node.reverse()
        print("数据翻转后：")
        self.node.read_list()


if __name__ == "__main__":
    #  0. 初始化数据
    data = [1, 2, 3, 4, 5]
    node = LList()

    #  1. 执行删除测试
    test = TestModule(data, node)
    # test.test_del()
    #  2. 测试插入模块
    # test.test_insert()
    #  3.测试翻转模块
    # node.init_list(data)
    # node.read_list()
    # node.reverse()
    # print("*" * 10)
    # node.read_list()

