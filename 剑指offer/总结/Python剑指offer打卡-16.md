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

  