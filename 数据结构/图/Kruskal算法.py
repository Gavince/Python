# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 下午2:27
# @Author  : gavin
# @FileName: Kruskal算法.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


class GMap:

    def __init__(self, vertex_data: [], matrix: []):
        self.edge_num = 0
        self.vertex_data = vertex_data
        self.matrix = matrix

        self.inf = float("inf")

        #  构建有效边数(不统计重复边)
        for i in range(len(vertex_data)):
            for j in range(i+1, len(vertex_data)):
                if self.matrix[i][j] != self.inf:
                    self.edge_num += 1

    def show_graph(self):

        for i in range(len(self.vertex_data)):
            for j in range(len(self.vertex_data)):
                print(self.matrix[i][j], end=" ")
            print()

    def sort_edges(self, edges: []):
        """对边进行排序(冒泡),有小到大"""

        for i in range(len(edges) - 1):
            flag = False
            for j in range(len(edges) - 1 - i):
                if edges[j].weight > edges[j + 1].weight:
                    edges[j], edges[j + 1] = edges[j + 1], edges[j]
                    flag = True
            if not flag:
                break

    def get_position(self, ver_data: str):
        """查指定顶点的下标"""

        for i in range(len(self.vertex_data)):
            if self.vertex_data[i] == ver_data:
                return i

        return -1

    def get_edges(self):
        """统计所有顶点之间的有效边"""

        index = 0
        edges = [0] * self.edge_num
        for i in range(len(self.vertex_data)):
            for j in range(i+1, len(self.vertex_data)):
                if self.matrix[i][j] != self.inf:
                    edges[index] = EData(self.vertex_data[i]
                                         , self.vertex_data[j]
                                         ,self.matrix[i][j])
                    index += 1

        return edges

    def get_end(self, ends:[], i:[]):

        while ends[i] != 0:
            i = ends[i]
        return i

    def kruskal(self):
        """加边法"""

        index: int = 0
        ends: [] = [0] * self.edge_num

        #  最终的有效边
        result = [0] *self.edge_num
        edges = self.get_edges()
        self.sort_edges(edges)  # 排序

        # 按照边的大小,从小到达依次加边(判断是否存在回路)
        for i in range(self.edge_num):
            p1: int = self.get_position(edges[i].start)
            p2: int = self.get_position(edges[i].end)

            m: int = self.get_end(ends, p1)
            n: int = self.get_end(ends, p2)

            # 终点相同,则构成回路
            if m != n:
                ends[m] = n
                result[index] = edges[i]
                index += 1

        print("Kruskal算法下的最小生成树为：")
        for item in result:
            if item == 0:
                continue
            else:
                print("<%s, %s>=%d" % (item.start
                                       , item.end
                                       , item.weight)
                      , end=" ")


class EData(object):

    """ 存放边有效边之间的数据 """
    def __init__(self, start: str, end: str, weight: int):
        self.start = start
        self.end = end
        self.weight = weight


if __name__ == "__main__":
    char_vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    '''用 浮点型 最大值 float('inf') '''
    array_matrix = [[0, 12, float('inf'), float('inf'), float('inf'), 16, 14],
                    [12, 0, 10, float('inf'), float('inf'), 7, float('inf')],
                    [float('inf'), 10, 0, 3, 5, 6, float('inf')],
                    [float('inf'), float('inf'), 3, 0, 4, float('inf'), float('inf')],
                    [float('inf'), float('inf'), 5, 4, 0, 2, 8],
                    [16, 7, 6, float('inf'), 2, 0, 9],
                    [14, float('inf'), float('inf'), float('inf'), 8, 9, 0]]
    g = GMap(char_vertex, array_matrix)
    # g2 = GMap(char_vertex, array_matrix)
    # array = g.get_edges()
    # g2.sort_edges(array)
    # for item in array:
    #     print(item.weight)
    # print("*"*10)
    g.show_graph()
    for item in g.get_edges():

        print(item)
        print(item.start, item.end, item.weight, end="|")


    print()
    print("总共的有效边数目", g.edge_num)

    g.kruskal()