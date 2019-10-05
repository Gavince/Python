# version2.0(多错误捕获的写法)
try:
    num = int(input("Please enter a num:"))

    result = 8/num
    raise SyntaxError("dads")
    print("Result:",result)
except ZeroDivisionError:
    print("除零错误！")
except ValueError:
    print("值错误")