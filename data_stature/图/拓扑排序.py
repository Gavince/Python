"""
简介：在将一件事情分解为若干个小事情时，会发现小事情之间有完成的先后次序之分，
若不按照特定的顺序完成，则会使得整件事情无法完成。因此这需要获取工作安排表。
而拓扑排则怎能根据小事情之间的先后次序生成这样一个工作安排表（拓扑序列）。
但请注意，能满足要求的拓扑序列不止一个
"""
#
# def naiveTopoSort(G, S=None):
#     """拓扑排序"""
#     if S is None:
#         S = set(G.keys())
#         # print("S0", S)
#     if len(S) == 1:
#         return list(S)
#     s = S.pop()
#     # print("s", s)
#     seq = naiveTopoSort(G, S)
#     # print(seq)
#     minIdx = 0
#     for i, v in enumerate(seq):
#          if s in G[v]:
#              minIdx = i+1
#
#     seq.insert(minIdx, s)
#     return seq
# G={
#     'a':{'b''c','d','e','f'},
#     'b':{'c','d','e','f'},
#     'c':{'d','e','f'},
#     'd':{'e','f'},
#     'e':{'f'},
#     'f':{}
# }
# res=naiveTopoSort(G)
# print(res)

"""
1、在有向无环图中，用顶点表示活动，用有向边<u，v>表示活动u必须先与活动v,这种有向图叫AOV网络。
2、若<u，v>，则u是v的直接前驱，v是u的直接后继；若<u，u1，u2，···un，v>则称u是v的前驱，v是u的后继。
3、前驱后继关系有传递性和反自反性。则可以推断AOV网络必须是有向无环图。
4、拓扑排序实现方法：
    1）从AOV网络中选择一个入度为0的顶点并输出；
    2）从AOV网络中删除该顶点以及该顶点发出的所有边；
    3）重复1）和2），直到找不到入度为0的顶点；
    4）如果所有顶点都输出了则拓扑排序完成，否则说明此图是有环图。
"""
# 非递归算法
def topoSort(G):

    cnt = dict((u, 0) for u in G.keys())

    # 计算所有顶点的入度
    for u in G:
        for v in G[u]:
            cnt[v] += 1

    # 寻找源点
    Q = [u for u in cnt.keys() if cnt[u] == 0]

    seq = []
    while Q:
        s = Q.pop()
        seq.append(s)
        for u in G[s]:
            cnt[u] -= 1
            # 每一次添加入度为零的点
            if cnt[u] == 0:
                Q.append(u)
    return seq


G={
    'a':{'b','f'},
    'b':{'c','d','f'},
    'c':{'d'},
    'd':{'e','f'},
    'e':{'f'},
    'f':{}
}
res=topoSort(G)
print(res)