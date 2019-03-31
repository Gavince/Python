def input_password():

    pwd = input("Please enter a password:")

    if len(pwd) >= 8:
        return pwd

    print("主动抛出异常")

    # 1>创建异常对象
    ex = Exception("密码长度不够")
    # 2>主动抛出异常
    raise ex


try:
    print(input_password())
except Exception as result:  #接受异常 并且输出异常
    print(result)