class Graph:

    def __init__(self, length:int, matrix:[], vertex:[]):
        """
        :param length:大小
        :param matrix: 邻接矩阵
        :param vertex: 顶点
        """
        self.dis = matrix
        self.pre = [[0 for col in range(length)] for row in range(length)]
        self.vertex = vertex

        # 初始化前驱
        for i in range(length):
            for j in range(length):
                self.pre[i][j] = i

    def show_graph(self):

        # 打印访问结点的前驱
        for k in range(len(self.dis)):
            for i in range(len(self.dis)):
                print(self.vertex[self.pre[k][i]], end=" ")

            print()

            # 打印各个结点到其他结点最短路径
            for i in range(len(self.dis)):
                print("{}到{}的最短路径是{}".format(self.vertex[k]
                                             , self.vertex[i], self.dis[k][i]))

            print()
            print()

    def floyd(self):
        """Floyd算法:"""

        length: int = 0
        for k in range(len(self.dis)):  #  中间结点遍历
            for i in range(len(self.dis)):
                for j in range(len(self.dis)):
                    length = self.dis[i][k] + self.dis[k][j]
                    if length < self.dis[i][j]:
                        self.dis[i][j] = length
                        self.pre[i][j] = self.pre[k][j]


if __name__ == "__main__":
    if __name__ == '__main__':
        vertex: [] = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        # 邻接矩阵
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
        g = Graph(len(vertex), matrix, vertex)
        # 调用弗洛伊德算法
        g.floyd()
        g.show_graph()







