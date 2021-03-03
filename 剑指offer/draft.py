class Solution:

    def findRepeatNumber(self, nums: [int]) -> int:

        dic = set()

        for num in nums:
            if num in dic: return num
            dic.add(num)

        return -1

    def findRepeatNumber1(self, nums: [int]) -> int:

        i = 0

        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1