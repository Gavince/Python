# Python剑指offer + leetcode高频题目总结

## 滑动窗口最大值（<font color = red>重点</font>）

题目类型：字符串

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述：
  	给你一个整数数组 nums，有一个大小为k的滑动窗口从数组的最左侧移动到
  数组的最右侧。你只可以看到在滑动窗口内的k个数字。滑动窗口每次只向右移动一
  位。返回滑动窗口中的最大值。
  
  如：
  输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
  输出：[3,3,5,5,6,7]
  解释：
  滑动窗口的位置        最大值
  　---------------        　　-----
  [1  3  -1] -3  5  3  6  7       3
   1 [3  -1  -3] 5  3  6  7       3
   1  3 [-1  -3  5] 3  6  7       5
   1  3  -1 [-3  5  3] 6  7       5
   1  3  -1  -3 [5  3  6] 7       6
   1  3  -1  -3  5 [3  6  7]      7
   
   解题方法：
  单调队列：只需要维护有可能成为窗口里最大值的元素就可以了，同时保证队里里的元素数值是由大到小的。
  (左删除，右添加原则)
  时间复杂度：O(N)  # 总共遍历N次
  空间复杂度：O(K)  # 队列需要存储k个值
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/solution/mian-shi-ti-59-i-hua-dong-chuang-kou-de-zui-da-1-6/)）

  ```python
  import collections
  
  class Solution:
      
      def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
  
          deque = collections.deque()
          res, n = [], len(nums)
  
          # 遍历窗口
          for i, j in zip(range(1-k, n-k+1), range(n)):
  
              # 左删除
              if i > 0 and deque[0] == nums[i - 1]: deque.popleft()
              # 右添加,单调递减
              while deque and deque[-1] < nums[j]: deque.pop()
  	  # 队列头部元素最大
              deque.append(nums[j])
  
              if i >= 0:
                  res.append(deque[0])
                  
          return res 
  ```

- 代码运行

  ![](/home/gavin/Python/剑指offer/总结/imgs/46.代码运行.png)

## 全排列

题目类型：回朔法

- 问题描述

  ```
  问题描述：
          给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以
  按任意顺序返回答案。
  
  示例：
  输入：nums = [1,2,3]
  输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
  
  注意:
  1. 不存在有重复排列:[1, 2, 2] [1, 2, 2]， 因此不用考虑消除重复数组
  2. 数组的拷贝和引用：res.append(nums[:]), res.append(nums)
  ```

- 代码

  ```python
  class Solution:
  
      def permute(self, nums):
          """数组的全排列"""
  
          res = []
  
          def dfs(x):
              # 回朔满足
              if x == len(nums) - 1:
                  res.append(nums[:])
                  return
              for i in range(x, len(nums)):
                  # 交换位置
                  nums[i], nums[x] = nums[x], nums[i]
                  dfs(x + 1)
                  nums[i], nums[x] = nums[x], nums[i]
  
          dfs(0)
          return res
  ```

## 字符串的排列

- 问题描述

  ```python
  问题描述：
  输入一个字符串，打印出该字符串中字符的所有排列。
  你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
  
  实例：
  输入：s = "abc"
  输出：["abc","acb","bac","bca","cab","cba"]
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/mian-shi-ti-38-zi-fu-chuan-de-pai-lie-hui-su-fa-by/)）

  ![](/home/gavin/Python/剑指offer/总结/imgs/字符串的排列.png)

  ```python
  class Solution:
      
      def permutation(self, s: str) -> List[str]:
          
        c, res = list(s), []
          def dfs(x):
              if x == len(c) - 1:
                  res.append(''.join(c))   # 添加排列方案
                  return
              dic = set()
              for i in range(x, len(c)):
                  if c[i] in dic: continue # 重复，因此剪枝
                  dic.add(c[i])
                  c[i], c[x] = c[x], c[i]  # 交换，将 c[i] 固定在第 x 位
                  dfs(x + 1)               # 开启固定第 x + 1 位字符
                  c[i], c[x] = c[x], c[i]  # 恢复交换
          dfs(0)
          return res
  ```


## 连续子数组的最大和（<font color = red>重点</font>）

- 题目说明  

  ```
  问题描述：
  	输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求
  所有子数组的和的最大值。要求时间复杂度为O(n)。
  
  解题方法：
  动态规划
  dp[i]的长度，时间复杂度O(n)
  直接使用nums数组进行存储，空间复杂度O(1)
  ```


- 代码（[解题思路](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/solution/cong-bao-li-po-jie-dao-dong-tai-gui-hua-yfvkp/)）

  状态转移方程：
  $$
  dp[j]={ dp[j−1]+nums[j],dp[j−1]>0 \\
    dp[j]=nums[j],   dp[j−1]≤0}\\
  $$

  情况描述：

  ![](/home/gavin/Python/剑指offer/总结/imgs/36.png)

  ```python
  class Solution:
      def maxSubArray(self, nums: List[int]) -> int:
  
          for i in range(1, len(nums)):
              nums[i] += max(nums[i-1], 0)
          
          return max(nums)
  ```


##　