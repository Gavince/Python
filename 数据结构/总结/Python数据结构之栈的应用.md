## Python数据结构之的的应用

### 括号匹配问题

- **算法描述**

  ​		在许多正文中都有括号，特别是在表示程序，数学表达式的正文里，括号有正确配对问题，每种括号都包括一个开括号和一个闭括号，相互对应．括号括起的片段可能嵌套，各种括号应该正确地嵌套并分别配对．

  ​		**配对原则**:在扫描正文时，**<font color = red>遇到的闭括号应该与此前最近遇到的且尚未获得匹配的开括号配对</font>**，若果不匹配，则匹配失败，正文中存在不能匹配的括号．

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
  		
          stack.reverse()　# 列表翻转
          print("Stack is :", stack)
  
  
  def check_parents(text):
      """检查括号"""
      parents = "{}[]()"
      open_parents = "{[("
      opposite = {"}": "{", "]": "[", ")": "("}
  
      def parentheses(text):
  
          i, len_text = 0, len(text)
          while True:
              while i < len_text and text[i] not in parents:
                  i += 1
              if i >= len_text:
                  return
              yield i, text[i]
              i += 1
  
      lstack = LStack()
      for i, pr in parentheses(text):
          if pr in open_parents:
              lstack.push(pr)
              lstack.show()
  
          elif lstack.pop() != opposite[pr]:
              print("括号不比配！")
              return
  
      if lstack.get_length() == len(text) or lstack.get_length() != 0: # 当括号全为单侧或者文本扫描完成还未匹配的括号
          print("括号不匹配！")
          return
  
      print("括号匹配真确！")
  
  
  if __name__ == "__main__":
      text = "(("
      check_parents(text)
  ```

  **测试 ：text = "((((((((("**

  ```python
  Stack is : ['(']
  Stack is : ['(', '(']
  Stack is : ['(', '(', '(']
  Stack is : ['(', '(', '(', '(']
  Stack is : ['(', '(', '(', '(', '(']
  Stack is : ['(', '(', '(', '(', '(', '(']
  Stack is : ['(', '(', '(', '(', '(', '(', '(']
  Stack is : ['(', '(', '(', '(', '(', '(', '(', '(']
  Stack is : ['(', '(', '(', '(', '(', '(', '(', '(', '(']
  括号不匹配！
  ```

  **测试： text = "((((((((()"**

  ```python
  Stack is : ['(']
  Stack is : ['(', '(']
  Stack is : ['(', '(', '(']
  Stack is : ['(', '(', '(', '(']
  Stack is : ['(', '(', '(', '(', '(']
  Stack is : ['(', '(', '(', '(', '(', '(']
  Stack is : ['(', '(', '(', '(', '(', '(', '(']
  Stack is : ['(', '(', '(', '(', '(', '(', '(', '(']
  Stack is : ['(', '(', '(', '(', '(', '(', '(', '(', '(']
  括号不匹配！
  ```

  **测试：text = "{({}[])[()()()()][]}"**

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

  **测试： text = "("**

  ```python
  Stack is : ['(']
  括号不匹配！
  ```

- **总结**

  ​		本算法实现原理较为简单，主要使用了栈先进后出的原则，**这样使得栈顶每一次都是那个最近的且未匹配的括号**，初次之外，在编写代码的过程中，使用了迭代器，使得每次的扫描变得简单，在对文本进行扫描匹配时，对一些特殊值也进行了处理，尤其是边界值．如无括号，只有单侧括号，只有最后一个括号匹配等．总之，在最后的代码完成后，要多次测试，以增强代码的稳定性．

### 表达式的表示和计算

### 栈与递归



