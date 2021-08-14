

# Python剑指offer打卡-28

## 二叉树的右视图

题目类型：二叉树

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
  	给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
  
  解题方法：
  层序遍历
  ```

- 代码（[解题方法](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/bfs-de-shi-yong-chang-jing-zong-jie-ceng-xu-bian-l/)）

  ```python
  import collections
  
  
  class Solution:
      def rightSideView(self, root: TreeNode) -> List[int]:
  
          if root is None:
              return []
          res = []
          deque = collections.deque([root])
          while deque:
              tmp = []
              for _ in range(len(deque)):
                  node = deque.popleft()
                  tmp.append(node.val)
                  if node.left: deque.append(node.left)
                  if node.right: deque.append(node.right)
              res.append(tmp[-1])
          
          return res
  ```

  