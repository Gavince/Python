"""
希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，
是直接插入排序算法的一种更高效的改进版本。
希尔排序是非稳定排序算法。该方法因DL．Shell于1959年提出而得名。
希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，
算法便终止。
"""


def sell_sort(li):
    gap = len(li) // 2  # 初始间隔
    while gap > 0:
        for j in range(gap, len(li)):  # 插入排序的次数
            # print(gap)
            i = j  # i 表示插入序列的索引
            while i > 0:  # 插入排序
                if li[i] < li[i - gap]:  # 不同间隔的同一位置进行比较
                    li[i], li[i - gap] = li[i - gap], li[i]
                    i -= gap
                else:
                    break
        gap //= 2  # 间隔不断被缩小，指导不为０

    return li


def sell_sort_optim(array):
    """优化后的希尔算法"""

    n = len(array)
    h = 1
    while h < n / 3:
        h = h * 3 + 1  # 选择起始步长,加１表示最后的为步长为１的插入排序

    while h >= 1:
        for i in range(h, n):  # 插入排序的次数
            j = i
            while h <= j and array[j] < array[j - h]:
                array[j], array[j - h] = array[j - h], array[j]
                j -= h

        h = h // 3  # 确定下一次的步长
    return array


if __name__ == "__main__":
    li1 = [100, 1, 5, 3, 8, 6, 0]
    li2 = [100, 1, 5, 3, 8, 6, 0]
    print("sell_sort:", sell_sort(li1))
    print("sell_sort_optim", sell_sort_optim(li2))
