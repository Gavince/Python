### 孩子们的游戏
- 问题描述

  ```python
  问题描述：
  有个游戏是这样的：首先，让小朋友们围成一个大圈。然后，随机指定一个数 m，让编号为 0 的小朋友开始报数
  。每次喊到 m-1 的那个小朋友要出列唱首歌，然后可以在礼品箱中任意的挑选礼物，并且不再回到圈中，从他的
  下一个小朋友开始，继续0…m-1报数…这样下去…直到剩下最后一个小朋友，可以不用表演，并且拿到终极大奖。请
  你试着想下，哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从 0 到 n-1 ) 如果没有小朋友，请返回 -1
  解决方案：
  递归
  ```

  **递归公式**：

  ![](./imgs/15.png)

- 代码

  ```python
  import sys
  sys.setrecursionlimit(1000000)  # 保证递归深度
  
  
  class Solution:
  
      def LastRemaining_Solution(self, n: int, m: int):
          """
          :param n:小孩数
          :param m: 指定编号
          :return:
          """
          if n < 1:
              return -1
  
          start = 0
          final = -1
          indexlist = list(range(n))  # 构造
  
          while indexlist:
              #  剔除位置
              k = (start + m - 1) % n
              n -= 1
              final = indexlist.pop(k)
              # print("final", final)
              #  删除上一元素之后，向前对其
              start = k
          return final
  
      def LastRemaining_Solution1(self, n: int, m: int):
  
          if n == 0:
              return -1
          if n == 1:
              return 0
          return (self.LastRemaining_Solution1(n - 1, m) + m) % n
  
  
  if __name__ == "__main__":
      obj = Solution()
      print(obj.LastRemaining_Solution(5, 3))
      print(obj.LastRemaining_Solution1(5, 3))
  ```

  **递归过程解析**：

  ![](./imgs/15.1.png)
### 链表中环的入口结点
- 问题描述

  ```python
  问题描述：
  给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
  
  解决方案：
  栈~
  ```

- 代码

  ```python
  class ListNode:
  
      def __init__(self, val):
          self.val = val
          self.next = None
  
  
  class Solution:
  
      def EntryNodeOfLoopCollections(self, pHead):
          """链表环中第一个入口结点"""
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
  ```


### 删除链表中的重复结点
- 问题描述

  ```python
  问题描述：
  在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
  解决方案：
  当删除重复结点时，直接遍历重复结点后，跳跃连接一前一后的结点
  前：１->1->2->3->4->5->6->6
  后：2->3->4->5
  ```

- 代码

  ```python
  class ListNode:
  
      def __init__(self, val):
          self.val = val
          self.next = None
  
  
  class Solution:
  
      def deleteDuplication(self, pHead):
          # 申请新的头结点
          new_head = ListNode(None)
          new_head.next = pHead
          pre = new_head
  
          while pHead and pHead.next:
              if pHead.val == pHead.next.val:
                  tmp = pHead.val
                  # 删除重复的结点
                  while pHead and pHead.val == tmp:
                      pHead = pHead.next
                  # 结点删除后，重新连接结点
                  pre.next = pHead
              else:
                  # 一个在前一个在后
                  pre = pHead
                  pHead = pHead.next
          return new_head.next
  
      def deleteDuplication1(self, pHead):
          """递归实现"""
  
          if pHead is None:
              return None
          if pHead.next is None:
              return pHead
          if pHead.val != pHead.next.val:
              pHead.next = self.deleteDuplication1(pHead.next)
              return pHead
          else:
              # 设置临时结点，用来删除重复数值
              tempNode = pHead
              while tempNode and tempNode.val == pHead.val:
                  tempNode = tempNode.next
              return self.deleteDuplication1(tempNode)
  
      def show(self, pHead):
  
          if pHead is None:
              return None
  
          while pHead:
              print(pHead.val, end=" ")
              pHead = pHead.next
  ```
### 数组中次数超过一半的数字
- 问题描述

  ```python
  问题描述：
  数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
  由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
  解决方案：
  1.字典{}
  ```
- 代码

  ```python
  class Solution:
  
      @staticmethod
      def MoreThanHalfNum_Solution(numbers):
  	"""字典统计重复数字"""
      
          count_dic = {}
          num_len = len(numbers)
          for item in numbers:
              if item in count_dic:
                  count_dic[item] += 1
              else:
                  count_dic[item] = 1
  
              if count_dic[item] > (num_len >> 1):
                  return item
  
          return 0
  
      @staticmethod
      def MoreThanHalfNum_Solution1(numbers):
          """基于排序算法"""
          length = len(numbers)
  
          if length == 0:
              return 0
          elif length == 1:
              return numbers[0]
          else:
              numbers.sort()
              num = numbers[int(length >> 1)]  # 中间位置的数据
              if numbers.count(num) > (length >> 1):
                  return num
              
              return 0
  ```
### 求第n个丑数
- 问题描述

  ```python
  问题描述:
  把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。
  习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
  
  首先从丑数的定义我们知道，一个丑数的因子只有2,3,5，那么丑数p = 2 ^ x * 3 ^ y * 5 ^ z，
  换句话说一个丑数一定由另一个丑数乘以2或者乘以3或者乘以5得到，那么我们从1开始乘以2,3,5，
  就得到2,3,5三个丑数，在从这三个丑数出发乘以2,3,5就得到4，6,10,6，9,15,10,15,25九个丑数，
  我们发现这种方法会得到重复的丑数，而且我们题目要求第N个丑数，这样的方法得到的丑数也是无序的
  
  解决方案:
  方法1:
  [丑数](https://blog.csdn.net/ggdhs/article/details/90313512)
  方法2:
  下一个丑数，一定是由之前某一个丑数乘以2或者乘以3或者是乘以5中的最小值,动态选择最小的丑数,并不断更新.
  ```

- 代码

  ```python
  class Solution:
    def GetUglyNumber_Solution(self, index: int):
        """求取第n个丑数"""
        
        if index == 0:
            return 0
    
        # 维护一个有序的丑数数组
        array = [1] 
        Q2 = []
        Q3 = []
        Q5 = []
        i = 0
          
        while i < index:
            Q2.append(array[i] * 2)
            Q3.append(array[i] * 3)
            Q5.append(array[i] * 5)
            minval = min(Q2[0], Q3[0], Q5[0])
            array.append(minval)
            #  保证两个连续相等的值被删除
            if minval == Q2[0]:
                Q2.remove(minval)
            if minval == Q3[0]:
                Q3.remove(minval)
            if minval == Q5[0]:
                Q5.remove(minval)
            i += 1
            
        return array[i - 1]
    
    def GetUglyNumber_Solution1(self, index: int):
        """动态调整"""
    
        if index == 0:
            return 0
        res = [1]
        n2, n3, n5 = 0, 0, 0  # 记录相乘位置
        i = 0
        while i < index:
            val = min(res[n2] * 2, res[n3] * 3, res[n5] * 5)
            res.append(val)
            # 动态更新自己相乘的位置
            if res[n2] * 2 == val:
                n2 += 1
            if res[n3] * 3 == val:
                n3 += 1
            if res[n5] * 5 == val:
                n5 += 1
            i += 1
            
        return res[i - 1]
  ```

### 数组中只出现一次的数字

- 问题描述

  ```python
  问题描述:
  一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
  解决方案:
  1. 字典
  2.异或
  概念：参与运算的两个值，如果两个相应位相同，则结果为0，否则为1。即：0^0=0， 1^0=1， 0^1=1， 1^1=0
  ```

- 代码

  ```python
  class Solution:
  
      def FindNumsAppearOnce(self, array):
          """寻找只出出现一次的数字"""
  
          memories = dict()
          for val in array:
              if val not in memories:
                  memories[val] = 0  # 初始化
              memories[val] += 1
  
          result = []
          for key, item in memories.items():
              if item == 1:
                  result.append(key)
              else:
                  continue
  
          return result
  
      def FindNumsAppearOnce1(self, array):
          """异或运算"""
  
          if not array:
              return []
  
          temp = 0
          for i in array:
              temp ^= i
              
          # 寻早第一个为1的二进制位置
          index = 0
          while (temp & 1) == 0:
              temp >>= 1
              index += 1
  
          # a, b两个数组
          a = b = 0
          for i in array:
              if self.one(i, index):
                  a ^= i
              else:
                  b ^= i
          return [a, b]
  
      def one(self, data, index):
  
          data >>= index
          return data & 1
      
      
  if __name__ == "__main__":
      li = [1, 2, 2, 5, 5, 7, 1, 8, 7, 6]
      obj = Solution()
      print(obj.FindNumsAppearOnce(li))
      print(obj.FindNumsAppearOnce1([1, 2, 2, 5, 5, 7, 1, 8, 7, 6]))
  ```


### 参考

[丑数](https://blog.csdn.net/ggdhs/article/details/90313512)

[VISUALIZE CODE EXECUTION](http://www.pythontutor.com/)

[数据结构与算法题目](https://blog.csdn.net/storyfull/category_9475477_2.html)

[剑指offer（python）](https://blog.csdn.net/ggdhs/category_8914921.html)