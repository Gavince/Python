# Python剑指offer打卡-24

[toc]

## 岛屿的最大面积

题目类型：DFS、BFS

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给定一个包含了一些 0 和 1 的非空二维数组grid 。一个岛屿是由一些相邻的1(代表土地) 构成
  的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设grid的四个边缘都被
  0（代表水）包围着。找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0 )
  
  解题方法：
  DFS和BFS
  ```

- 代码

  **DFS**

  ```python
  class Solution:
      def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
  
          def dfs(grid, i, j):
  
              if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == 0:
                  return 0
              # 已访问标记
              grid[i][j] = 0
              return 1 + dfs(grid, i + 1, j) + dfs(grid, i - 1, j) + dfs(grid, i, j - 1) + dfs(grid, i, j + 1)
  
          ans = 0
          for i in range(len(grid)):
              for j in range(len(grid[0])):
                  if grid[i][j]:
                      ans = max(ans, dfs(grid, i, j))
          
          return ans
  ```

  **BFS**

  ```python
  class Solution:
      def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
  
          def bfs(grid, i, j):
              
              deque = [[i, j]]
              count = 0
              while deque:
                  [i, j] = deque.pop(0)
                  if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                      # 已访问标记
                      grid[i][j] = 0
                      count += 1
                      deque += [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
              
              return count
  
          ans = 0
          for i in range(len(grid)):
              for j in range(len(grid[0])):
                  if grid[i][j]:
                      ans = max(ans, bfs(grid, i, j))
          return ans
  
  ```

## 重排链表

题目类型：链表

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给定一个单链表 L 的头节点 head ，单链表 L 表示为：L0→ L1→ … → Ln-1→ Ln请
  将其重新排列后变为：L0→Ln→L1→Ln-1→L2→Ln-2→ …不能只是单纯的改变节点内部的值，而
  是需要实际的进行节点交换。
  
  解题方法：
  快慢指针 + 链表翻转 + 合并链表
  
  时间复杂度：O(N)
  空间复杂度：O(1)
  ```

- 代码

  快慢指针寻找中间节点（回文链表）

  ![](./imgs/97.png)

  ```python
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, val=0, next=None):
  #         self.val = val
  #         self.next = next
  class Solution:
      def reorderList(self, head: ListNode) -> None:
          """
          Do not return anything, modify head in-place instead.
          """
          # 快慢指针拆分
          slow, fast = head, head.next
          while fast and fast.next:
              slow = slow.next
              fast = fast.next.next
          
          cur = slow.next
          slow.next = None
          # 逆转链表
          pre = None
          while cur:
              tmp = cur.next
              cur.next = pre
              pre = cur
              cur = tmp
          # 两个链表的合并
          l1, l2 = head, pre
          while l1 and l2:
              l1_tmp = l1.next
              l2_tmp = l2.next
  
              l1.next = l2
              l1 = l1_tmp
  
              l2.next = l1
              l2 = l2_tmp
  ```

  

