### 旋转数组中的最小数字

- 问题描述

  ```python
  问题描述：
  把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
  例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0
  
  解决方案:
  1. 暴力搜索
  2. 二分法
  ```

- 代码

  ```python
  class Solution:
  
      def find_num(self, RotateArray):
  
          # 条件1：数组大小为空，返回0
          if not RotateArray:
              return 0
  
          if len(RotateArray) == 1:
              return RotateArray[0]
  
          left = 0
          right = len(RotateArray) - 1
  
          while left <= right:
              middle = (right + left) // 2
              # 真值比左面小，则表示找到相应的数值
              if RotateArray[middle] < RotateArray[middle - 1]:
                  return RotateArray[middle]
              # 中值小于右面, 其值在左面
              elif RotateArray[middle] < RotateArray[right]:
                  right = middle - 1
              else:
                  left = middle + 1
  
          return 0
  ```

  测试样例：

  ```python
  obj = Solution()
  Rl1 = [2, 3, 4, 5, 1]
  Rl2 = [3, 4, 5, 1, 2]
  Rl3 = [4, 5, 1, 2, 3]
  Rl4 = [5, 1, 2, 3, 4]
  print(obj.find_num(Rl1))
  print(obj.find_num(Rl2))
  print(obj.find_num(Rl3))
  print(obj.find_num(Rl4))
  print(obj.find_num([5, 2, 4]))
  print(obj.find_num([5, 1]))
  print(obj.find_num([5]))
  print(obj.find_num([4, 5, 5, 1, 1, 2, 3]))
  ```

  测试结果:

  ```python
  1 1 1 1 2 1 5 1 
  ```

###  调整顺序使得奇数位于前面

- 问题描述

  ```python
  问题描述：
  输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
  所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
  
  解决方案：
  1. 暴力遍历
  2. sorted
  3.冒泡排序分类
  ```

- 代码

  ```python
  class Solution:
  
      def fun1(self, array):
          """奇数在前，偶数在后，相对位置保持不变"""
          new_arry = []
  
          for i in range(len(array)):
              if array[i] & 1 == 1:  # 二进制与操作，奇数（***1(奇数) & 0001 = 0001）
                  new_arry.append(array[i])
          for j in range(len(array)):
              if array[j] & 1 == 0:
                  new_arry.append(array[j])
  
          return new_arry
  
      def fun2(self, array):
  
          # sorted 默认降序排列
          return sorted(array, key=lambda x:x%2, reverse=True)
  
      def fun3(self, array):
          """冒泡排序"""
          
          for i in range(len(array)-1):
              flag = False
              for j in range(len(array)-1-i):
                  if array[j]%2 == 0 and array[j+1]%2 == 1:
                      array[j], array[j+1] = array[j+1], array[j]
                      flag = True
                  if flag is False:
                      break
                      
          return array
  ```

### 包含min函数的栈

- 问题描述

  ```python
  问题描述：
  定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O(1))
  解决方案：
  1.构建一个和原栈相同的大小的保存最小值的序列
  2.合理利用存储
  list : 6 7 5 8 4
  min  : 6   5   4
  ```

- 代码

  ```python
  class Solution:
  
      def __init__(self):
  
          self.stack = []
          self.min_values = []  # 存储最小栈元素
  
      def pop(self):
  
          if not self.stack:
              return None
  
          if self.stack[-1] == self.min_values[-1]:
              self.min_values.pop()
  
          return self.stack.pop()
  
      def push(self, val):
  
          self.stack.append(val)
  
          if self.min_values:
              #  是否为当前最小元素
              if self.min_values[-1] >= val:
                  self.min_values.append(val)
          else:
              self.min_values.append(val)
  
      def min(self):
  
          if not self.min_values:
              return None
          else:
              return self.min_values[-1]
  
      def top(self):
  
          if not self.stack:
              return None
          return self.stack[-1]
  ```

###　判断一个序列是否为该栈的弹出序列

- 问题描述

  ```python
  问题描述：
      输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等
  。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的
  弹出序列。（注意：这两个序列的长度是相等的）
  
  解决方案：
  使用栈来作为临时的变换
  Eg:
  1 2 3 4 5
  4 5 3 2 1(可行)
  4 5 3 1 2(元素1不可行, 不满足栈的性质)
  ```

- 代码

  ```python
  class Solution:
  
      def find_seq_exist(self, push_value, pop_values):
          """判断序列"""
  
          if not push_value or len(pop_values) == len(push_value):
              return None
  
          stack = []
          index = 0
          for item in push_value:
              stack.append(item)
              while stack and stack[-1] == pop_values[index]:
                  stack.pop()
                  index += 1
  
          return True if stack == [] else False
  ```

### 从尾到头打印链表

- 问题描述

  ```python
  问题描述：
  输入一个链表，按链表从尾到头的顺序返回一个ArrayList
  
  解决方案：
  1. 使用列表存储结点，并翻转
  2. 栈
  3. 递归
  fun(node.next) + [node.val]
  [] + [8] + [7] + [5]
  [8, 7, 5]
  ```

- 代码

  ```python
  # 版本一
  class Solution:
  
      @staticmethod
      def PrintListFromTailToHead(listNode):
          if not listNode:
              return []
  
          result = []
          while listNode:
              result.append(listNode.val)
              listNode = listNode.next
  
          result.reverse()
  
          return result
  
  
  # 版本二
  class Solution1:
  
      @staticmethod
      def PrintListFromTailToHead(listNode):
  
          if not listNode:
              return []
  
          stack = []  # 栈
          result = []
  
          while listNode:
              stack.append(listNode.val)
              listNode = listNode.next
          while stack:
              result.append(stack.pop())
  
          return result
  
  
  # 版本三(递归)
  class Sulution2:
  
      def PrintListFromTailToHead(self, listNode):
          
          if not listNode:
              return []
  
          return self.PrintListFromTailToHead(listNode.next) + [listNode.val]
  ```

### 参考

[数据结构与算法题目](https://blog.csdn.net/storyfull/category_9475477_2.html)

[剑指offer（python）](https://blog.csdn.net/ggdhs/category_8914921.html)

[旋转数组的通用解决办法](https://zhuanlan.zhihu.com/p/136849860)