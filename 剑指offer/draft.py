import collections
from typing import List


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        deque = collections.deque()
        res, n = [], len(nums)

        # bianlishuzu
        for i, j in zip(range(1 - k, n - k + 1), range(n)):
            if i > 0 and deque[0] == nums[i - 1]: deque.popleft()
            while deque and deque[-1] < nums[j]: deque.pop()

            deque.append(nums[j])

            if i >= 0:
                res.append(deque[0])
        return res
