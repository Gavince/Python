class LNode(object):
    """
    创建节点
    """
    count = 0
    def __init__(self, elem):
        """

        :param elem:
        """
        self.elem = elem
        self.next = None
        LNode.count += 1


class Singlelist(object):
    """
    操作单链表
    """
    def init_list(self, data):
        self.head = LNode(data[0])
        p = self.head

        for i in data[1:]:
            node = LNode(i);
            p.next = node #链接新的节点
            p = p.next

    def is_empty(self):

        p = self.head

        if p.next is None:

            print("Empty")
            return 1
        else:
            return 0

    def get_length(self):

        p = self.head
        num = 0
        if(self.is_empty()):
            while p:
                num +=1
                p = p.next
        print("lengh is :"%num)

    def show(self):

        p = self.head
        if(self.is_empty()):
            while p:
                print("p.elem = "% p.elem)
                p = p.next
        else:
            print("列表为空！")

    def insert_node(self, i, num):

        if i > self.get_length():
            print("不能插入元素！")
            exit(0)

        p = self.head
        index = 0 #z做为索引节点

        #找节点位置
        while index < i:
            p = p.next
            index += 1

        #创建节点
        Node = LNode(num)
        Node.next = p.next
        p.next = Node

    def del_node(self, i):

        if i > self.get_length():
            print("删除失败！")
            exit(0)

        # 查找删除位置
        index = 0
        p = self._head
        while index < i:

            index += 1
            pre = p
            p = p.next
        pre.next = p.next#去除中间的一个节点删去主要的节点

    def reverse(self):

        p = self.head
        self._head = None
        while p:
            q = p
            p = p.next
            q.next = self._head
        print("显示")


if __name__ == "__main__":
    # 数据
    data = [0, 1, 2, 3, 4]
    node = Singlelist()
    node.init_list(data)
    node.is_empty()
    node.get_length()
    node.read_list()
    node.insert_node(2, 45)
    node.read_list()
    node.del_node(3)
    node.read_list()
    node.reverse()
    node.read_list()


