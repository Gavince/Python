class Solution:

    def fun(self, pHead):

        if pHead is None:
            return

        cur = pHead
        stack = []
        while cur:
            if cur not in stack:
                stack.append(cur)
                cur = cur.next
            else:
                return cur
        return None