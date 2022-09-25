class Graph:
    """创建图"""

    def __init__(self, n):
        self.vertex_list = []
        self.edges = [[0 for i in range(n)] for j in range(n)]
        self.num_of_edges = 0

    def get_num_of_vertex(self):
        """获取顶点数目"""
        return len(self.vertex_list)

    def get_val_by_index(self, index):
        """返回结点的下标"""
        return self.vertex_list[index]

    def get_wight(self, v1, v2):
        """获取变的权重"""
        return self.edges[v1][v2]

    def show_graph(self):

        for col in self.edges:
            print(col)

    def insert_edge(self, v1, v2, weight):
        """
        :param v1:源顶点
        :param v2: 目的顶点
        :param weight: 边权重
        :return:
        """
        self.edges[v1][v2] = weight
        self.edges[v2][v1] = weight
        self.num_of_edges += 1

    def insert_vertex(self, vertex):
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
