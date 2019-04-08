def demo1():

    return int(input("Please enter a num"))


def demo2():
    return demo1()


try:
    demo2()
except ZeroDivisionError:
    print("除零错误")
except Exception as result:
    print("未知错误%s" % result)