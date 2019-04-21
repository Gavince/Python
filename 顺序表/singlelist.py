class LNode(object):
    """
    创建节点
    """
    count = 0#用来计算所创建的单链表节点

    def __init__(self, elem):
        self.elem = elem
        self.next = None
        LNode.count += 1


class Singlelist(object):
    """创建一个单链表"""

    def __init__(self):
        self._head = LNode(None)#初始化头结点

    def initList(self, data):
        """连接单链表"""
        self._head = LNode(data[0])#头结点
        p = self._head

        #注入元素值
        for i in data[1:]:
            node = LNode(i)#创建一个新的节点
            p.next = node#连接节点
            p = p.next #移动节点

    def IsEmpty(self):
        """判断是否为空"""
        p = self._head

        if p.next is None:
            print("Enpty List")
            return 1

        else:
            return 0

    def GetLength(self):
        """长度"""
        if self.IsEmpty():
            print("None : 0")
            return 0

        p = self._head
        num = 0 #计算节点的数量
        while p:
            num += 1
            p = p.next

        return num

    def ReadList(self):
        """显示数据"""

        if self.IsEmpty():
            return 0

        p = self._head
        print("列表元素:", end="")
        while p:
            print(p.elem, end=' ')
            p = p.next

        print('')

    def InsertNode(self, i, num):
        """在指定位置插入元素"""
        print(i)
        if i > self.GetLength():
            print("无法插入！")
            exit(0)
        #寻找节点
        p = self._head
        index = 0 #索引
        while index < i:
            p = p.next
            index += 1

        Node = LNode(num)
        Node.next = p.next
        p.next = Node

    def DelNode(self, i):
        """删除指定的节点"""

        if i > self.GetLength():
            print("删除失败！")
            exit(0)

        #查找删除位置
        index = 0
        p = self._head

        while index < i:

            index += 1
            pre = p #保存上一个节点
            p = p.next

        pre.next = p.next

    def Reverse(self):
        """翻转链表"""

        p =self._head
        self._head = None
        while p:
            q = p
            p = p.next
            q.next = self._head
            self._head = q
        print("显示翻转列表")


if __name__ == "__main__":
    #数据
    data = [0, 1, 2 , 3 , 4]
    node = Singlelist()
    node.initList(data)
    node.IsEmpty()
    node.GetLength()
    node.ReadList()
    node.InsertNode(2, 45)
    node.ReadList()
    node.DelNode(3)
    node.ReadList()
    node.Reverse()
    node.ReadList()

