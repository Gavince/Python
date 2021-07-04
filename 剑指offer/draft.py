class Solution:

    def twoSum(self, nums, target):
        """暴力求解"""

        hashtable = dict()

        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            # 整数对应value
            hashtable[num] = i
        return []
