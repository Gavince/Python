### 链表中倒数第k个结点

- 问题描述

  ```python
  问题描述：
  输入一个链表，输出该链表中倒数第k个结点
  
  解决方案：
  使用栈存储，先进后出。
  ```

- 代码

  ```python
  class Solution:
  
      @staticmethod
      def FindKthToTail(head, k):
  
          if not head or not k:
              return None
          
          node = None
          stack = []
          temp = head
          while temp:
              stack.append(temp)
              temp = temp.next
          if len(stack) >= k:  # k值限制
              for i in range(k):  # 倒数第k个结点
                  node = stack.pop()
              return node
          else:
              return None
  ```

### 链表的翻转（重点）

- 问题描述

  ```python
  问题描述：
  输入一个链表，反转链表后，输出新链表的表头
  
  解决方案：
  1. 递归
  2. 循环
  ```

- 代码

  ```python
  class ListNode:
  
      def __init__(self, val):
          self.val = val
          self.next = None
  
  
  class Solution:
  
      @staticmethod
      def reverse_list(pHead):
  
          if not pHead or pHead.next is None:
              return pHead
  
          newHead = None
          cur = pHead
          while cur:
              tmp = cur.next
              cur.next = newHead
              newHead = cur
              cur = tmp
  
          return newHead
  ```

- 样例测试

  ```python
  n1 = ListNode(1)  # 依次实例5个结点
  n2 = ListNode(2)
  n3 = ListNode(3)
  n4 = ListNode(4)
  n5 = ListNode(5)
  n1.next = n2  # 依次将结点链接起来，形成一个链表
  n2.next = n3
  n3.next = n4
  n4.next = n5
  head1, head2 = n1, n1
  print("翻转前的链表：", end=" ")
  while head1:
      print(head1.val, end=" ")
      head1 = head1.next
  
  obj = Solution()
  p = obj.reverse_list(head2)
  print("\n翻转后的链表：", end=" ")
  while p:
      print(p.val, end=" ")
      p = p.next
  ```

- 结果

  ```python
  翻转前的链表： 1 2 3 4 5 
  翻转后的链表： 5 4 3 2 1 
  ```

### 合并两个排序的链表

- 问题描述

  ```python
  问题描述：
  输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
  
  解决方案：
  1. 构建一个新的链表用于添加合并后的有序链表
  2. 递归
  ```

- 代码

  ```python
  class ListNode:
  
      def __init__(self, x):
          self.val = x
          self.next = None
  
  
  class Solution:
  
      @staticmethod
      def merge(pHead1, pHead2):
  
          if not pHead1 and not pHead2:
              return None
  
          if not pHead1:
              return pHead2
          if not pHead2:
              return pHead1
  
          # 构建新的链表
          newnode = ListNode(-1)
          temp = newnode
          p1, p2 = pHead1, pHead1
  
          while p1 and p2:
  
              if p1.val < p2.val:
                  temp.next = ListNode(p1.val)
                  temp = temp.next
                  p1 = p1.next
              else:
                  temp.next = ListNode(p2.val)
                  temp = temp.next
                  p2 = p2.next
          # 连接未遍历部分的数据
          if p1:
              temp.next = p1
          if p2:
              temp.next = p2
  
          return newnode
  ```

### 复杂链表的复制

- 问题描述

  ```python
  问题描述：
  输入一个复杂链表（每个节点中有节点值，以及两个指针，**一个指向下一个节点，另一个特殊指针指向任意一个节点**），
  返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空。
  
  解决方案：
  A---  a***  --->B  ***>b
  A.next.random = a.random.next问题描述：
  输入一个复杂链表（每个节点中有节点值，以及两个指针，**一个指向下一个节点，另一个特殊指针指向任意一个节点**），
  返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空。
  ```

- 代码

  ```python
  class RandomListNode:
  
      def __init__(self, val):
          self.val = val
          self.next = None
          self.random = None
  
  
  class Solution:
  
      def clone(self, pHead):
  
          if pHead is None:
              return None
  
          #   复制一个新的node,插入到原有的node当中，实现次序的链接的指针
          pTemp = pHead
          while pTemp:
              node = RandomListNode(pTemp.val)
              node.next = pTemp.next
              pTemp.next = node
              pTemp = node.next  # 临时头结点向下移动
  
          #   对随机指针进行复制
          pTemp = pHead
          while pTemp:
              if pTemp.random:
                  pTemp.next.random = pTemp.random.next
              pTemp = pTemp.next.next
  
          # 断开原来的链表
          pTemp = pHead
          newHead = pHead.next
          pNewTemp = pHead.next
  
          # 两个指针同时遍历，并连接自己的下一个结点
          while pTemp:
              pTemp.next = pTemp.next.next
              if pNewTemp.next:
                  pNewTemp.next = pTemp.next.next
                  pNewTemp = pNewTemp.next
              pTemp = pTemp.next
              
          return newHead
  ```

### 两个链表的第一个公共结点

<img src="./imgs/14.png" style="zoom: 67%;" />

- 问题描述

  ```python
  解决方案：
  1. 暴力搜索
  不推荐
  2.使用栈从后向前找出第一个不相等的结点
  A:1 2 5 6
  公共结点---->10 11 55 88
  B:2 4 8 9
  3. 交替遍历指针
  p1 -> --->......p1=p2
  p2 --> ---->......return p1
  实例：
  a:1 2 3 4 
  b:0 7 8 9 6 5 2
  c(公共部分): 10 10 10
  a + c + b = b + c + a
  ```

- 代码

  ```python
  class Solution:
  
      def FindFristCommonNode(self, pHead1, pHead2):
  
          res_set = {}  # 集合的无序性
          # 加入
          while pHead1:
              res_set.add(pHead1)
              pHead1 = pHead1.next
          # 对比
          while pHead2:
              if pHead2 in res_set:
                  return pHead2
              pHead2 = pHead2.next
  
      def FindFristCommonNode1(self, pHead1, pHead2):
  
          stack1 = []
          stack2 = []
          
          while pHead1:
              stack1.append(pHead1)
              pHead1 = pHead1.next
          while pHead2:
              stack2.append(pHead2)
              pHead2 = pHead2.next
          while stack1 and stack2 and stack1[-1] == stack2[-1]:
              res = stack1.pop()
              stack2.pop()
              
          return res
  
      def FindFristCommonNode2(self, pHead1, pHead2):
  
          if pHead1 is None or pHead2 is None:
              return None
          
          p1 = pHead1
          p2 = pHead2
          while p1 != p2:
              p1 = pHead2 if p1 is None else p1.next  # 遍历完p1结点遍历p2结点
              p2 = pHead1 if p2 is None else p2.next  # 遍历完p2结点遍历p1结点
              
          return p
  ```

### 参考

[数据结构与算法题目](https://blog.csdn.net/storyfull/category_9475477_2.html)

[剑指offer（python）](https://blog.csdn.net/ggdhs/category_8914921.html)

[旋转数组的通用解决办法](https://zhuanlan.zhihu.com/p/136849860)