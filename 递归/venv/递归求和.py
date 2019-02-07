def sum_numbers(num):
    """

    :param num:
    """
    if num == 1:
        return 1

    #计算原则１＋２＋３.......num

    temp = sum_numbers(num-1)

    #两个数字加和
    return temp + num


result = sum_numbers(100)
print ("Sum is :%d"%result)