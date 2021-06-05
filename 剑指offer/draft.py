class Solution:

    def permute(self, nums):
        res = []

        def dfs(x):
            # 回朔的终点
            if x == len(nums) - 1:
                res.append(nums[:])
            dic = set()
            for i in range(x, len(nums)):
                # 消除重节点
                if nums[i] in dic: continue
                dic.add(nums[i])

                # change position
                nums[i], nums[x] = nums[x], nums[i]
                dfs(x + 1)
                nums[i], nums[x] = nums[x], nums[i]
        dfs(0)
        return res
