## Python数据结构之基本循环单链表

### 前言

​		单链表的另一常见变形是循环单链表（**简称循环链表**），其中最后一个结点的next域不用None，而是指向表的第一个结点，但是如果仔细考虑链表对象记录表尾结点更加重要．这样可以同时支持时间复杂度Ｏ(1)的表头/表尾插入和删除操作．

![循环单链表](/home/gavin/Python/数据结构/Picture/循环单链表.png)

### 循环链表的基本操作

#### 创建结点

- **代码**

  ```python
  class Node:
      """
      定义node节点
      """
      # 记录创建的节点数目
      count = 0
  
      def __init__(self, elem):
          self.elem = elem
          self.next = None
          Node.count += 1
  
      def __del__(self):
          Node.count -= 1
  ```

####  初始化循环单链表

-  **代码**

  ```python
  class CSlist:
      """
      创建循环单链表
      """
  
      def __init__(self):
          self.__head = None
  
      def is_empty(self):
          """判断空"""
          return self.__head is None
  ```

#### 获得结点个数

- **代码**

  ```python
      @staticmethod
      def get_length():
          """获得数据的长度"""
          print("创建的数据节点数目为：", Node.count)
          return Node.count
  ```

#### 头插法

- **图示**

  ![循环单链表头插法](/home/gavin/Python/数据结构/Picture/循环单链表头插法.png)

- **代码**

  ```python
      def add_head(self, elem):
          """头插法"""
  
          #  1. 申请插入节点
          node = Node(elem)
  
          #  2. 判断是否只有头结点
          if self.is_empty():
              self.__head = node
              node.next = self.__head
          else:
              cur = self.__head  # 循环遍历结点
              #  3.找到链表的结尾
              while cur.next != self.__head:
                  cur = cur.next
              #  4. 插入node 节点
              node.next = self.__head
              cur.next = node
              self.__head = node  # 重新找到头结点
  ```

  

#### 尾插法

- **图示![循环单链表尾插法](/home/gavin/Python/数据结构/Picture/循环单链表尾插法.png)**

- **代码**

  ```python
      def add_rear(self, elem):
          """尾插法"""
          #  1. 申请节点
          node = Node(elem)
  
          #  2.判断节点是否为单一节点
          if self.is_empty():
              self.__head = node
              node.next = self.__head
          else:
              cur = self.__head　# 用作遍历
              while cur.next != self.__head:
                  cur = cur.next
              cur.next = node
              node.next = self.__head
  ```

#### 遍历循环链表

- **代码**

  ```python
      def travel(self):
          """遍历整个链表"""
  
          #  1.判断是否为空节点
          if self.is_empty():
              print("空链表！")
              return 0
          #  2. 设置遍历指针
          cur = self.__head
          while cur.next != self.__head:  # 保证遍历不会进入死循环
              print("Current data is :", cur.elem)
              cur = cur.next
          print("Current data is :", cur.elem)  # 输出最后一个结点元素
  ```

#### 指定位置插入数据结点

 - **代码**

   ```python
       def insert_data(self,pos ,elem):
           """插入数据"""
           
           #  0.判断插入位置是否合法
           index = self.get_length()
           if (pos < 1) or (int(pos) > index):
               print("插入位置错误！")
               return
           
           #  1.插入点在链表的开头（头插法）
           if pos == 1
               self.add_head(elem)
               
           #  2.插入点在链表的末尾（尾插法）
           elif pos == (self.get_length()):
               self.add_rear(elem)
               
           #  3.插入点在链表的中间
           else:
               cur = self.__head
               node = Node(elem)
               
               # 3.1 查找指点位置
               while pos:
                   pos -= 1
                   cur = cur.next
                   
               # 3.2 插入节点
               node.next = cur.next
               cur.next = node
   ```

#### 删除指定元素数据

- **代码**

  ```python
      def del_data(self, elem):
          """删除指定数据的节点"""
  
          #  1. 判断是否为节点
          if self.is_empty():
              print("请先添加数据！！！")
              return
          
          # 寻找指定数据的节点
          cur = self.__head
          if cur.elem == elem:
              #  2.0 直接在第一次就找到了数据节点
              #  此时先要删除头结点
              #  2.1判断数据是否只有头结点
              if cur.next != self.__head:
                  # 2.2 第一个节点非空
                  while cur.next != self.__head:
                      cur = cur.next
                  #  2.3 删除节点
                  self.__head = self.__head.next
                  cur.next = self.__head
              else:
                  self.__head = None
          else:
              # 3.0 在中间找到元素节点和尾部找到节点
              # 3.1 遍历
              pre = self.__head
              while cur.next != self.__head:
                  if cur.elem == elem:
                      pre.next = cur.next
                      #  继续寻找下一个可以删除的结点
                      pre = cur
                      cur = cur.next
                  else:
                      pre = cur
                      cur = cur.next
              # 3.2 此时退出层循环,在尾部查找数据
              if cur.elem == elem:
                  pre.next = self.__head
              else:
                  print("所查找的数据未存入！！！")
                  return
  ```

### 测试模块

- **测试代码**

  ```python
  class TestModule:
      """
      测试模块
      """
  
      def test_add(self):
          """测试插入模块"""
  
          print("插入数据显示：")
          clist.add_head(12)
          clist.add_head(45)
          clist.add_head(455)
          clist.add_rear(100)
          clist.add_rear(45)
          clist.travel()
  
      def test_del(self):
          """测试删除模块"""
  
          print("原始数据：")
          clist.travel()
          clist.del_data(45)
          print("删除指定元素：")
          clist.travel()
          print("删除第一个结点元素：")
          clist.del_data(455)
          clist.travel()
          print("删除最后一个结点元素：")
          clist.del_data(100)
          clist.travel()
          print("删除链表最后一个元素：")
          clist.del_data(12)
          clist.travel()
  ```

- **测试插入模块结果**

  ```python
  插入数据显示：
  Current data is : 455
  Current data is : 45
  Current data is : 12
  Current data is : 100
  Current data is : 45
  ```

- **测试删除模块结果**

  ```python
  原始数据：
  Current data is : 455
  Current data is : 45
  Current data is : 12
  Current data is : 100
  Current data is : 45
  删除指定元素（45）：
  Current data is : 455
  Current data is : 12
  Current data is : 100
  删除第一个结点元素：
  Current data is : 12
  Current data is : 100
  删除最后一个结点元素：
  Current data is : 12
  删除链表最后一个元素：
  空链表！
  ```

### 总结

​		循环单链表支持高效的表首端/尾端插入和首端弹出元素，在这种表上扫描，需要特别注意结束判断的问题．尤其是在插入和删除操作时，特别要注意一些特定边界值的选定，如果在编写代码时，出现了一些边界值的错误，一定要善于运用Debug调试，这样能使的代码更加具有稳定性．代码链接如下：

[Python数据结构之基本循环单链表]()