# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 下午2:12
# @Author  : gavin
# @FileName: prime算法.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
# 加点法


class MGraph:

    def __init__(self, vertex):
        self.vertex = vertex  # 顶点数目
        self.data = vertex * [0]  # 顶点
        self.weight = [[0 for row in range(vertex)] for col in range(vertex)]


class MinTree:

    @staticmethod
    def create_graph(graph, vertex_num: int, data: [], weight: []):

        for i in range(vertex_num):
            graph.data[i] = data[i]
            for j in range(vertex_num):
                graph.weight[i][j] = weight[i][j]

    def show_graph(self, graph):

        for link in graph.weight:
            print(link)

    def prim_algorithm(self, graph, v: int):
        """加点法"""

        visited = [0] * graph.vertex  # 表示已访问的结点
        visited[v] = 1  # 初始结点
        v1 = -1
        v2 = -1
        min_weight = float("inf")

        # 遍历n-1次，寻找n-1条边,构成最小生成树
        for k in range(1, graph.vertex):

            # 遍历寻找具有最小的边的两个顶点
            for i in range(graph.vertex):
                for j in range(graph.vertex):
                    #  寻访问结与未访问结点之间的最小权值边
                    if visited[i] == 1 and visited[j] == 0 and graph.weight[i][j] < min_weight:
                        min_weight = graph.weight[i][j]
                        v1 = i
                        v2 = j

            print("边 %s--> %s 权值: %d " % (graph.data[v1]
                                          , graph.data[v2]
                                          , graph.weight[v1][v2]))
            # 更新
            visited[v2] = 1
            min_weight = float("inf")


if __name__ == "__main__":
    vertex_data = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    weights = [[10000, 5, 7, 10000, 10000, 10000, 2],
               [5, 10000, 10000, 9, 10000, 10000, 3],
               [7, 10000, 10000, 10000, 8, 10000, 10000],
               [10000, 9, 10000, 10000, 10000, 4, 10000],
               [10000, 10000, 8, 10000, 10000, 5, 4],
               [10000, 10000, 10000, 4, 5, 10000, 6],
               [2, 3, 10000, 10000, 4, 6, 10000]]

    g = MGraph(len(vertex_data))
    tree = MinTree()
    tree.create_graph(g, len(vertex_data), vertex_data, weights)
    tree.show_graph(g)
    tree.prim_algorithm(g, 0)
