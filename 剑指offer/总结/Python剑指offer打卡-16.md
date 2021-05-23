# Python剑指offer打卡-16

[toc]

## 最长递增子序列

- 问题描述

  ```
  问题描述：
      给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。子序列是
  由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
  例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
  
  示例：
  输入：nums = [0,1,0,3,2,3]
  输出：4
  
  解题方法：
  动态规划
  dp[i]表示到当前结点i所表示的子序列的长度
  dp[i] = max(dp[i], dp[j - 1])
  
  时间复杂度：O(N^2)
  空间复杂度：O(N)  dp状态的存储
  ```

- 代码

  ```python
  class Solution:
  
      def lengthOfLIS(self, nums) -> int:
  
          if not nums: return 0
          # 转移结点
          dp = [1] * len(nums)
  
          # 状态转移
          for i in range(len(nums)):
              for j in range(i):
                  if nums[j] < nums[i]:
                      dp[i] = max(dp[i], dp[j] + 1)
  
          return max(dp)
  ```


## 两数之和

- 问题描述

  ```python
  问题描述：
  	给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 
  的那两个 整数，并返回它们的数组下标。你可以假设每种输入只会对应一个答案。但是，数
  组中同一个元素在答案里不能重复出现。你可以按任意顺序返回答案。
  
  解题方法：
  方法一：暴力求解
  时间复杂度O(N^2)
  空间复杂度O(1)
  
  方法二：哈希表（空间换时间）
  时间复杂度O(N)
  空间复杂度O(N)
  
  注意：
  同一个元素不能重复出现
  [4, 4, 2, 1, 2]   target = 4
  不能出现[2, 2] or [4, 4] 应该出现[2, 4]的索引组合，index从0开始
  ```

- 代码

  ```python
  class Solution:
      def twoSum(self, nums: List[int], target: int) -> List[int]:
  	"""暴力求解"""
      
          for i in range(len(nums)):
              for j in range(i + 1, len(nums)):
                  if nums[i] + nums[j] == target:
                      return [i, j]
          
          return []
      
      def twoSum(self, nums: List[int], target: int) -> List[int]:
      	"""哈希表"""    
          
          hashtable = dict()
          for i, num in enumerate(nums):
              if target - num in hashtable:
                  return [hashtable[target - num], i]
              # {values: index}
              hashtable[nums[i]] = i
          
          return []
  ```

## 两数相加

- 问题描述

  ```
  问题描述：
      给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，
  并且每个节点只能存储一位数字。请你将两个数相加，并以相同形式返回一个表示和的
  链表。你可以假设除了数字 0 之外，这两个数都不会以 0开头。
  
  解题方法：
  进位计算
  
  复杂度：
  时间复杂度:O(max(L1, L2))
  空间复杂度O(1)
  
  注意：
  每个节点只能存储一位数值
  ```

- 代码

  图解

  ![](./imgs/78.png)

  ```python
  class ListNode:
  
      def __init__(self, val=0, next=None):
          self.val = val
          self.next = next
  
  
  class Solution:
  
      def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
  
          # 申请头结点
          dummy = cur = ListNode()
          # 进位节点
          carry = 0
          while l1 or l2:
  
              x = l1.val if l1 else 0
              y = l2.val if l2 else 0
              # 存储节点值
              sum = x + y + carry
              cur.next = ListNode(sum % 10)
              carry = sum // 10
              cur = cur.next
  
              # 更新节点
              if l1: l1 = l1.next
              if l2: l2 = l2.next
  
          if carry: cur.next = ListNode(carry)
  
          return dummy.next
  ```


## 三数之和

- 问题描述

  ```
  问题描述：
  给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？
  请你找出所有和为 0 且不重复的三元组。
  
  解题方法:
  （1）暴力求解
  时间复杂度：O(N^3)
  （2）二分法查找
  需要消除重复值：固定点消除，子区间内消除
  时间复杂度：O(N^2)
  
  注意：
  返回的list中不能含有重复的列表值
  如 [-1, 1, 0] [1, 0, -1]
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/3sum/solution/suan-fa-si-wei-yang-cheng-ji-er-fen-cha-5bk43/)）

  图解
  
  说明在二分法中求和，需要注意在left 和 right 的移动中要消去重复出现的值，而在外层固定值i 的变换中要消去i领域内的重复值。 
  
  ![](./imgs/79.png)
  
  ```python
  import numpy as np
  
  class Solution:
      
      def threeSum(self, nums: List[int]) -> List[List[int]]:
  
          res = []
          nums = sorted(nums)
          for i in range(len(nums)):
              for j in range(i + 1, len(nums)):
                  for k in range(j + 1, len(nums)):
                      if nums[i] + nums[j] + nums[k] == 0:
                          res.append([nums[i], nums[j], nums[k]])
          
          return np.unique(np.array(res), axis = 0).tolist()
      
      def threeSum(self, nums: List[int]) -> List[List[int]]:
  
          nums.sort()
          res = []
  
          for i in range(len(nums) - 2):
              # 三正数相加不能为零
              if nums[i] > 0: break
              if i > 0 and nums[i] == nums[i - 1]: continue
              # 固定当前值
              target = -nums[i]
              # 二分算法
              left, right = i + 1, len(nums) - 1
              while left < right:
                  if target == nums[left] + nums[right]:
                      res.append([nums[i], nums[left], nums[right]])
                      # 更新边界
                      left += 1
                      right -= 1
                      while left < right and nums[left] == nums[left - 1]:
                          left += 1
                      while left < right and nums[right] == nums[right + 1]:
                          right -= 1
                  elif target > nums[left] + nums[right]:
                      left += 1
                  else:
                      right -= 1
          return res
  
  ```

## 无重复字符的最长子串

- 问题描述

  ```
  问题描述：
  给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
  
  解题方法：
  滑动窗口
  时间复杂度：O(n)
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-by-powcai/)）

  图解:窗口内无重复数值

  ![](./imgs/80.png)

  ```python
  class Solution:
      def lengthOfLongestSubstring(self, s: str) -> int:
  
          if not s: return 0
          # left 记录窗口左边界索引值
          left, max_len, cur_len = 0, 0, 0
          look_up = set()
  
          for i in range(len(s)):
              cur_len += 1
              # 循环判断，直到左边界唯一
              while s[i] in look_up:
                  look_up.remove(s[left])
                  left += 1
                  cur_len -= 1
              # 记录字符串最长长度
              if cur_len > max_len: max_len = cur_len
              look_up.add(s[i])
  
          return max_len
  ```
