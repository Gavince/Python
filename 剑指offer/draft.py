import heapq


class Solution:

    def getLeastNumbers(self, arr, k):

        if not arr:
            return list()

        # 构建最大堆
        hp = [-x for x in arr[:k]]

        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]

        return ans


print(Solution().getLeastNumbers([3, 2, 1], 2))