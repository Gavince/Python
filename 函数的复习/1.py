"""2019.3.31 大晴天　微风"""


def fun1(name, age, perference):
    """
    describe:基本函数的书写
    :param name:描述信息
    :param age: 年龄
    :param perference:长相
    :return: 返回值
    """
    print("姓名：%s, 年龄：%d, 长相：%s" % (name, age, perference))


def fun2(age, kind="little", cost=122): #此处必须先列出没有缺省参数的值，然后子有具体参数的值
    """
    describe:描述缺省参数
    :param age:年代
    :param kind: 种类
    :param cost: 花费
    :return: 返回值
    """
    age += 100
    print("Kind:%s, Cost:%d"%(kind, cost))
    print("Age:%d"%(age))


def fun3():
    """
    describe: 返回值
    :return:
    """
    message = input("Please enter a txt：")

    return message


def fun4(frist_name, last_name, middle_name=""):
    """

    :param frist_name:
    :param last_name:
    :param middle_name:
    :return:
    """
    if middle_name:
        print(frist_name + " " + middle_name + " " + last_name)
    else:
        print(frist_name + " " + last_name)


print("*************************")
fun1("gavin", 19, "handsome")
fun1(name="kk", perference="beautiful", age=18) #关键字实参的不需要注意参数顺序
print("*************************")
fun2(15, "lower", 78778)# 缺省参数的运行
fun2(16)
print("*************************")
message = fun3()
print("Message:%s"%(message))
print("*************************")
fun4("张", "万", "玉")
fun4("张", "玉")
