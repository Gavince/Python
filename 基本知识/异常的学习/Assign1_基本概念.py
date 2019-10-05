# version1.0(一种异常的捕获)
try:
    #可能会出现错误的地方
    num = int(input("please enter number"))
except:
    #修改后的执行方法
    print("please enter a correct a num!")
print("--------------")



