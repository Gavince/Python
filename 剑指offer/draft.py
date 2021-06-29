class Solution:

    def countBits(self, n: int):
        def countOnes(x):
            ones = 0
            while x > 0:
                x &= (x - 1)
                ones += 1
            return ones

        res = [countOnes(x) for x in range(n + 1)]

        return res
