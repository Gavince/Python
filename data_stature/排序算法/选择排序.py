"""
选择排序算法
选择排序（Selection sort）是一种简单直观的排序算法。
它的工作原理如下。首先在未排序序列中找到最小（大）元素，
存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，
然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

选择排序的主要优点与数据移动有关。如果某个元素位于正确的最终位置上，则它不会被移动。
选择排序每次交换一对元素，
它们当中至少有一个将被移到其最终位置上，因此对n个元素的表进行排序总共进行至多n-1次交换。
在所有的完全依靠交换去移动元素的排序方法中，选择排序属于非常好的一种
"""


def select_sort(li):
    """选择排序"""
    n = len(li)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if li[min_index] > li[j]:  # 找出最小索引
                min_index = j
        #  交换位置,使得第一个位置之最小
        li[min_index], li[i] = li[i], li[min_index]
    return li


def select_sort_reverse(li):
    """反向选择排序"""
    n = len(li)

    for i in range(n-1, -1, -1):
        max_index = i
        for j in range(i-1, -1, -1):
            if li[max_index] < li[j]:
                max_index = j

        # 交换索引位置
        li[i], li[max_index] = li[max_index], li[i]

    return li


if __name__ == "__main__":
    li = [1, 5, 2, 6, 6, 7, 9]
    print("select_sort:", select_sort(li))
    print("select_sort_reverse:", select_sort_reverse(li))