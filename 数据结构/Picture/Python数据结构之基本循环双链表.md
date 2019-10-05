## Python数据结构之基本双链表

### 前言

​		单链表只有一个一个方向的链接，只能做一个方向的扫描和逐步操作．即使增加了尾部节点的引用，也只能支持Ｏ(1)时间的首端元素加入/删除和尾端加入．如果希望两端插入和删除操作都能高效的完成，就必须修改结点的基本设计，加入另一个方向的链接，这样就得到了双向链接表，简称**双链表**．双链表的一般结构如下图：

![双链表](/home/gavin/Python/数据结构/Picture/双链表.png)

### 双链表节点

- **说明**

  ​	双向链表支持两个方向的移动，因此在结点的设置上增加了指向前一个域的prev项．

- **图示**

  ![双链表的节点](/home/gavin/Python/数据结构/Picture/双链表的节点.png)

- **代码**

  ``` python
  class DLNode:
      """
      定义双向链表的结点
      """
  
      def __init__(self, elem, ):
          self.elem = elem
          self.next = None
          self.prev = None
  ```

### 双链表头插法

- **图示**（其中<font color = red>head</font>表示未插入数据时，所对应的头结点）

  ![双链表头插法](/home/gavin/Python/数据结构/Picture/双链表头插法.png)

- **代码**

  ```python
      def add_head(self, elem):
          """头插法"""
  
          # 1.创建结点
          node = DLNode(elem=elem)
          #  2.链表为空
          if self.is_empty():
              self._head = node
          #  3.链表不为空
          else:
              node.next = self._head
              self._head.prev = node
              self._head = node  # 4.定义新的头结点双
  ```

 ### 双链表尾插法

- **图示**

  ![双向链表尾插法](/home/gavin/Python/数据结构/Picture/双向链表尾插法.png)

- **代码**

  ```python
      def append(self, elem):
          """尾插法"""
  
          # 1.创建结点
          node = DLNode(elem=elem)
          # 2.链表为空
          if self.is_empty():
              self._head = node
          #  3.链表不为空
          else:
              cur = self._head
              while cur.next:
                  cur = cur.next
  
              # 4. 尾部插入数据
              cur.next = node
              node.prev = cur
              
  ```

### 双链表的插入

- **说明**

  ​		双链表的插入需要考虑三个位置，首结点,尾结点和中间结点，对于头尾结点的插入，可以使用使用头插法和尾插法来处理，而对于中间结点，需要考虑插入结点后前后的连接状态，遵循<font color = ##0099ff>你来我往</font>的原则．同时，在插入时也要注意指向的问题，负责会出现类型错误．

- **图示**

  ![双链表的插入](/home/gavin/Python/数据结构/Picture/双链表的插入.png)

- **代码**

  ```python
      def insert(self, pos, elem):
          """指定位置插入数据"""
  
          if pos > self.get_length():
              print("非法位置插入数据！！！")
              return
          #  1.判断特殊条件
          if pos == 1:
              self.add_head(elem)
          elif pos == self.get_length():
              self.append(elem)
          else:
              node = DLNode(elem)
              cur = self._head
              while pos and cur.next:
                  pos -= 1
                  cur = cur.next
              #  2.插入元素
              node.next = cur
              node.prev = cur.prev
              cur.prev.next = node
              cur.prev = node
  ```


###　双链表的删除

- **图示**

  ![双链表的删除](/home/gavin/Python/数据结构/Picture/双链表的删除.png)

- **代码**

  ``` python
      def del_node(self, elem):
          """删除指定元素"""
  
          flag = 0  # 记录删除点元素
          if self.is_empty():
              print("空链表，请先输入数据！")
              return
  
          cur = self._head
          #  1. 判断头结点
          if cur.elem == elem:
              if cur.next is None:
                  self._head = None
              else: 
                  self._head = cur.next
                  self._head.prev = None
          else:
              while cur.next:
                  #  3.删除中间节点
                  if cur.elem == elem:
                      cur.prev.next = cur.next
                      cur.next.prev = cur.prev
                      flag += 1
                  #  4.最后一个结点删除
                  cur = cur.next
  
              if cur.elem == elem:
                  cur.prev.next = None  # 指向为空
                  flag += 1
              if flag == 0:
                  print("所删除的元素不在链表中！")
  ```

### 功能测试

- **说明**

  ​		该模块主要对一些特殊值进行测试，主要是对临界值进行测试．保证代码的正确性和健硕性．

- **测试代码**

  ```python
  class TestModule:
      """
      测试类
      """
  
      def __init__(self, list1=None):
          self.list1 = list1
  
      def test_add(self, list1=None):
          """测试添加操作"""
  
          self.list1.add_head(478)
          self.list1.add_head(465)
          self.list1.add_head(45)
          self.list1.append(78)
          self.list1.append(12)
          self.list1.append(79)
          self.list1.show()
  
      def test_del(self):
          """测试删除操作"""
          print("原始数据:")
          self.list1.show()
          print("--" * 10)
  
          print("首部删除元素：")
          self.list1.del_node(45)
          self.list1.show()
          print("--" * 10)
  
          print("中间删除元素：")
          self.list1.del_node(78)
          self.list1.show()
  
          print("--" * 10)
          print("尾部删除元素：")
          self.list1.del_node(79)
          self.list1.show()
  
          print("--" * 10)
          print("删除不存在的元素：")
          self.list1.del_node(1212)
          print("--" * 10)
          self.list1.show()
  
      def test_insert(self):
          """测试插入操作"""
  
          print("原始数据:")
          self.list1.show()
          print("--" * 10)
  
          print("首部添加元素：")
          self.list1.insert(1, 100)
          self.list1.show()
          print("--" * 10)
  
          print("中间添加元素：")
          self.list1.insert(4, 456456)
          self.list1.show()
  
          print("--" * 10)
          print("尾部添加元素：")
          index = self.list1.get_length()
          self.list1.insert(index, 11111)
          self.list1.show()
  
          print("--" * 10)
          print("非法位置添加元素：")
          self.list1.insert(1111, 1212)
          self.list1.show()
  ```

- **头尾插入测试结果**

  ```python
  # 注意在头尾插入数据要特别注意插入结点后，结点在双链表中的位置
  测试添加模块：
  当前结点的元素值： 45
  当前结点的元素值： 465
  当前结点的元素值： 478
  当前结点的元素值： 78
  当前结点的元素值： 12
  当前结点的元素值： 79
  ```

- **插入测试结果**

  ```python
  测试插入模块：
  原始数据:
  当前结点的元素值： 45
  当前结点的元素值： 465
  当前结点的元素值： 478
  当前结点的元素值： 78
  当前结点的元素值： 12
  当前结点的元素值： 79
  --------------------
  首部添加元素：
  当前结点的元素值： 100
  当前结点的元素值： 45
  当前结点的元素值： 465
  当前结点的元素值： 478
  当前结点的元素值： 78
  当前结点的元素值： 12
  当前结点的元素值： 79
  --------------------
  中间添加元素：
  当前结点的元素值： 100
  当前结点的元素值： 45
  当前结点的元素值： 465
  当前结点的元素值： 478
  当前结点的元素值： 456456
  当前结点的元素值： 78
  当前结点的元素值： 12
  当前结点的元素值： 79
  --------------------
  尾部添加元素：
  当前结点的元素值： 100
  当前结点的元素值： 45
  当前结点的元素值： 465
  当前结点的元素值： 478
  当前结点的元素值： 456456
  当前结点的元素值： 78
  当前结点的元素值： 12
  当前结点的元素值： 79
  当前结点的元素值： 11111
  --------------------
  非法位置添加元素：
  非法位置插入数据！！！
  当前结点的元素值： 100
  当前结点的元素值： 45
  当前结点的元素值： 465
  当前结点的元素值： 478
  当前结点的元素值： 456456
  当前结点的元素值： 78
  当前结点的元素值： 12
  当前结点的元素值： 79
  当前结点的元素值： 11111
  
  ```

- **删除测试结果**

  ```python
  测试删除模块：
  原始数据:
  当前结点的元素值： 45
  当前结点的元素值： 465
  当前结点的元素值： 478
  当前结点的元素值： 78
  当前结点的元素值： 12
  当前结点的元素值： 79
  --------------------
  首部删除元素：
  当前结点的元素值： 465
  当前结点的元素值： 478
  当前结点的元素值： 78
  当前结点的元素值： 12
  当前结点的元素值： 79
  --------------------
  中间删除元素：
  当前结点的元素值： 465
  当前结点的元素值： 478
  当前结点的元素值： 12
  当前结点的元素值： 79
  --------------------
  尾部删除元素：
  当前结点的元素值： 465
  当前结点的元素值： 478
  当前结点的元素值： 12
  --------------------
  删除不存在的元素：
  所删除的元素不在链表中！
  --------------------
  当前结点的元素值： 465
  当前结点的元素值： 478
  当前结点的元素值： 12
  
  ```

  ## 总结

  ​		双链表的每一个节点都有两个方向的链接，因此可以高效地找到前后的结点，双链表的操作和基本单链表的操作大致相同，对于有些方法可以直接使用继承的方法来实现，这样即简化了双链表的操作，又使得代码更加简洁．
  
  [Python数据结构之基本双链表](https://github.com/Gavince/Python/tree/master/数据结构/单链表)
