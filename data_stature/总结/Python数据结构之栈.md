## Python数据结构之栈

### 前言

**容器：**作为容器数据结构，它们保证存入的元素被保存在容器里，尚未明确删除的元素总是可以访问，而取出并删除的元素就不再存在于容器中了．

**栈：**栈主要用于在计算过程中保存临时的数据，这些数据是计算中发现或者产生的，在后面的计算中可能需要使用它们．栈是最简单的缓存结构，它支持数据项的存储和访问，<font color = red>不支持数据项之间的任何关系</font>．栈遵循的原则是：<font color = #0099ff>后进先出（LIFO）</font>

**栈的应用环境：**

- 计算过程分为一些顺序进行的步骤（任何复杂一点的计算都是这样）．
- 计算中执行的某些步骤会不断产生一些后面可能需要的中间数据 ．
- 产生的数据中有些不能立即使用，但有需要在将来使用． 
- 需要保存的数据项数不能事先（在编程序的时候）确定

**栈的图示：**

![栈](/home/gavin/Python/数据结构/Picture/栈.png)

### 栈的基本操作

#### 栈的抽象数据类型

```python
ADT Stack:

    Stack:Stack(self) #创建空栈
    is_ empty(self)  #判断栈是否为空，空时返回True否则返回False
    push(self,elem)  #将元素elem加人栈，也常称为压入或推入
    pop(self) #删除栈里最后压人的元素并将其返回，常称为弹出
    top(self) #取得栈里最后压人的元素，不删除
```

#### 栈的顺序表实现

- **说明**

  ​		对于顺序表，后端插入和删除是O(1)操作，应该用这一端作为栈顶

- **代码**

  ```python
  class SStack:
      """
      创建一个栈类(原则：FILO)
      """
  
      def __init__(self):
          self._elems = []
  
      def is_empty(self):
          """判断空"""
          return self._elems == []
  
      def top(self):
          """显示最后一个元素"""
          if self.is_empty():
              print("栈空！！！")
          else:
              return self._elems[-1]
  
      def push(self, elem):
          """添加元素"""
          self._elems.append(elem)
  
      def pop(self):
          """删除元素"""
          if self.is_empty():
              print("栈空！！！")
          else:
              return self._elems.pop()  # 默认pop出栈底元素
  
      def show(self):
          print("SStack :", self._elems)
  
          
  if __name__ == "__main__":
       # １．顺序栈
      sstack = SStack()
      sstack.pop()
      sstack.push(1)
      sstack.push(2)
      sstack.push(3)
      sstack.show()
      print("Top:",sstack.top())
      sstack.pop()
      sstack.show()
  ```

- **结果**

  ```python
  栈空！！！
  SStack : [1, 2, 3]
  Top: 3
  SStack : [1, 2]
  ```

#### 栈的链接表实现

- **说明**

  ​		对于链接表，前端插入和删除都是Ｏ(1)操作，应该用这端作为栈顶．具体操作为基本单链表<font color=##009ff>头插法和头删法</font>

- **代码**

  ```python
  class Node:
      """
      链表结点
      """
  
      def __init__(self, elem):
          self.elem = elem
          self.next = None
  
  
  class LStack:
      """
      创建一个链表栈(原则：FILO)
      """
  
      def __init__(self):
          self._top = None
  
      def is_empty(self):
          """判断空"""
          return self._top is None
  
      def pop(self):
          """表头删除栈顶元素()"""
          if self.is_empty():
              print("空栈！！！")
          else:
              self._top = self._top.next
  
      def top(self):
          """查看栈顶结点"""
          if self.is_empty():
              print("空栈！！！")
          else:
              return self._top.elem
  
      def push(self, elem):
          """表头栈顶添加元素"""
  
          # 1.创建结点
          node = Node(elem)
          # 2.判断结点类型
          if self.is_empty():
              self._top = node
          else:
              node.next = self._top
              self._top = node
  
      def show(self):
          """显示栈"""
          stack = []
  
          if self.is_empty():
              print("栈空！！！")
          else:
              cur = self._top
              while cur:
                  stack.append(cur.elem)
                  cur = cur.next
              print("Stack :", stack)
  
              
  if __name__ == "__main__":
      lstack = LStack()
      lstack.push(1)
      lstack.push(2)
      lstack.push(3)
      print("Top:",lstack.top())
      lstack.show()
      lstack.pop()
      lstack.show()
      lstack.pop()
      lstack.show()
  ```

- **结果**

  ```python
  Top: 3
  Stack : [3, 2, 1]
  Stack : [2, 1]
  Stack : [1]
  ```

### 栈的应用

  #### 括号匹配问题

- **问题说明**

  ​		输入一段序列，判断序列中的括号是否一一对应，遵循最近原则匹配成功，则这一对括号匹配，以此检测所有的括号的匹配状态．

- **代码**

  ```python
  class Node:
      """栈节点"""
  
      def __init__(self, elem):
          self.elem = elem
          self.next = None
  
  
  class LStack:
      """创建顺序栈"""
  
      def __init__(self):
          """初始化栈顶指针"""
          self._top = None
  
      def is_empty(self):
          return self._top is None
  
      def push(self, elem):
          """压栈"""
  
          node = Node(elem)
          if self.is_empty():
              self._top = node
          else:
              node.next = self._top
              self._top = node
  
      def pop(self):
          """出栈"""
  
          if self.is_empty():
              print("空栈！！！")
              return
          pop_elem = self._top.elem
          self._top = self._top.next
          return pop_elem
  
      def top(self):
          """显示栈顶元素"""
  
          if self.is_empty():
              print("空栈！！！")
          else:
              return self._top.elem
  
      def get_length(self):
          """获得栈中元素"""
  
          stack = []
          if self.is_empty():
              return 0
          else:
              cur = self._top
              while cur:
                  stack.append(cur.elem)
                  cur = cur.next
  
          return len(stack)
  
      def show(self):
          """显示栈数据"""
  
          stack = []
          if self.is_empty():
              print("空栈！！！")
          else:
              cur = self._top
              while cur:
                  stack.append(cur.elem)
                  cur = cur.next
                  
          stack.reverse()
          print("Stack is :", stack)
  
  
  def check_parents(text):
      """检查括号"""
      parents = "{}[]()"
      open_parents = "{[("
      opposite = {"}": "{", "]": "[", ")": "("}
  
      def parentheses(text):
  
          i, len_text = 0, len(text)
          while True:
              while i < len_text and text[i] not in parents:  # 找括号
                  i += 1
              if i >= len_text:  
                  return
              yield i, text[i]  # 找到括号
              i += 1
  
      lstack = LStack()
      for i, pr in parentheses(text):
          if pr in open_parents:
              lstack.push(pr)
              lstack.show()
  
          elif lstack.pop() != opposite[pr]:　　# 最近匹配原则
              print("括号不比配！")
              return
  
      if lstack.get_length() == len(text) or lstack.get_length() != 0:　#特殊情况处理：1．全为左括号　２．出现({{} 只有最后一对括号匹配
          print("括号不匹配！")
          return
  
      print("括号匹配真确！")
  
  
  if __name__ == "__main__":
      text = "{({}[])[()()()()][]}"
      check_parents(text)
  
  ```

- **结果**

  ```python
  Stack is : ['{']
  Stack is : ['{', '(']
  Stack is : ['{', '(', '{']
  Stack is : ['{', '(', '[']
  Stack is : ['{', '[']
  Stack is : ['{', '[', '(']
  Stack is : ['{', '[', '(']
  Stack is : ['{', '[', '(']
  Stack is : ['{', '[', '(']
  Stack is : ['{', '[']
  括号匹配真确！
  ```

  