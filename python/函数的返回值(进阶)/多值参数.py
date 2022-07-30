def demo(num, *nums, **person):

    print(num)
    print(nums)
    print(person)


def demo1(*args):
    """

    :param args:
    :return:
    """
    num = 0

    print(args)

    for n in args:
        num += n
    return num

#demo(1)
demo(1,45,454,4,name= "xiaoming",age = 18,sex = "female")

result = demo1(1,12,5545,121,3333,2555)
print("Result is =%d"%result)