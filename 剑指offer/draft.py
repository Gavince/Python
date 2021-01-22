class Solution:

    def FindFristCommonNode(self, head1, head2):

        if head1 is None or head2 is None:
            return None

        p1 = head1
        p2 = head2

        while p1!=p2:
            p1 = head2 if p1 is None else p1.next
            p2 = head1 if p2 is None else p2.next

        return p1

    def FindFristCommonNode1(self, phead1, phead2):

        if phead1 is None or phead2 is None:
            return None

        stack1 = []
        stack2 = []

        while phead1:
            stack1.append(phead1)
            phead1 = phead1.next

        while phead2:
            stack2.append(phead2)
            phead2 = phead2.next

        while stack1 and stack2 and stack1[-1] == stack2[-1]:
            res = stack1.pop()
            stack2.pop()
        return res