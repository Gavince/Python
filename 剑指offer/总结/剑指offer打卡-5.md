### 二叉树中和为某一值的路径

- 问题描述

  ```python
  问题描述：
  输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树
  的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数
  组靠前).
  
  解决方案：
  递归
  ```

- 代码

  ```python
  class Solution:
  
      def FindPath(self, root, expectNumber):
  
          if root is None:
              return []
  
          res = []
          if root.val == expectNumber and root.left is None and root.right is None:
              res.append(root.val)
  
          left = self.FindPath(root.left, expectNumber - root.val)
          right = self.FindPath(root.right, expectNumber - root.val)
          for path in left + right:
              # 向上添加路径
              res.append([root.val] + path)
  
          return res
  ```


### 判断是否是二叉搜索树的后序遍历序列结果

- 问题描述

  ```python
  问题描述：
  输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,
  否则输出No。假设输入的数组的任意两个数字都互不相同。
  
  解决方案：
  BST:整体上应该保证结点数值右大左小
  递归
  ```

- 代码

  ```python
  class Solution:
  
      def VerifySquenceOfBST(self, squence):
          if len(squence) == 0:
              return False
  
          root = squence.pop()
          lefttree = []
          righttree = []
  
          for i in range(len(squence)):
              if squence[i] < root:
                  lefttree.append(squence[i])
              else:
                  break
          for i in range(len(lefttree), len(squence) - 1):
              if squence[i] <= root:  # 表示右子树的结点值小于其对应根结点,不满足BST原则
                  return False
              righttree.append(squence[i])
  
          # 叶子结点
          if len(lefttree) <= 1:
              left = True
          else:
              left = self.VerifySquenceOfBST(lefttree)
          if len(righttree) <= 1:
              right = True
          else:
              right = self.VerifySquenceOfBST(righttree)
  
          return left and right
  ```

### 从上往下打印二叉树 二叉树的广度遍历

- 问题描述

  ```python
  问题描述：
  从上往下打印出二叉树的每个节点，同层节点从左至右打印
  
  解决方案：
  简单的层序遍历
  ```

- 代码

  ```python
  class TreeNode:
  
      def __init__(self, val):
  
          self.val = val
          self.left = None
          self.right = None
  
  
  class Solution:
  
      def __init__(self):
          self.root = None
  
      def add_node(self, val):
  
          node = TreeNode(val)
          if self.root is None:
              self.root = node
              return
          queue = [self.root]
          while queue:
              temp_node = queue.pop(0)
              if temp_node.left is None:
                  temp_node.left = node
                  return
              else:
                  queue.append(temp_node.left)
              if temp_node.right is None:
                  temp_node.right = node
                  return
              else:
                  queue.append(temp_node.right)
  
          return
  
      def PrintFromTopToBottom(self, root):
  
          if root is None:
              return None
          queue = [root]
          ret = []
          while queue:
              temp_node = queue.pop(0)
              ret.append(temp_node.val)
              if temp_node.left:
                  queue.append(temp_node.left)
              if temp_node.right:
                  queue.append(temp_node.right)
          return ret
  
  
  if __name__ == "__main__":
      obj = Solution()
      for i in range(1, 9):
          obj.add_node(i)
      # print(obj.PrintFromTopToBottom(obj.root))  # [1, 2, 3, 4, 5, 6, 7, 8]
      print(obj.FindPath(obj.root, 15))
  ```

### 二叉树的镜像

- 问题描述

  ```python
  问题描述：
  操作给定的二叉树，将其变换为源二叉树的镜像
  
  解决方案：
  
  源二叉树：
  　　８
  　６　10
  5    7    9     11
  镜像二叉树：
         8
    10     6
  11  9    7  5
  ```

- 代码

  ```python
  class TreeNode:
  
      def __init__(self, val):
          self.val = val
          self.left = None
          self.right = None
  
  
  class Solution:
  
      def Mirror(self, root):
          if root is None:
              return None
          if root.left is None and root.right is None:
              return root
          
          # 左右互换
          root.left, root.right = root.right, root.left
          self.Mirror(root.left)
          self.Mirror(root.right)
  
          return root
  ```

### 重建二叉树

- 问题描述

  ```python
  问题描述：
  输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和
  中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和
  中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
  
  解决方案:
  前序遍历的第一个结点为根结点
  递归
  ```

- 代码

  ```python
  class TreeNode:
  
      def __init__(self, x):
          self.val = x
          self.left = None
          self.right = None
  
  
  class Solution:
  
      def reConstructBinaryTree(self, pre, tin):
          """
          :param pre: 前序遍历结果
          :param tin: 中序遍历结果
          :return:
          """
  
          if not pre or not tin:
              return None
          if len(pre) is not len(tin):
              return None
  
          # 根节点为前序遍历的第一个值
          val = pre[0]
          root = TreeNode(val)
          pos = tin.index(val)
          tin_left = tin[:pos]
          tin_right = tin[pos + 1:]
  
          pre_left = pre[1:pos + 1]
          pre_right = pre[pos + 1:]
  
          # 递归遍历
          left_node = self.reConstructBinaryTree(pre_left, tin_left)
          right_node = self.reConstructBinaryTree(pre_right, tin_right)
          root.left = left_node
          root.right = right_node
  
          return root
  
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

### 二叉树的子结构

- 问题描述

  ```python
  问题描述：
  输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
  
  解决方案：
  ①如果A,B有一个为空，return False
  ②如果A,B不为空，A.val == B.val, 且B为单节点，则return True;如果结点B不为单节点则需要比较
  A.left.val == B.left.val 和 A.right.val == B.right.val
  ③如果B.val != A.val 则遍历Ａ结点的子节点和B进行比较，找到相同结点后，转②，否则return False
  ```

- 代码

  ```python
  class TreeNode:
  
      def __init__(self, val):
          self.val = val
          self.left = None
          self.right = None
  class Solution:
      def HasSubTree(self, pRoot1, pRoot2):
  
          if pRoot1 is None or pRoot2 is None:
              return False
          return self.isSubTree(pRoot1, pRoot2)
  
      def isSubTree(self, pRoot1, pRoot2):
          if pRoot1 is None and pRoot2 is None:
              return True
  
          if pRoot1 is None:
              return False
          if pRoot2 is None:
              return False
  
          if pRoot1.val == pRoot2.val:
              if pRoot2.left is None and pRoot2.right is None:  # 此时pRoot2无子节点
                  return True
              else:
                  if self.isSubTree(pRoot1.left, pRoot2.left) and self.isSubTree(pRoot1.right, pRoot2.right):
                      return True
  
          # A,B树原始根结点不相同
          return self.isSubTree(pRoot1.left, pRoot2) or self.isSubTree(pRoot1.right, pRoot2)
  
  ```

### 参考

[VISUALIZE CODE EXECUTION](http://www.pythontutor.com/)

[数据结构与算法题目](https://blog.csdn.net/storyfull/category_9475477_2.html)

[剑指offer（python）](https://blog.csdn.net/ggdhs/category_8914921.html)  



  

  

  

