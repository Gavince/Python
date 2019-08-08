class LNode(object):
    """
    create a INode
    """
    count = 0

    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_
        LNode.count += 1


head = LNode(454)
q = head

for i in range(1, 11):
    q.next = LNode(i)  # 创建新节点
    q = q.next

q = head  # 找到头结点
while q:
    print("*****")
    print("Head elem:", q.elem)
    q = q.next

print("Objection number is :", LNode.count)
