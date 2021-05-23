# Python剑指offer打卡-17

[toc]

## 最长回文子串

回文的意思是正着念和倒着念一样，如：==上海自来水来自海上==

- 问题描述

  ```
  问题描述：
  给你一个字符串 s，找到 s 中最长的回文子串。
  
  解题方法：
  动态规划
  时间复杂度O(n^2)
  空间复杂度O(n^2)
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/)）

  图解：

  ![](./imgs/81.png)

  ```python
  class Solution:
      def longestPalindrome(self, s: str) -> str:
  
          n = len(s)
          if n < 2:
              return s
          
          # 保证最长回文
          max_len = 1
          begin = 0
          # 起始状态
          dp = [[False] * n for _ in range(n)]
          # 只有一个字符，本身为
          for i in range(n):
              dp[i][i] = True
          # 遍历可能的回文长度,起始长度为L = 2
          for L in range(2, n + 1):
              # 枚举左边界
              for i in range(n):
                  j = L + i - 1
                  if j >= n:
                      break
                  # 状态转移
                  if s[i] != s[j]:
                      dp[i][j] = False
                  else:
                      if j - i < 3:
                          dp[i][j] = True
                      else:
                          dp[i][j] = dp[i + 1][j - 1]
          
                   # 最长回文子串
                  if dp[i][j] and j - i + 1 > max_len:
                      max_len = j - i + 1
                      begin = i
          
          return s[begin: begin + max_len]
  ```

  

