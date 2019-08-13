try:
    num = int(input("Please enter a num:"))

    Result = 8 / num

    print("Result:", Result)
except ZeroDivisionError:
    print("除零错误！")
except ValueError:
    print("值错误！")
except Exception as result:
    print("未知异常：%s" % result)
else:
    print("未出现异常！")
finally:
    print("结束异常捕获的执行！")