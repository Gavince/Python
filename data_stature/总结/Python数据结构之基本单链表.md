## Python数据结构之基本单链表

### 前言
​		单向链接表(单链表)的结点是一个二元组，形式如下图，其表元素域elem保存着作为表元素的数据项（或者数据项的关联信息），链接域next里保存同一个表里下一个结点的标示．

![单链表节点表示](/home/gavin/Python/数据结构/Picture/单链表节点表示.png)

​		单链表的一般表示形式如下：

![单链表](/home/gavin/Python/数据结构/Picture/单链表.png)

### 基本链表的操作

#### 创建结点

- **代码**

  ```python
  class Node(object):
      """
      定义节点　
      """
      # 定义类属性,用来记录创建的结点数目
      count = 0
  
      def __init__(self, elem):
          
          self.elem = elem
          self.next = None
          Node.count += 1
          
      def __del__(self):
          """删除对象后自动删除"""
          
          Node.count -= 1
  ```

#### 初始化数据节点

- **代码**

  ```python
  class LList(object):
      """
      创建单链表
      """
  
      def __init__(self):
          """初始化头结点"""
          self._head = Node(None)
  
      def init_list(self, data):
          """创建单链表"""
          self._head = Node(data[0])
          p = self._head
  
          for i in data[1:]:
              node = Node(i)
              p.next = node
              p = p.next
  ```

#### 插入元素

- **图示**

  ![插入单链表](/home/gavin/Python/数据结构/Picture/插入单链表.png)

- **代码**

  ```python
      def insert_node(self, i, num):
          """插入数据节点"""
          
          if i > self.get_length():
              print("插入节点索引错误！！！")
              return 0
  
          # 寻找节点
          p = self._head
          index = 1
          if i == 1:
              #  头结点插入
              node = Node(num)
              node.next = self._head
              self._head = node
              return 0
          else:
              while index < i:#  查找索引结点
                  p = p.next
                  index += 1
              # 插入节点
              node = Node(num)
              node.next = p.next
              p.next = node
  ```

#### 删除指定节点

- **图示**

  ![单链表删除](/home/gavin/Python/数据结构/Picture/单链表删除.png)

- **代码**

  ```python
      def del_node(self, i):
          """删除节点"""
          
          if i > self.get_length():
              print("删除索引节点错误！！！")
              return 0
  
          p = self._head
          index = 1
          if i == 1:
              self._head = p.next
              return 0
          else:
              while index < i:
                  index += 1
                  pre = p  # 保存上一个节点
                  p = p.next  # 遍历数据节点
              pre.next = p.next　# 实现删除
  ```

#### 获得结点长度

- **代码**

  ```python
  ## 方法一
      def get_length(self):
          """获得链表的长度"""
          if self.is_empty():
              print("Length is 0")
              return 0
  
          p = self._head
          num = 0
          while p:
              num += 1
              p = p.next
          return num
      
  ## 方法二(通过设置类属性来得到创建的节点个数)
  	@staticmethod
      def get_length():
          """获得数据的长度"""
          print("创建的数据节点数目为：", Node.count)
          return Node.count
  ```

#### 读出数据

- **代码**

  ```python
      def read_list(self):
          """读取单链表"""
          
          if self.is_empty():
              print("未录入数据！！！")
              return 0
          
          p = self._head
          while p:
              print("Elem is :", p.elem)
              p = p.next
  ```

#### 链表是否为空

- **代码**

  ```python
      def is_empty(self):
          """判断是否为空"""
          
          p = self._head
          if p is None:
              print("Empty!!!")
              return 1
          else:
              return 0
  ```

### 单链表反转

- **图示**

  ![翻转单链表](/home/gavin/Python/数据结构/Picture/翻转单链表.png)

  

- **代码**

  ```python
      def reverse(self):
          """单链表的翻转"""
  
          p = self._head
          self._head = None
          while p:
              q = p
              p = p.next  # 循环遍历
              q.next = self._head
              self._head = q
  ```

### 单链表的边界值测试

- **测试代码模块**

  ```python
  class TestModule():
      """测试单链表的模块"""
  
      def __init__(self, data = [], node = None):
          self.data = data
          self.node = node
          print("执行测试程序！")
  
      def test_del(self):
          """ 测试删除操作"""
          
          self.node.init_list(self.data)
          #  1. 测试删除模块
          print("删除前的数据：")
          self.node.read_list()
          #  1.１ 删除头节点
          self.node.del_node(1)
          print("删除头结点:")
          self.node.read_list()
          #  1.2 删除未节点
          print("删除前的数据：")
          self.node.read_list()
          print("删除尾节点：")
          self.node.del_node(4)
          self.node.read_list()
          #  1.3 删除中间节点
          print("删除前的数据：")
          self.node.read_list()
          print("删除中间节点：")
          self.node.del_node(2)
          self.node.read_list()
          self.node.del_node(2)
          self.node.read_list()
  
      def test_insert(self):
          """测试插入算法"""
  
          self.node.init_list(self.data)
          print("原始数据：")
          self.node.read_list()
          #  1. 头插
          print("头插：")
          self.node.insert_node(1, 100)
          self.node.read_list()
          #  2. 尾插
          print("尾插：")
          self.node.insert_node(6, 666)
          self.node.read_list()
          #  3. 指定位置插入
          print("中间插：")
          self.node.insert_node(2, 455)
          self.node.read_list()
          
      def test_reverse(self):
          """测试翻转模块"""
          
          self.node.init_list(self.data)
          print("原始数据：")
          self.node.read_list()
          self.node.reverse()
          print("数据翻转后：")
          self.node.read_list()
  
  ```

- **测试删除代码的结果**

  ```python
  删除前的数据：
  Elem is : 1
  Elem is : 2
  Elem is : 3
  Elem is : 4
  Elem is : 5
  删除头结点:
  Elem is : 2
  Elem is : 3
  Elem is : 4
  Elem is : 5
  删除前的数据：
  Elem is : 2
  Elem is : 3
  Elem is : 4
  Elem is : 5
  删除尾节点：
  Elem is : 2
  Elem is : 3
  Elem is : 4
  删除前的数据：
  Elem is : 2
  Elem is : 3
  Elem is : 4
  删除中间节点：
  Elem is : 2
  Elem is : 4
  ```

- **测试插入代码的结果**

  ```python
  原始数据：
  Elem is : 1
  Elem is : 2
  Elem is : 3
  Elem is : 4
  Elem is : 5
  头插：
  Elem is : 100
  Elem is : 1
  Elem is : 2
  Elem is : 3
  Elem is : 4
  Elem is : 5
  尾插：
  Elem is : 100
  Elem is : 1
  Elem is : 2
  Elem is : 3
  Elem is : 4
  Elem is : 5
  Elem is : 666
  中间插：
  Elem is : 100
  Elem is : 1
  Elem is : 455
  Elem is : 2
  Elem is : 3
  Elem is : 4
  Elem is : 5
  Elem is : 666
  ```

- **测试单链表翻转代码的结果**

  ``` python
  原始数据：
  Elem is : 1
  Elem is : 2
  Elem is : 3
  Elem is : 4
  Elem is : 5
  数据翻转后：
  Elem is : 5
  Elem is : 4
  Elem is : 3
  Elem is : 2
  Elem is : 1
  
  ```
  
  ### 总结
  
  ​		基本单链表的包含一系列结点，通过<font color = red>一个方向</font>的链接构造起来．它支持高效的（Ｏ(1)的）前端（首端）插入和删除操作，定位操作或尾端操作都需要Ｏ(n)时间．基本单向链表的操作相对简单一些，如果遇见难以理解的操作，需要通过图示的方法，直观的理解算法的本质．基本单链表的操作也有一些缺点，如不能支持高效的尾部删除等．本次代码没有添加文字形式的注释，如需更深的理解，请阅读参考书籍．代码链接如下：
  
  [Python数据结构之基本单链表]()

