"""
冒泡排序的简介：
冒泡排序（英语：Bubble Sort）是一种简单的排序算法。
它重复地遍历要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
遍历数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。
"""


def bubble_sort(alist):
    """简单的冒泡排序(上升)"""

    n = len(alist)

    # 第一种写法
    # for i in range(n-1):
    #     for j in range(n-1-i):

    # 第二种写法
    for i in range(n - 1, 0, -1):
        count = 0
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                count += 1

        if count == 0:  # 表示此时已经有序, 直接退出外层循环(考虑时间复杂度)
            break

    return alist


def order_bubble(array):
    """奇数在前　偶数在后"""

    n = len(array)
    for i in range(n - 1):
        flag = False  # 查看第k次是否已经排好序
        for j in range(n - 1 - i):
            if array[j] % 2 == 0 and array[j + 1] % 2 == 1:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True  # 尚未排好序列

        if flag is False:
            break

    return array


def double_order_bubble(items):
    """双向排序"""
    n = len(items)

    # 从左向右排序
    for i in range(n - 1):
        flag = False
        for j in range(n - 1 - i):
            if items[j + 1] < items[j]:
                items[j], items[j + 1] = items[j + 1], items[j]
                flag = True
        # 从右向左排序
        if flag:
            flag = False
            for j in range(n - 2 - i, 0, -1):
                if items[j] > items[j - 1]:
                    items[j], items[j - 1] = items[j - 1], items[j]
                    flag = True
        # 退出
        if flag is False:
            break

    return items


def str_bubble_sort(str_items, comp=lambda x, y: x > y):
    """
    非数字实现排序
    :return:
    """
    n = len(str_items)

    # 从左向右排序
    for i in range(n - 1):
        flag = False
        for j in range(n - 1 - i):
            if comp(str_items[j + 1], str_items[j]):
                str_items[j], str_items[j + 1] = str_items[j + 1], str_items[j]
                flag = True

        # 从右向左排序
        if flag:
            flag = False
            for j in range(n - 2 - i, 0, -1):
                if comp(str_items[j], str_items[j - 1]):
                    str_items[j], str_items[j - 1] = str_items[j - 1], str_items[j]
                    flag = True

        # 退出
        if flag is False:
            break

    return str_items


if __name__ == "__main__":
    # 算法一
    alist = [1, 2, 2, 8, 3, 7, 4]
    reverse_alist = bubble_sort(alist)
    print("reverse_alist:", reverse_alist)

    # 算法二
    array = [1, 5, 8, 2, 3, 7, 6]
    print("reverse_array:", order_bubble(array))

    # 算法三
    items = [1, 5, 6, 2, 3, 7, 6, 77]
    print("reverse_item:", double_order_bubble(items))
    # 算法四
    items_arr = ["apple", "orange", "pear", "bikes", "dog", "AI", "beautiful"]
    print(str_bubble_sort(items_arr, lambda s1, s2: len(s1) > len(s2)))


"""
知识点：
lambda语句中，冒号前是参数，可以有多个，用逗号隔开，冒号右边的返回值。
"""