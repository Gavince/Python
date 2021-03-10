class Solution:

    def minNumber(self, nums):

        def quick(l, r):
            if l >= r:
                return

            low, hight = l, r
            while low < hight:
                while low < hight and strs[low] + strs[l] < strs[l] + strs[low]: low += 1
                while low < hight and strs[hight] + strs[l] >= strs[l] + strs[hight]: hight -= 1
                # change
                strs[low], strs[hight] = strs[hight], strs[low]
            strs[low], strs[l] = strs[l], strs[low]
            quick(l, low - 1)
            quick(low + 1, r)

        strs = [str(c) for c in nums]
        quick(0, len(strs) - 1)

        return "".join(strs)


if __name__ == "__main__":
    obj = Solution()
    print(obj.minNumber(nums=[3, 30, 34, 5, 9]))