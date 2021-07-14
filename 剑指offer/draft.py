class TreeLinkNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:

    def getNextNode(self, pHead):

        if pHead.right:
            tmp_node = pHead.right
            while tmp_node:
                tmp_node = tmp_node.left
            return tmp_node
        else:
            tmp_node = pHead
            while tmp_node.parent:
                if tmp_node.parent.left == tmp_node:
                    return tmp_node.parent
                tmp_node = tmp_node.parent

        return None