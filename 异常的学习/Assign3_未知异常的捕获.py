# version3.0(未知异常的捕获)
try:
    num = int(input("Please enter a num:"))

    result = 8/num

    print("Result:",result)
except Exception as result:
    print("未知错误%s" % result)