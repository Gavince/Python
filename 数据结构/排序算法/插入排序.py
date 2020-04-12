"""
插入排序（英语：Insertion Sort）是一种简单直观的排序算法。
它的工作原理是通过构建有序序列，对于未排序数据，
在已排序序列中从后向前扫描，找到相应位置并插入。
插入排序在实现上，在从后向前扫描过程中，需要反复把已排序元素
逐步向后挪位，为最新元素提供插入空间
"""


def insert_sort(li):
    """插入排序"""
    n = len(li)

    # 选择尚未排好的序列作为插入点,每次插入一个元素
    for i in range(1, n):
        j = i
        while j>0:
            if li[j] < li[j-1]:
                li[j], li[j-1] = li[j-1], li[j]  # 自右向左依次比较插入
                j -= 1  # 插入有序中进行再一次排序
            else:
                break

    return li


def insert_sort_industy(li):
    n = len(li)
    for i in range(2, n):
        key = li[i]
        j = i-1  # 用来构造已经排序好的索引
        while j > 0 and key < li[j]:
            li[j+1] = li[j]
            j -= 1
        # 索引位０
        li[j + 1] = key

    return li


if __name__ == "__main__":
    li = [1, 5, 2, 6, 3, 7, 9, 55, 4, 1, 0]
    print("insert_sort:", insert_sort(li))
    print("insert_sort:", insert_sort_industy(li))