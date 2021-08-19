class Solution:

    def mergeSort(self, arr):

        if len(arr) <= 1:
            return arr

        # 划分点
        mid = len(arr) // 2
        left, right = arr[:mid], arr[mid:]
        return self.merge(self.mergeSort(left), self.mergeSort(right))

    def merge(self, left, right):

        result = []
        # 共同部分
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        # 剩余部分
        while left:
            result.append(left.pop(0))
        while right:
            result.append(right.pop(0))

        return result
