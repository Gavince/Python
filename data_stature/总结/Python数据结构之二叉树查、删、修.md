## Python数据结构之二叉树增、查、删、修

### 增加

​		一层一层添加数据（层序遍历原则），使用队列对结点进行存储，从左向右增加结点，最终可形成完全二叉树。

```python
def add(self, val):
    """添加树节点实现完全二叉树"""
    node = Node(val)

    if self.root is None:
        self.root = node
        return

    #  使用队列来实现节点存储
    queue = [self.root]
    while queue:
        tmp_node = queue.pop(0)  # 先进先出
        #  左子树
        if tmp_node.left_child is None:
            tmp_node.left_child = node
            return
        else:
            queue.append(tmp_node.left_child)
       	#  右子树
        if tmp_node.right_child is None:
            tmp_node.right_child = node
            return
        else:
            queue.append(tmp_node.right_child)
```

### 查找

#### 查找当前结点

- 层序查找

  ```python
  def bro_search(self, val):
      """查找指定数据的父亲结点"""
      
      if self.root.val == val:  # 根节点无父亲节点
          return self.root
  
      # 层序遍历，寻找节点
      queue = [self.root]
  
      while queue:
          tmp_node = queue.pop(0)
          
          if tmp_node.left_child and tmp_node.left_child.val == val:
              return tmp_node.left_child
          
          if tmp_node.right_child and tmp_node.right_child.val == val:
              return tmp_node.right_child
  
          #  往下一层进行寻找
          if tmp_node.left_child:
              queue.append(tmp_node.left_child)
          if tmp_node.right_child:
              queue.append(tmp_node.right_child)
  
      return None
  ```

- 前序查找

  ```python
  def pre_search(self, node, val):
      """先序遍历"""
  
      if node is None:
          return
      
      if node.val == val:
          return node
      left_part = self.pre_search(node.left_child, val)
      # 直接查找到结点，不在继续递归直接退出
      if left_part:
          return left_part
      right_part = self.pre_search(node.right_child, val)
      if right_part:
          return right_part
  
      return None
  ```

- 中序查找

  ```python
  def in_search(self, node, val):
      """中序查找"""
      if node is None:
          return
  
      left_part = self.in_search(node.left_child, val)
      if left_part:
          return left_part
      print("中序！！！")
      if node.val == val:
          return node
      right_part = self.in_search(node.right_child, val)
      if right_part:
          return right_part
  
      return None
  ```

- 后序查找

  ```python
  def post_search(self, node, val):
      """后序查找"""
      if node is None:
          return
  
      left_part = self.post_search(node.left_child, val)
      if left_part:
          return left_part
      right_part = self.post_search(node.right_child, val)
      if right_part:
          return right_part
      print("后序！！！")
      if node.val == val:
          return node
  
      return None
  ```

#### 查找结点的父结点

**目标**：层序遍历搜索所查找的结点，并把其父结点作为返回值返回。

```python
def get_parent(self, val):
    """查找指定数据的父亲结点"""

    if self.root.val == val:  # 根节点无父亲节点
        return None

    # 层序遍历，寻找节点(队列)
    queue = [self.root]

    while queue:
        tmp_node = queue.pop(0)
        if tmp_node.left_child and tmp_node.left_child.val == val:
            return tmp_node
        if tmp_node.right_child and tmp_node.right_child.val == val:
            return tmp_node

        #  往下一层进行寻找
        if tmp_node.left_child:
            queue.append(tmp_node.left_child)
        if tmp_node.right_child:
            queue.append(tmp_node.right_child)
```

### 删除

#### 删除结点及其子结点

目标：搜索到所删除的结点，并且把孩子结点也删除。

```python
def del_node(self, node, val):
    """删除节点的同时需要将左右子树都删除"""
    if node is None:
        return
    if node.val == val and node == self.root:
        self.root = None
        self.flag = True
        return

    #  结点中找的数值,左右结点置空
    if node.val == val:
        node.left_child = None
        node.right_child = None
        return node.val

    # 遍历
    left_part = self.del_node(node.left_child, val)
    if left_part:  # 左树查找有返回值
        node.left_child = None  # 查找结点置空
        self.flag = True

    right_part = self.del_node(node.right_child, val)
    if right_part:  # 右树查找有返回值
        node.left_child = None
        self.flag = True
        return None
```

输出结果（删除中间结点1）：

```python
删除前树结构： 0 1 3 7 8 4 9 2 5 6 
删除后树结构： 0 2 5 6
```

输出结果（删除叶子结点9）：

```python
删除前树结构： 0 1 3 7 8 4 9 2 5 6 
删除后树结构： 0 1 3 7 8 4 2 5 6 
```

输出结果（删除根结点0）：

```python
删除前树结构： 0 1 3 7 8 4 9 2 5 6 
删除后树结构：
```

输出结果（删除根未知结点）：

```python
删除前树结构： 0 1 3 7 8 4 9 2 5 6 
树中无指定结点！！！
```

#### 删除当前结点

目标：只删除结点，不删除其孩子结点

```python
    def delete(self, val):
        """删除指定结点"""

        if self.root is None:
            return False

        # 得到删除结点的父亲结点
        parent = self.get_parent(val)

        if parent:
            # 得到删除结点
            del_node = parent.left_child if parent.left_child.val == val else parent.right_child

            if del_node.left_child is None:
                if parent.left_child.val == val:
                    parent.left_child = del_node.right_child
                else:
                    parent.right_child = del_node.right_child
                del del_node
                return True
            elif del_node.right_child is None:
                if parent.left_child.val == val:
                    parent.left_child = del_node.left_child
                else:
                    parent.right_child = del_node.left_child

                del del_node
                return True
            else:  # 左右树都不为空
                tmp_pre = del_node
                tmp_next = del_node.right_child
                if tmp_next.left_child is None:
                    tmp_pre.right_child = tmp_next.right_child
                    tmp_next.left_child = del_node.left_child
                    tmp_next.right_child = del_node.right_child
                else:
                    while tmp_next.left_child:  # 寻找左子树
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left_child

                    tmp_pre.left_child = tmp_next.right_child
                    tmp_next.left_child = del_node.left_child
                    tmp_next.right_child = del_node.right_child
                if parent.left_child.val == val:
                    parent.left_child = tmp_next
                else:
                    parent.right_child = tmp_next
                del del_node
                return True
        else:
            return False
```

### 参考

[Python 实现二叉树的创建、二叉树的添加、二叉树的删除、二叉树的修改、二叉树的查找、二叉树的的遍历 最详细的二叉树 增 删 改 查](https://blog.csdn.net/storyfull/article/details/103717740)



