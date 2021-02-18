# Python剑指offer打卡-7

[toc]

## 二叉树的下一个节点

- 问题描述

  ```
  问题描述：
  给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
  ```

  

- 代码（[解题思路](https://www.nowcoder.com/questionTerminal/9023a0c988684a53960365b889ceaf5e)）

  图解

  ![](./imgs/中序遍历.png)

- ```python
  class TreeLinkNode:
  
      def __init__(self, val):
          self.val = val
          self.left = None
          self.right = None
          self.next = None
  
  
  class Solution:
  
      def GetNext(self, pNode):
  
          if pNode.right:
              tmp_node = pNode.right
              while tmp_node.left:
                  tmp_node = tmp_node.left
              return tmp_node
          else:
              tmp_node = pNode
              while tmp_node.next:  
                  if tmp_node.next.left == tmp_node: # 当前节点为父节点的左节点
                      return tmp_node.next
                  tmp_node = tmp_node.next  # 寻找父结点, 当前结点为父节点的右节点
              return None
  ```

## 对称二叉树

- 问题描述

  ```
  问题描述：
  请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的.
  示例：
      1
    2   2
  3  4 4  3
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/solution/mian-shi-ti-28-dui-cheng-de-er-cha-shu-di-gui-qing/)）

  ```python
  class Solution:
      
      def isSymmetric(self, root):
  
          def recur(L, R):
              if not L and not R: return True
              if not L or not R or L.val != R.val: return False
              return recur(L.left, R.right) and recur(L.right, R.left)
  
          return recur(root.left, root.right) if root else True
  ```


## 按之字形顺序打印二叉树

- 问题描述

  ```
  请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
  解题：
  构造奇偶条件，遍历不同顺序
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/solution/mian-shi-ti-32-iii-cong-shang-dao-xia-da-yin-er--3/)）

  ```python
  # Definition for a binary tree node.
  import collections
  
  class TreeNode:
       def __init__(self, x):
           self.val = x
           self.left = None
           self.right = None
  
  class Solution:
      def levelOrder(self, root: TreeNode) -> List[List[int]]:
  
          if not root: return []
          res, deque = [], collections.deque([root])
  
          while deque:
              tmp = collections.deque()
              for _ in range(len(deque)):
                  node = deque.popleft() # 从左向右遍历
                  if len(res) % 2: tmp.appendleft(node.val) # 偶数层,队列首部,从右向左
                  else: tmp.append(node.val) # 奇数层，队列尾部
                  if node.left: deque.append(node.left)
                  if node.right: deque.append(node.right)
              
              res.append(list(tmp))
          return res
  ```


## 把二叉树打印成多行

- 问题描述

  ```
  问题描述：
  从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/solution/mian-shi-ti-32-ii-cong-shang-dao-xia-da-yin-er-c-5/)）

  ```python
  import collections
  
  class TreeNode:
       def __init__(self, x):
           self.val = x
           self.left = None
           self.right = None
  
  class Solution:
      def levelOrder(self, root: TreeNode) -> List[List[int]]:
  
          if not root: return []
          res, queue = [], collections.deque([root])
  
          while queue:
              tmp = []
              for _ in range(len(queue)):
                  node = queue.popleft()
                  tmp.append(node.val)
                  if node.left: queue.append(node.left)
                  if node.right: queue.append(node.right)
  
              res.append(tmp)
          return res
  ```

## 二叉搜索树的第k个节点

- 问题描述

  ```
  问题描述：
  给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8） 中，按结点数值大小顺序第三小结点的值为4。
  
  解决方法：
  二叉搜索树的中序遍历为有序序列（递增序列），将其转换为逆序列，可以求得最大kth数值，并实现提前返回，减少时间复杂度。
  ```

- 代码

  ```python
  class Solution:
      def kthLargest(self, root: TreeNode, k: int) -> int:
          
          def dfs(root):
              if not root: return
              dfs(root.right)
              if self.k == 0: return  # 实现提前放回，节省内存消耗
              self.k -= 1
              if self.k == 0: self.res = root.val
              dfs(root.left)
  
          self.k = k
          dfs(root)
          return self.res
  ```

  ## 参考

[python collections 模块中的 deque](https://blog.csdn.net/HappyRocking/article/details/80058623?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control)