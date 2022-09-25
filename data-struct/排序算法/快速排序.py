"""
快速排序（英语：Quicksort），又称划分交换排序（partition-exchange sort）
，通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一
部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过
程可以递归进行，以此达到整个数据变成有序序列。
"""


def quick_sort(li, first, last):
    """
    :param li:数据
    :param first:首元素的值
    :param last: 末尾元素的值
    :return: 已排序好的值
    """
    # 递归的出口
    if first >= last:
        return

    mid_value = li[first]

    low = first
    high = last

    while low < high:
        while low < high and mid_value <= li[high]:  # high游标左移
            high -= 1
        li[low] = li[high]

        while low < high and li[low] < mid_value:  # low游标右移

            low += 1
        li[high] = li[low]

    # 左右相逢，赋中值
    li[low] = mid_value

    # 递归重复分区求最小
    quick_sort(li, first, low - 1)
    quick_sort(li, low + 1, last)

    return li


def quick_sort2(array, left=0, right=None):
    """算法导论版本"""
    if len(array) < 1:
        return []

    if right is None:
        right = len(array) - 1
    if left < right:
        pivot = partition(array, left, right)
        quick_sort(array, left, pivot - 1)  # 左侧
        quick_sort(array, pivot + 1, right)  # 右侧
    return array


def partition(arr, left, right):
    i = left - 1
    for j in range(left, right):
        if arr[j] <= arr[right]:
            i += 1
            arr[j], arr[i] = arr[i + 1], arr[right]
    arr[right], arr[i + 1] = arr[i + 1], arr[right]

    return i + 1


if __name__ == "__main__":
    array1 = [1, 2, 9, 3, 3, 6, 4, 1]
    print("Quick_sort:", quick_sort(array1, 0, len(array1) - 1))
    array2 = [1, 2, 9, 3, 3, 6, 4, 1]
    print("Quick_sort2:", quick_sort2(array2))
