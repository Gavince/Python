# Python剑指offer打卡-22

[toc]

## 回文数

题目类型：回文数

- 问题描述

  ```
  问题描述:
         给你一个整数x，如果x是一个回文整数，返回true；否则，返回
  false。回文数是指正序（从左向右）和倒序（从右向左）读都是一样
  的整数。例如，121 是回文，而 123 不是。
  进阶：你能不将整数转为字符串来解决这个问题吗？
  
  解题方法:
  (1)字符串判断
  s[::-1] == s
  
  (2)求整得头　＝＝　求余得尾
  情况１：当整数为负数时，不是回文数
  eg: -121(-121和121-不相等)
  
  情况２：当整数能够被10整除，且不为０时，不是回文数
  eg: 120、112020
  
  情况3：数字长度奇偶情况下，退出原则
  while res < x:
  偶数：1221
  res: 1 12
  x:  122 12
  res == x
  奇数：121
  res: 1 12
  x: 12 1
  x = res // 10
  时间复杂度：O(N)
  空间复杂度:O(1)
  ```

- 代码

  ```python
  class Solution:
      def isPalindrome1(self, x: int) -> bool:
  
          s = str(x)
          return s == s[::-1]
  
      def isPalindrome2(self, x: int) -> bool:
  
          if x < 0 or (x % 10 == 0 and x != 0):
              return False
  
          res = 0
          while res < x:
              res = res * 10 + x % 10
              x = x // 10
  
          return x == res or x == res // 10
  ```


## 前K个高频元素

题目类型：排序

- 问题描述

  ```
  问题描述：
      给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。
  你可以按 任意顺序 返回答案。
  
  实例：
  输入: nums = [1,1,1,2,2,3], k = 2
  输出: [1,2]
  ```

- 代码

  ```python
  from typing import List
  from collections import defaultdict
  from collections import Counter
  import heapq
  
  class Solution:
  
      def topKFrequent1(self, nums, k):
          """直接排序"""
  
          count = Counter(nums)
          return [item[0] for item in count.most_common(k)]
  
      def topkFrequent(self, nums, k):
          """堆排序"""
  
          count = Counter(nums)
          hp = [(val, key) for key, val in count.items()]
          return [item[1] for item in heapq.nlargest(k, hp)]
  
      def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
          """字典计数"""
          count = defaultdict(int)
          res = []
  
          for num in nums:
              count[num] += 1
  
          for key, value in sorted(count.items(), key=lambda x: x[1], reverse=True)[:k]:
              res.append(key)
  
          return res
  
  
  if __name__ == "__main__":
      obj = Solution()
      print(obj.topKFrequent1(nums=[1, 2, 2, 5, 4, 4, 4, 4, 6], k=2))
  ```

  