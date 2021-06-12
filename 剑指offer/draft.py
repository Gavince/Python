class Solution:

    def reconstructQueue(self, pepole):

        pepole = sorted(pepole, key = lambda x: (-x[0], x[1]))

        i = 0
        while i < len(pepole):
            if i > pepole[i][1]:
                # 插入后删除
                pepole.insert(pepole[i][1], pepole[i])
                pepole.pop(i + 1)
            i += 1

