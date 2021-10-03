class Solution:
    def LIS(self , arr ):
        # write code here
        n = len(arr)
        if n < 2:
            return n
        # 设定初始状态
        dp = [1]*n
        # 状态转移
        for i in range(n):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
         # 获取序列
        m = max(dp)
        index = dp.index(m)
        res = [0]*m
        m -= 1
        res[m] = arr[index]
        for i in range(index, -1, -1):
            if arr[i] < arr[index] and dp[i] == dp[index] - 1:
                m -= 1
                res[m] = arr[i]
                index = i
        return res

if __name__ == "__main__":
  obj = Solution()
  print(obj.LIS([1, 2, 4, 3, 6]))
