## Python数据结构之图基础

### 什么是图？

<img src="../Picture/graph.png" style="zoom:50%;" />

- 表示多对多的关系
- 一组顶点，通常用V(Vertex)表示顶点集合
- 一组边，通常用E(Edge)表示边的集合，边是顶点对，分为有向边和无向边

### 图的创建

#### 邻接矩阵

- 代码

  ```python
  class Graph:
      """创建图"""
  
      def __init__(self, n):
          
          self.vertex_list = []
          self.edges = [[0 for i in range(n)] for j in range(n)]  # 初始化图
          self.num_of_edges = 0  #　记录有效边数目
  
      def get_num_of_vertex(self):
          """获取顶点数目"""
          return len(self.vertex_list)
  
      def get_val_by_index(self, index):
          """返回结点的下标"""
          return self.vertex_list[index]
  
      def get_wight(self, v1, v2):
          """获取边的权重"""
          return self.edges[v1][v2]
  
      def show_graph(self):
  
          for col in self.edges:
              print(col)
  
      def insert_edge(self, v1, v2, weight):
          """插入边"""
  
          self.edges[v1][v2] = weight
          self.edges[v2][v1] = weight
          self.num_of_edges += 1
  
      def insert_vertex(self, vertex):
          """插入顶点"""
          
          self.vertex_list.append(vertex)
          
          
  if __name__ == "__main__":
      graph = Graph(5)
      print("原始图结构：")
      vertex_val = ["A", "B", "C", "D", "E"]
      for vertex in vertex_val:
          graph.insert_vertex(vertex)
      graph.show_graph()
      graph.insert_edge(1, 2, 5)
      graph.insert_edge(2, 4, 6)
      graph.insert_edge(3, 1, 4)
      graph.insert_edge(2, 2, 5)
      print("增加边的结构：")
      graph.show_graph()
  ```

- 结果

  ```python
  原始图结构：
  [0, 0, 0, 0, 0]
  [0, 0, 0, 0, 0]
  [0, 0, 0, 0, 0]
  [0, 0, 0, 0, 0]
  [0, 0, 0, 0, 0]
  增加边的结构：
  [0, 0, 0, 0, 0]
  [0, 0, 5, 4, 0]
  [0, 5, 5, 0, 6]
  [0, 4, 0, 0, 0]
  [0, 0, 6, 0, 0]
  ```

- 结论

  ​		使用邻接矩阵的形式实现图结构，能够更加直观的理解顶点之间的关系，也能够很好的计算相应顶点的出度和入度，但是，对于无向图而言，邻接矩阵的使用，会同时保存两个顶点之间的的两条边关系，造成存储浪费，所以，可以使用一维列表之间进行存储，减少一半的存储关系或者使用邻接表的方式。

#### 邻接表

- 代码

  ```python
  class Vertex:
      """创建顶点类"""
  
      def __init__(self, key):
          self.id = key
          self.connectedTo = {}
  
      def add_neighbor(self, nbr, weight):
          self.connectedTo[nbr] = weight
  
      def __str__(self):
          return str(self.id) + " connected to " + str([x.id for x in self.connectedTo])
  
      def get_connections(self):
          return self.connectedTo.keys()
  
      def get_id(self):
          return self.id
  
      def get_weight(self, nbr):
          return self.connectedTo[nbr]
  
  
  class Graph:
  	"""创建图"""
      
      def __init__(self):
          self.vertList = {}
          self.numVertice = 0
  
      def add_vertex(self, key):
          self.numVertice += 1
          newVertex = Vertex(key)
          self.vertList[key] = newVertex  # 添加新的顶点
          return newVertex
  
      def get_vertex(self, n):
          if n in self.vertList:
              return self.vertList
          else:
              return None
  
      def __contains__(self, item):
          return n in self.vertList
  
      def add_edge(self, f, t, cost=0):
          if f not in self.vertList:
              nv = self.add_vertex(f)
              
          if t not in self.vertList:
              nv = self.add_vertex(t)
              
          self.vertList[f].add_neighbor(self.vertList[t], cost)
  
      def get_vertics(self):
          return self.vertList.keys()
  
      def __iter__(self):
          return iter(self.vertList.values())
  
  
  if __name__ == "__main__":
      g = Graph()
      for i in range(6):
          g.add_vertex(i)
  
      g.add_edge(0,1,5)
      g.add_edge(0,5,2)
      g.add_edge(1,2,4)
      g.add_edge(2,3,9)
      g.add_edge(3,4,7)
      g.add_edge(3,5,3)
      g.add_edge(4,0,1)
      g.add_edge(5,4,8)
      g.add_edge(5,2,1)
  
      for x in g:
          print(x)
  ```

- 结果

  ``` python
  0 connected to [1, 5]
  1 connected to [2]
  2 connected to [3]
  3 connected to [4, 5]
  4 connected to [0]
  5 connected to [4, 2]
  ```

- 结论

  ​		在python中可以使用字典来实现图邻接表的形式，对其而言，能较为方便的查找任一顶点的所有邻接点，减少了稀疏图（点多边少）占存储空间的麻烦，可以直观的计算出任一顶点的出度（有向图），但是，入度无法很好计算得出。

### 图的遍历

#### DFS（深度优先搜索）

​		DFS的实现过程与树的先序号遍历相同，DFS的实现过程中要设置相应的顶点访问标识，已经访问过的结点不在访问，实现过程最重要的是状态的回溯，可以使用递归。算法通俗理解：一条道走到黑（选择），不行就撤（回溯），已走过不在重复（状态标识）。

- 代码

  ```python
    def get_first_neighbor(self, index):
          """查询第一关系边顶点"""
          
          for j in range(self.get_num_of_vertexs()):
              if self.edges[index][j] > 0:
                  return j
  
          return -1
  
      def get_next_neighbor(self, v1, v2):
          """查询第二个结点"""
  
          for j in range(v2 + 1, self.get_num_of_vertexs()):
              if self.edges[v1][j] > 0:
                  return j
  
          return -1
      
      def dfs(self, is_visited, i):
          """深度优先查找"""
  
          print(self.get_val_by_index(i), "->", end=" ")
          self.is_visited[i] = True
  
          first = self.get_first_neighbor(i)
  
          while first != -1:
              if not self.is_visited[first]:
                  self.dfs(is_visited, first)  # 递归遍历
       			
              first = self.get_next_neighbor(i, first)
  
      def dfs_override(self):
          """遍历每一个子图"""
          
          for i in range(self.get_num_of_vertexs()):
              if not self.is_visited[i]:
                  self.dfs(self.is_visited, i)
  ```

#### BFS（广度优先搜素）

​		BFS相当于树的层序遍历，可以使用队列对顶点进行存储搜索，让后先进后出的对顶点的有效边顶点进行搜索，已搜索过的便不再搜素，所以，要标识顶点的搜索状态。

- 代码

  ```python
    def get_first_neighbor(self, index):
          """查询第一关系边顶点"""
          
          for j in range(self.get_num_of_vertexs()):
              if self.edges[index][j] > 0:
                  return j
  
          return -1
  
      def get_next_neighbor(self, v1, v2):
          """查询第二个结点"""
  
          for j in range(v2 + 1, self.get_num_of_vertexs()):
              if self.edges[v1][j] > 0:
                  return j
  
          return -1
  
      def bfs(self, is_visited, i):
          """宽度优先搜索"""
  
          queue = []
          print(self.get_val_by_index(i) + "->", end=" ")
          self.is_visited[i] = True
          queue.append(i)
  
          while queue:
              u = queue.pop(0)
              w = self.get_first_neighbor(u)
  
              while w != -1:
                  if not is_visited[w]:
                      print(self.get_val_by_index(w), "->", end=" ")
                      self.is_visited[w] = True
                      queue.append(w)
                  w = self.get_next_neighbor(u, w)
  
      def bsf_override(self):
  
          for j in range(self.get_num_of_vertexs()):
              if not self.is_visited[j]:
                  self.bfs(self.is_visited, j)
  ```

### 参考

[搜索思想——DFS & BFS（基础基础篇](https://zhuanlan.zhihu.com/p/24986203)

[邻接表]([https://facert.gitbooks.io/python-data-structure-cn/7.%E5%9B%BE%E5%92%8C%E5%9B%BE%E7%9A%84%E7%AE%97%E6%B3%95/7.5.%E9%82%BB%E6%8E%A5%E8%A1%A8/](https://facert.gitbooks.io/python-data-structure-cn/7.图和图的算法/7.5.邻接表/))

[数据结构与算法--图 一步一步带你用Python实现图的深度遍历和广度优先遍历 Python实现图的深度遍历和广度优先遍历 Python详解DFS和BFS过程](https://blog.csdn.net/storyfull/article/details/103858521)