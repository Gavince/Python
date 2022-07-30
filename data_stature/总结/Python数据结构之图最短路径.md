## Python数据结构之最短路径

### 单源点最短路径之Dijkstra算法

算法步骤：

1. 把Ｖ分成两组

   (1) S: 以求出最短路径的顶点的集合

   (2) T = V - S : 尚未确定最短路径的顶点集合。

2. 将Ｔ中顶点<font color = red>按最短路径递增的次序</font>加入到Ｓ中。

**保证**：

（１）从源点$v_0$到Ｓ中各顶点的最短路径长度都不大于从$v_0$到Ｔ中任何顶点的最短路径长度。

（２）每个顶点对应一个距离值：

​		**Ｓ中顶点**：从$v_0$到此顶点的最短路径长度，

​		**Ｔ中顶点**：从$v_0$到此顶点的**只包括**Ｓ中顶点**作中间顶点**的最短路径长度。

代码：

(1) 访问顶点类

```python
class VisitedVertex:
    """访问顶点类"""

    def __init__(self, length: int, index: int):
        """
        :param length:顶点个数
        :param index: 查询的单原点
        """

        self.index = index
        self.ver = None

        self.already_array = [0] * length  # 标识已访问过的结点
        self.pre_visited = [0] * length  # 保存前驱结点中继节点
        self.dis = [float("inf")] * length  # 记录最短距离，初始化无穷

        # 初始化自身到自身的距离为0
        self.dis[index] = 0
        self.already_array[index] = 1

    def is_visited(self, index: int):
        """结点是否已经被访问"""

        return self.already_array[index] == 1

    def update_dis(self, index: int, length: int):
        """更新最短路径"""

        self.dis[index] = length

    def updata_pre(self, pre: int, index: int):
        """更新顶点的前驱结点"""

        self.pre_visited[pre] = index

    def get_dis(self, index: int):
        """得到距离"""
        return self.dis[index]

    def update_arr(self):

        min_val = float("inf")
        index = 0
        for i in range(len(self.already_array)):
            if self.already_array[i] == 0 and self.dis[i] < min_val:
                min_val = self.dis[i]
                index = i

        #  更新顶点
        self.already_array[index] = 1
        return index

    def show_result(self):

        print("输出结果：")
        for item in self.already_array:
            print(item, end=" ")

        print()
        for item in self.pre_visited:
            print(item, end=" ")
        print()

        for item in self.dis:
            print(item, end=" ")
        print()

        self.ver = Graph(vertex, matrix)
        count: int = 0
        for item in self.dis:
            if item != float("inf"):
                print("{}->{}:distance:{}".format(self.ver.vertex[self.index], self.ver.vertex[count], self.dis[count]))
                count += 1
```

(2) 创建邻接图

```python
class Graph:
    """构建图"""

    def __init__(self, vertex: [], matrix: []):

        self.vertex = vertex  # 顶点
        self.matrix = matrix  # 邻接矩阵
        self.vv = None

    def show_djs(self):

        self.vv.show_result()

    def show_graph(self):
        """显示图"""

        for col in self.matrix:
            print(col)

    def djs(self, index: int):
        """迪杰斯塔拉算法"""
        self.vv = VisitedVertex(len(self.vertex), index)
        # 　第一次更新直接相连的顶点
        self.updata(index)

        #  加入n-1个结点
        for j in range(1, len(self.vertex)):
            # 中间结
            index = self.vv.update_arr()
            # 　修改路径
            self.updata(index)

    def updata(self, index):
        """更最短S集合中的最短路径"""

        length: int = 0
        for j in range(len(self.matrix[index])):
            # 路径长度递增原则
            length = self.vv.get_dis(index) + self.matrix[index][j]
            
            # 第一前驱为查询结
            if not self.vv.is_visited(j) and length < self.vv.get_dis(j):
                self.vv.updata_pre(j, index)
                self.vv.update_dis(j, length)

if __name__ == "__main__":
    vertex: [] = ["A", "B", "C", "D", "E", "F", "G"]
    matrix: [] = [[0 for col in range(len(vertex))] for row in range(len(vertex))]
    # 用来表示一个极大的数
    F: float = float('inf')
    matrix[0] = [0, 5, 7, F, F, F, 2]
    matrix[1] = [5, 0, F, 9, F, F, 3]
    matrix[2] = [7, F, 0, F, 8, F, F]
    matrix[3] = [F, 9, F, 0, F, 4, F]
    matrix[4] = [F, F, 8, F, 0, 5, 4]
    matrix[5] = [F, F, F, 4, 5, 0, 6]
    matrix[6] = [2, 3, F, F, 4, 6, 0]
    g = Graph(vertex, matrix)
    g.show_graph()
    g.djs(6)
    g.show_djs()
```

### 多源点最短路之Floyd算法

目标：计算出图中各个顶点之间的最短路径

算法步骤：

​	初始时设置一个n阶方阵，令其对角线元素为０(即自身到自身的路径为0)，若存在弧$<v_i, v_j>$，则对应的元素为权重；否则为无穷。算法进行时，逐步试着在原路径中增加中间结点，若加入中间顶点后路径变短，则修改之；否则，维持原值。所有顶点试探完毕，算法结束。

代码：

1) 初始化矩阵1

```python
# matrix 为邻接矩阵形式
matrix[0] = [0, 5, 7, F, F, F, 2]
matrix[1] = [5, 0, F, 9, F, F, 3]
matrix[2] = [7, F, 0, F, 8, F, F]
matrix[3] = [F, 9, F, 0, F, 4, F]
matrix[4] = [F, F, 8, F, 0, 5, 4]
matrix[5] = [F, F, F, 4, 5, 0, 6]
matrix[6] = [2, 3, F, F, 4, 6, 0]
```

2) Floyd核心算法（<font color=red>不断询问新的结点的加入有没使得原来的路径更短</font>）

```python
    def floyd(self):
        """Floyd算法:"""

        length: int = 0
        for k in range(len(self.dis)):  #  中间结点(新节点)
            
            for i in range(len(self.dis)):
                for j in range(len(self.dis)):
                    length = self.dis[i][k] + self.dis[k][j]
                    if length < self.dis[i][j]:
                        self.dis[i][j] = length
                        self.pre[i][j] = self.pre[k][j]
```

### 参考

[数据结构与算法--弗洛伊德算法 Python实现弗洛伊德算法 一步一步带你实现弗洛伊德算法](https://blog.csdn.net/storyfull/article/details/104014992)

[数据结构与算法--迪杰斯特拉算法 Python实现迪杰斯特拉算法 一步一步带你用Python实现迪杰斯特拉算法](https://blog.csdn.net/storyfull/article/details/104014963)

[数据结构与算法基础--第11周08--6.6图的应用8--6.6.2最短路径3--Floyd算法](https://www.bilibili.com/video/BV1Ut41197NX?t=712)

[数据结构与算法基础--第11周07--6.6图的应用7--6.6.2最短路径2--Dijkstra算法](https://www.bilibili.com/video/av36886088)

