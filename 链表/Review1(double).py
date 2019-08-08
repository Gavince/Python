class Node(object):
    """创建一个双线链表的节点"""

    def __init__(self, elem):
        self.elem = elem
        self.prev = None
        self.next = None


class DList(object):

    def __init__(self):
        #初始化双链表
        self.__head = Node(None)#此时头尾指针不初始化数据(注意此时的数据存储为None)
        self.__tail = Node(None)
        self.__head.next = self.__tail#实现头尾指针相互指向
        self.__tail.prev = self.__head

    def GetLength(self):
        """获得链表的长度"""
        cur = self.__head
        self.count = 0
        while cur.next != self.__tail:
            self.count += 1
            cur = cur.next
        if self.count == 0:
            return 0
        else:
            return self.count

    def isempty(self):
        """是否为空链表"""
        if self.GetLength():
            print("列表不空！")
        else:
            print("列表为空")

    def insert(self, elem):
        """插入节点数据"""

        #1.申请节点
        node = Node(elem)
        #2.加入链表
        node.next = self.__head.next  #头插法
        self.__head.next.prev = node

        self.__head.next = node
        node.prev = self.__head

    def display(self):
        """打印列表的数据"""

        #尾部开始查找
        p = self.__tail

        while p.prev != self.__head:

            print("数据：%d" % p.prev.elem )
            p = p.prev

    def delnode(self, elem):
        """删除节点"""

        #1.找到节点的位置
        p = self.__head.next

        while p:

            if p.elem == elem:
                # 2.删除该节点
                p.prev.next = p.next
                p.next.prev = p.prev
                break
            else:
                p = p.next

        if p is None:
            print("找不到节点")

    def clearall(self):

        """清空所有的列表的"""
        self.__head.next = self.__tail
        self.__tail.prev =self.__head

    def reverse(self):

        pass


if __name__  == "__main__":

    list1 = DList()
    list1.isempty()
    for i in range(1, 100, 40):
        list1.insert(i)
    count = list1.GetLength()
    print("count :",count)
    list1.display()
    #清空了数据
    list1.clearall()
    list1.display()
    print("此处显示了删除两个节点的数据\n")
    list1.delnode(1)
    list1.delnode(41)
    list1.delnode(81)
    list1.delnode(1)
    list1.display()