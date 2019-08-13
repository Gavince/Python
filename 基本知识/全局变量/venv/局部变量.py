# 局部变量
gl_num = 4545



def demo1():

    """
    形参形成与调用　终于函数的消亡
    局部变量的使用只限制与局部
    """
    num = 10
    print(num)
    print("Id1 is %d\n"%id(num))


def demo2():
    """函数的使用"""
    num = 455
    print(num) #两个局部变量的互不干涉
    print("Id3 is %d\n"%id(num))


# 全局和局部相同变量名的数据地址不同
demo1()
demo2()

print("Id2 is %d"%id(gl_num))
print(gl_num)

