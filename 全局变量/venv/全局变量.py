# 全局变量
gl_num = 10  # 表示再次出现变量名时　具有相同id值　表明是同一地址


def fun1():
    """
    """
    global core  #申明一个全局变量

    num = 4545 #局部
    core = 12
    print(num)
    print("Id1 is %d" % id(num))


def fun2():
    """
    """
    print("Core(fun2) = %d"%core)
    #num = 45
    print(gl_num)
    print("Id2 is %d" %id(gl_num))


fun1()
fun2()
print(gl_num)
print("Id3 is %d" % id(gl_num))
print("Core(Out) is %d"%core)


"""
注意：
    1. 函数的全局变量不能在局部（函数内部）被修改　即使被修改也是定义局部变量的使用
    2. 局部变量的使用只限与函数内部
    3. 执行顺序先从函数的内部执行局部变量　然后查找相同的全局变量 
    4. 全局变量的引用要定义在函数的最前面 否则会出现未定义的情况
"""