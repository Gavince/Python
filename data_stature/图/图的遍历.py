class Graph:

    def __init__(self, n):

        self.vertex_list = []  # 顶点列表
        self.edges = [[0 for i in range(n)] for i in range(n)]  # 边
        self.num_of_edges = 0  # 记录有效边
        self.is_visited = [0] * n

    def get_num_of_vertexs(self):
        """获取顶点数目"""

        return len(self.vertex_list)

    def get_num_of_edges(self):
        """获取有效边数目"""

        return self.num_of_edges

    def get_val_by_index(self, index):
        """指定索引值"""

        return self.vertex_list[index]

    def get_weight(self, v1, v2):
        """获得指定边的权重"""

        return self.num_of_edges[v1][v2]

    def show_graph(self):
        """显示图结构"""

        for col in self.edges:
            print(col)

    def insert_vertex(self, vertex):
        """插入顶点"""

        self.vertex_list.append(vertex)

    def insert_edge(self, v1, v2, weight):
        """插入边关系"""

        self.edges[v1][v2] = weight
        self.edges[v2][v1] = weight
        self.num_of_edges += 1

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


if __name__ == "__main__":
    graph = Graph(5)
    vertex_val = ["A", "B", "C", "D", "E"]
    for vertex in vertex_val:
        graph.insert_vertex(vertex)
    print("原始图结构：")
    graph.show_graph()
    graph.insert_edge(0, 1, 1)  # A-B
    graph.insert_edge(0, 2, 1)
    graph.insert_edge(1, 2, 1)
    graph.insert_edge(1, 3, 1)
    graph.insert_edge(1, 4, 1)
    print("增加边的结构：")
    graph.show_graph()
    print("DFS:")
    graph.dfs_override()
    # print("bfs:")
    # graph.bsf_override()