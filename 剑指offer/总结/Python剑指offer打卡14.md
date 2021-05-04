# Python剑指offer打卡14

[toc]

## 最长不含重复字符的子字符串

### leetcode

注意：输入为字符串

- 问题描述

  ```
  问题描述：
  请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
  
  实例：
  输入: "abcabcbb"
  输出: 3 
  解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
  
  注意：
  最长不含重复子串的长度
  ```

- 代码

  ```python
  class Solution:
      def lengthOfLongestSubstring(self, s: str) -> int:
          dic = {}
          res = tmp = 0
          for j in range(len(s)):
              i = dic.get(s[j], -1) # 获取索引 i
              dic[s[j]] = j # 更新哈希表
              tmp = tmp + 1 if tmp < j - i else j - i # dp[j - 1] -> dp[j]
              res = max(res, tmp) 
          return res
  ```
  

### 牛客网（最长无重复子串）

说明：输入为int型的list

- 问题描述

  ```
  问题描述：
  给定一个数组arr，返回arr的最长无的重复子串的长度(无重复指的是所有数字都不相同)。
  
  实例：
  输入：
  [2, 3, 4, 5]
  输出：
  ４
  ```

- 代码

  ```python
  class Solution:
      def maxLength(self , arr ):
          # write code here
          dic = {}
          res = tmp = 0
          for j in range(len(arr)):
              i = dic.get(str(arr[j]), -1)  # 获取i索引，最近重复字符，默认-1填充
              dic[str(arr[j])] = j  # 更新索引
              tmp = tmp + 1 if tmp < j - i else j - i
              res = max(res, tmp)
              
          return res
  ```

  

  

