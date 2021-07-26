# Python 高频题目

[toc]

## 无重复字符的最长子串<font color=red>（重点）</font>

题目类型：字符串

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述：
  	给定一个字符串，请你找出其中不含有重复字符的 最长子串的长度。
  
  解题方法：
  滑动窗口
  两种情况下滑动窗口的移动：
  （1）[abcdef]a  ----> [bcdefa]
  （2）[bdefa]a  ----> [a]
  时间复杂度：O(N)
  空间复杂度：O(N) 使用集合临时存储了最长字符串，极端情况下需要存储N
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-by-powcai/)）

  图解:窗口内无重复数值

  ![](/home/gavin/Python/剑指offer/总结/imgs/80.png)

  ```python
  class Solution:
      def lengthOfLongestSubstring(self, s: str) -> int:
  
          if not s: return 0
          # left 记录窗口左边界索引值
          left, max_len, cur_len = 0, 0, 0
          # 集合保证了无重复性
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
    -------------------        　 -----
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

  图解算法：

  ![](/home/gavin/Python/剑指offer/总结/imgs/46.代码运行.png)

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

## 全排列（<font color = red>重点</font>）

题目类型：数组

题目难度：:star2::star2::star2::star2:

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

## 字符串的排列（<font color = red>重点</font>）

题目类型：字符串

题目难度：:star2::star2::star2::star2:

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

题目类型：数组、动态规划

题目难度：:star2::star2::star2:

- 题目说明  

  ```
  问题描述：
  	输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组
  的和的最大值。要求时间复杂度为O(n)。
  
  解题方法：
  动态规划
  (1) 状态定义： 设动态规划列表 dp ，dp[i] 代表以元素 nums[i]结尾的连续子数组最大和。
  为何定义最大和 dp[i] 中必须包含元素 nums[i]：保证 dp[i]递推到dp[i+1] 的正确性；如
  果不包含 nums[i]，递推时则不满足题目的 连续
  子数组 要求。
  (2) 转移方程： 若dp[i−1]≤0 ，说明 dp[i - 1]对 dp[i]产生负贡献，
  即 dp[i-1] + nums[i]不如 nums[i]本身大。
  当 dp[i - 1] > 0时：执行 dp[i] = dp[i-1] + nums[i]；
  当 dp[i−1]≤0 时：执行 dp[i] = nums[i]；
  (3) 初始状态： dp[0] = nums[0]，即以 nums[0]结尾的连续子数组最大和为 nums[0] 。
  (4) 返回值： 返回 dp 列表中的最大值，代表全局最大值。
  
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

## 数组中次数超过一半的数字（<font color = red>重点</font>）

题目类型：数组

题目难度：:star2::star2:

- 问题描述

  ```python
  问题描述：
  	数组中有一个数字出现的次数超过数组长度的一半，请找出
  这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于
  数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如
  果不存在则输出0。
  
  解决方案：
  1.摩尔投票法
  时间复杂度：O(N) 
  空间复杂度：O(1)
  
  注意：
  1. [1, 2, 2, 3, 3, 3, 2, 2] 此时输出结果为3, 但注意题目要求必须超
  过数组一半长度，而此时是相等。
  2. 若不存在，则需要输出０(摩尔投票法需要加入验证环节)
  3. 摩尔投票法找的其实不是众数，而是占一半以上的数。当数组没有超过一半的数，
  则可能返回非众数，比如[1, 1, 2, 2, 2, 3, 3]，最终返回3。投票法简单来说就是不同
  则抵消，占半数以上的数字必然留到最后。
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/solution/mian-shi-ti-39-shu-zu-zhong-chu-xian-ci-shu-chao-3/)）

  ```python
  class Solution:
  
      def MoreThanHalfNum(self, numbers):
          # write code here
          # 摩尔投票法
          votes = 0
          count = 0
          for num in numbers:
              # 假设x为众数
              if votes == 0: x = num
              # 进行投票表决
              votes += 1 if x == num else -1
          # 验证环节
          for num in numbers:
              if num == x: count += 1
          return x if count > len(numbers) >> 1 else 0 # 当无众数时返回 0
  ```

## 二维数据查找（<font color = red>重点</font>）

题目类型：数组

题目难度：:star2:

- 问题描述

  ```python
  问题描述：
  	在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增
  的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的
  一个二维数组和一个整数，判断数组中是否含有该整数,形式如下:
  1  2  3  4
  2  3  4  5
  6  7  8  9
  10 11 12 13
  解决方案：
  1.暴力搜索（遍历）
  时间复杂度：O(N^2)
  空间复杂度：O(1)
  
  2.考虑数据在存储位置上的存储性质
  时间复杂度：O(N)
  空间复杂度：O(1)
  ```

- 代码

  ```python
  class Solution:
  
      def find(self, array, target):
          """不考虑时间复杂度，暴力搜索, T(O)=n^2"""
  
          for i in range(len(array)):
              for j in range(len(array[i])):
                  if array[i][j] == target:
                      return True
          return False
  
      def findNumberIn2DArray(self, matrix, target):
          """在二维数组中找到指定数字"""
  
          i, j = len(matrix)-1, 0
          while i >= 0 and j < len(matrix[0]):
              if matrix[i][j] > target: i -= 1
              elif matrix[i][j] < target: j += 1
              else: return True
  
          return False
  ```

## 跳台阶问题（<font color = red>重点</font>）

题目类型：数组、动态规划

题目难度：:star2:

- 问题描述

  ```python
  问题描述1：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级
  的台阶总共有多少种跳法（先后次序不同算不同的结果）
  解决方案：
  当n=0 1（默认值）
  n=1 1 
  n=2 2
  n=3 3
  n=4 5
  ．．．．．．
  所以，符合斐波那契数列f(n) = f(n-1) + f(n-2)
  时间复杂度：O(n)
  空间复杂度：O(1)
  
  问题描述2：一只青蛙一次可以跳上1级台阶，也可以跳上2级,更可以一次跳上n级台阶
  求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）
  解决方案：
  n = 0 0
  n = 1 1
  n = 2 2
  n = 3 4
  ．．．．．．
  所以，f(n) = 2f(n-1)
  
  时间复杂度：O(n)
  空间复杂度：O(1)
  ```

- 代码（[解题思路](https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/57xs06/)）

  ```python
  class Solution:
  
  # 问题一
      def numWays(self, n: int) -> int:
          a, b = 1, 1
          for _ in range(n):
              a, b = b, a + b
          
          return a%1000000007
      
  # 问题二
      def jump_floor(self, n: int):
   
          if n == 0 or n == 1 or  n == 2:
              return n
  
          return 2 * self.jump_floor(n - 1)
  ```

## 链表中倒数第k个结点（<font color = red>重点</font>）

题目类型：链表、双指针

题目难度：:star2::star2:

- 问题描述

  ```python
  问题描述：
  输入一个链表，输出该链表中倒数第k个结点
  
  解决方案：
  方法1：使用栈存储，先进后出。
  方法2：双指针(双指针相差k，先前指针走完时，正好后指针到指定结点)
   former + after = after + former
   K + M = Ｍ + K
  时间复杂度：O(N)
  空间复杂度：O(1)
  ```

- 代码（[解题思路](![Picture0.png](https://pic.leetcode-cn.com/ab52aeb21d3ea0c2b2aaca94241413db5d060b88e950461953db64e36a89a435-Picture0.png))）

  算法图解：

  <img src="/home/gavin/Python/剑指offer/总结/imgs/双指针.png" style="zoom: 50%;" />

  ```python
  class Solution:
      
      def FindKthToTail(self, head, k):
          """双指针，两个指针之间相差k值"""
  
          former, latter = head, head
          for _ in range(k):
              # 提前判断K是否满足要求
              if not former: return None
              former = former.next
  
          while former:
              former = former.next
              latter = latter.next
  
          return latter
  ```

## 链表的翻转（<font color = red>重点</font>）

题目类型：链表

题目难度：:star2::star2:

- 问题描述

  ```python
  问题描述：
  输入一个链表，反转链表后，输出新链表的表头。
  
  解决方案：
  链表的遍历插入
  
  时间复杂度：O(N)
  空间复杂度：O(1)
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/solution/jian-zhi-offer-24-fan-zhuan-lian-biao-die-dai-di-2/)）

  算法图解：

  <img src="/home/gavin/Python/剑指offer/总结/imgs/链表翻转.gif" style="zoom: 67%;" />

  ```python
  class Solution:
  
      def reverseList(self, pHead):
          """链表的翻转"""
  
          cur, pre = pHead, None
          while cur:
              tmp = cur.next
              cur.next = pre
              pre = cur
              cur = tmp
  
          return pre
  ```

## 合并两个排序的链表（<font color = red>重点</font>）

题目类型：链表

题目难度：:star2::star2:

- 问题描述

  ```python
  问题描述：
  	输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合
   成后的链表满足单调不减规则。
  
  解决方案：
  1. 构建一个新的链表用于添加合并后的有序链表
  2. 递归
  
  时间复杂度：min(O(len(l1), len(l2)))
  空间复杂度：O(1)
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/solution/mian-shi-ti-25-he-bing-liang-ge-pai-xu-de-lian-b-2/)）

  算法图解：

  <img src="/home/gavin/Python/剑指offer/总结/imgs/12.png"  />

  ```python
  class ListNode:
       def __init__(self, x):
           self.val = x
           self.next = None
  
  
  class Solution:
      
      def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
  
          cur = dummy = ListNode(0)
  
          while l1 and l2:
              if l1.val < l2.val:
                  cur.next, l1 = l1, l1.next
              else:
                  cur.next, l2 = l2, l2.next
              cur = cur.next
          
          cur.next = l1 if l1 else l2
  
          return dummy.next
  ```

## 两个链表的第一个公共结点（浪漫相遇）:heart:

题目类型：链表、双指针

题目难度：:star2::star2:

<img src="/home/gavin/Python/剑指offer/总结/imgs/14.png" style="zoom: 67%;" />

- 问题描述

  ```python
  问题描述：
  输入两个链表，找出它们的第一个公共节点。
  
  解决方案：
  1. 暴力搜索
  No Recommend
  2.使用栈从后向前找出第一个不相等的结点
  A:1 2 5 6
  公共结点---->10 11 55 88
  B:2 4 8 9
  3. 交替遍历指针
  时间复杂度：（M + N）
  空间复杂度：（１）
  p1 -> --->......p1=p2
  p2 --> ---->......return p1
  实例：
  a:(1 2 3 4 ) 10 10 10
  b:(0 7 8 9 6 5 2)  10 10 10
  c(公共部分): 10 10 10
  a + c + b = b + c + a
  
  时间复杂度：O(a + b)
  空间复杂度：O(1)
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/solution/shuang-zhi-zhen-fa-lang-man-xiang-yu-by-ml-zimingm/)）

  ```python
  class Solution:
  
      def findFirstCommonNode(self, pHead1, pHead2):
          """烂漫相遇问题（我走过你来时的路）"""
  
          node1, node2 = pHead1, pHead2
          
          while node1 != node2:
              node1 = node1.next if node1 else pHead2
              node2 = node2.next if node2 else pHead1
              
          return node1
  ```

## 重建二叉树（<font color = red>重点</font>）

题目类型：树

题目难度：:star2:

- 问题描述

  ```python
  问题描述：
  　　输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设
  输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历
  序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8 ,6}，则重建二叉树并返
  回。
  
  解决方案:
  前序遍历的第一个结点为根结点
  递归
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/solution/mian-shi-ti-07-zhong-jian-er-cha-shu-di-gui-fa-qin/)）

  图解

  ![](/home/gavin/Python/剑指offer/总结/imgs/重建二叉树.png)

  ```python
  class TreeNode:
  
      def __init__(self, x):
          self.val = x
          self.left = None
          self.right = None
  
  
  class Solution:
      
      def reConstructBinaryTree1(self, pre, tin):
  
          if len(pre) == 0:
              return None
          else:
              # 根据前序遍历，找出根节点在中序遍历中的位置
              pos = tin.index(pre[0])
  
          root = TreeNode(pre[0])
          root.left = self.reConstructBinaryTree1(pre[1:pos + 1], tin[:pos])
          root.right = self.reConstructBinaryTree1(pre[pos + 1:], tin[pos + 1:])
  
          return root
  ```

## 从上往下打印二叉树（<font color = red>重点</font>）

- 问题描述

  ```python
  问题描述：
  从上往下打印出二叉树的每个节点，同层节点从左至右打印
  
  解决方案：
  简单的层序遍历
  ```

- 代码

  **图解**

  ![](/home/gavin/Python/剑指offer/总结/imgs/层序遍历.png)

  ```python
  class Solution:
      
          def levelOrder(self, root: TreeNode) -> List[int]:
              """"层序遍历"""
              
                  if not root: return []
                  
                  res, queue = [], collections.deque()
                  queue.append(root)
                  
                  while queue:
                          node = queue.popleft()
                          res.append(node.val)
                          if node.left: queue.append(node.left)
                          if node.right: queue.append(node.right)
                              
         	        return res
      
  	def levelOrder(self, root):
  		"""层序遍历（每一层遍历）"""
          
  		if root is None: return []
  		res, deque = [], collections.deque()
  		deque.append(root)
  		
  		while deque:
  			tmp = []
  			for _ in range(len(deque)):
  				node = deque.popleft()
  				tmp.append(node.val)
  				if node.left: deque.append(node.left)
  				if node.right: deque.append(node.right)
  			res.append(tmp)
  
  		rerurn res
  	
              def levelOrder(self, root: TreeNode) -> List[List[int]]:
              	"""Z字形遍历"""
                  
                  if not root: return []
                  res, deque = [], collections.deque([root])
  
                  while deque:
                      tmp = collections.deque()
                      for _ in range(len(deque)):
                          node = deque.popleft() # 从左向右遍历
                          if len(res) % 2: tmp.appendleft(node.val) # 偶数层,队列首部
                          else: tmp.append(node.val) # 奇数层，队列尾部
                          if node.left: deque.append(node.left)
                          if node.right: deque.append(node.right)
  
                      res.append(list(tmp))
                  return res
  ```

## 最小的k个数（<font color = red>重点</font>）

题目类型：数组、排序

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
         输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个
  数字，则最小的4个数字是1,2,3,4,。
  
  解决方案：
  (1) quick sort
  未优化：所有数字先有序化，后截取指定区间内的数字
  时间复杂度：O(nlogn)
  空间复杂度：O(n)
  优化：旨在k区间内进行寻找
  若 k = l，我们就找到了最小的 k 个数，就是左侧的数组；
  若 k<l，则最小的 k 个数一定都在左侧数组中，我们只需要对左侧数组递归
  地 parition 即可；
  若 k>l，则左侧数组中的 l 个数都属于最小的 k 个数，我们还需要在右侧
  数组中寻找最小的 k-l 个数，对右侧数组递归地 partition 即可。
  时间复杂度：O(n)
  空间复杂度：o(logn)
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/jian-zhi-offer-40-zui-xiao-de-k-ge-shu-j-9yze/)）

  图解最大堆

  <img src="/home/gavin/Python/剑指offer/总结/imgs/最大堆.gif" style="zoom:80%;" />

  ```python
  class Solution:
      
      def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
  
          def quickSort(nums, start,  end):
  
              if start >= end:
                  return nums[:k]
              
              low = start
              hight = end
              pivot = nums[start]
              while low < hight:
                  while low < hight and pivot <= nums[hight]:
                      hight -= 1
                  nums[low] = nums[hight]
                  while low < hight and pivot > nums[low]:
                      low += 1
                  nums[hight] = nums[low]
              nums[low] = pivot
  
              if k < low: quickSort(nums, start, low - 1)
              if k > hight: quickSort(nums, low + 1, end)
          
          quickSort(arr, 0, len(arr) - 1)
  
          return arr[:k]
  ```

## 两数之和（<font color = red>重点</font>）

题目类型：数组

题目难度：:star2::star2:

- 问题描述

  ```python
  问题描述：
  	给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和
  为目标值 的那两个 整数，并返回它们的数组下标。你可以假设每种输入只会对应
  一个答案。但是，数组中同一个元素在答案里不能重复出现。你可以按任意顺序
  返回答案。
  
  解题方法：
  方法一：暴力求解
  时间复杂度O(N^2)
  空间复杂度O(1)
  
  方法二：哈希表（空间换时间）
  原理：将数组中的一个整数固定，另一个整数采用target - num的形式表现。
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

## 三数之和（<font color = red>重点</font>）

题目类型：数组

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述：
  	给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，
  使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
  
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

  ![](/home/gavin/Python/剑指offer/总结/imgs/79.png)

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
              # 正负相抵(提前终止)
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

## 二叉树的最近公共祖先（<font color = red>重点</font>）

题目类型：二叉树

题目难度：:star2::star2::star2:

==注意==：leetcode和牛客网对于本题的输入输出参数的要求。

- 问题描述

  ```python
  问题描述：
  	给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
  
  知识点：
          最近公共祖先的定义： 设节点 root为节点p,q 的某公共祖先，若其左子节点
  root.left和右子节点root.right 都不是p,q 的公共祖先，则称 root 是 “最近的公
  共祖先” 。
  
  解题方法：
  回朔法（后序遍历）
  时间复杂度：O(N)
  空间复杂度：O(N)
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/mian-shi-ti-68-ii-er-cha-shu-de-zui-jin-gong-gon-7/)）

  <img src="/home/gavin/Python/剑指offer/总结/imgs/61.png" style="zoom:75%;" />

  ```python
  class Solution:
      def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
          
          # 回朔终点
          if not root or root == p or root == q:
              return root
  
          left = self.lowestCommonAncestor(root.left, p, q)
          right = self.lowestCommonAncestor(root.right, p, q)
          
          # 三种情况
          if not left: return right
          if not right: return left
  
          return root
  ```

- 牛客网

  ```python
  问题描述：
  	给定一棵二叉树以及这棵树上的两个节点 o1 和 o2，请找到 o1 和 o2 的最近公共祖先节点。 
  主要区别在于结点的输入值从TreeNode类型变为int型
  参数说明：
  # @param root TreeNode类 
  # @param o1 int整型 
  # @param o2 int整型 
  # @return int整型
  ```

  ```python
  def lowestCommonAncestor(self , root , o1 , o2 ):
          # write code here
          def dfs(root, o1, o2):
              
              if not root or root.val == o1 or root.val == o2:
                  return root
              
              # 后序遍历
              left = dfs(root.left, o1, o2)
              right = dfs(root.right, o1, o2)
              
              # 如果left、right有一个为空，那么就返回不为空的哪一个
              if not left: return right
              if not right: return left
              #  如果left、right都不为空，那么代表o1、o2在root的两侧，所以root为他们的公共祖先
              
              return root
          
          return dfs(root, o1, o2).val
  ```

## 最长递增子序列（<font color=red>重点</font>）

题目类型：数组、动态规划

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      　给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。子序列是
  由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
  例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
  
  示例：
  输入：nums = [10,9,2,5,3,7,101,18]
  输出：4
  解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
  
  解题方法：
  动态规划四步走原则
  (1)转态定义：dp[i]表示到当前结点i所表示的子序列的长度
  (2)转态转移：dp[i] = max(dp[i], dp[j] + 1)，表示为i之前最大的递增子序列
  (3)初始值：dp = [1]*len(nums)
  (4)返回值：max(dp)
  
  时间复杂度：O(N^2)  两层循环
  空间复杂度：O(N)  dp状态的存储
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/)）

  算法图解：

  <img src="/home/gavin/Python/剑指offer/总结/imgs/76.png" style="zoom:80%;" />

  ```python
  class Solution:
      def lengthOfLIS(self, nums: List[int]) -> int:
          
          if not nums: return 0
          # 定义dp,并设置初始值
          dp = [1]*len(nums)
          # 遍历转态
          for i in range(len(nums)):
              for j in range(i):
                  if nums[j] < nums[i]:
                      # 更新状态(已有子序列的前提上进行更新)
                      dp[i] = max(dp[i], dp[j] + 1)
          # 返回值
          return max(dp)
  ```

## 最长回文子串（<font color=red>重点</font>）

题目类型：字符串

回文的意思是正着念和倒着念一样，如：==上海自来水来自海上==

- 问题描述

  ```
  问题描述：
  给你一个字符串 s，找到 s 中最长的回文子串。
  
  字符串的回文：
          对于一个子串而言，如果它是回文串，并且长度大于 2，那么将它首尾的
  两个字母去除之后，它仍然是个回文串。例如对于字符串“ababa”，如果我
  们已经知道“bab” 是回文串，那么 “ababa” 一定是回文串，这是因为它
  的首尾两个字母都是a”。
  
  
  解题方法：
  动态规划
  (1)状态定义：d[i][j]表示s[i:j]为回文子串；
  (2)状态转移：d[i][j] = dp[i + 1][j - 1]，子问题是否为回文子串；
  (3)初始状态：dp[i][i] = True，表示只有一个字符时为回文子串；
  (4)返回值：最长的回文子串长度。
  时间复杂度O(n^2)
  空间复杂度O(n^2)
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/)）

  图解：

  ![](/home/gavin/Python/剑指offer/总结/imgs/81.png)

  ```python
  class Solution:
      def longestPalindrome(self, s: str) -> str:
          
          n = len(s)
          # 当s只有一个字符和无字符时
          if n < 2:
              return s
          
          # 转态定义
          dp = [[False]*n for _ in range(n)]
          # 初始状态
          for i in range(n):
              dp[i][i] = True
          max_len, begin = 1, 0
          # 遍历状态
          for L in range(2, n + 1):
              # 左右边界
              for i in range(n):
                  j = i + L - 1
                  if j >= n:
                      break
                  if s[i] != s[j]:
                      dp[i][j] = False
                  else:
                      if j - i < 3:
                          dp[i][j] = True
                      else:
                          dp[i][j] = dp[i + 1][j - 1]
                  # 更新最长回文子串长度起始值
                  if dp[i][j] and j - i + 1 > max_len:
                      max_len = j - i + 1
                      begin = i
          
          return s[begin: begin + max_len]
  ```

## 