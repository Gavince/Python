""" 2019 02 06 sunny """


def demo(num, num_list):

    """ example """

    num += num #实际是一个赋值语句
    # num_list += num_list #此时＋＝并不等于赋值语句,而是相当与调用列表的extend方法
    # 正式的列表的赋值语句
    num_list = num_list + num_list #不会影响参数的值

    print("Local num is :%d" % num)
    print("Local num_list is :", num_list)


num1 = 4545
num1_list = [45,78,96]

demo(num1, num1_list)
print("Num1 is :",num1, "\nnum _list is :", num1_list)