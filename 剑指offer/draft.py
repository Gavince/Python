class Solution:

    def isPalindrom(self, head) -> bool:
        """翻转链表法"""
        if not head or not head.next:
            return True
        # 寻找链表的中间节点进行翻转
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next
        slow.next = None
        pre = None
        # 翻转后半段
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        while pre:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next

        return True


if __name__ == "__main__":
    obj = Solution()
    print(obj.countSubStrings("abba"))