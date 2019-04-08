def si_hi(names):
    """

    :param names:名字
    :return: 空
    """
    for name in names:
        print("Hello " + name.title())
    temp = input("Please enter other name:")
    names.append(temp)

    return names


names = ["gavin", "tom", "ben", "nancy"]
names_copy1 = si_hi(names) #此处相当于一个赋值语句,实参和形参指向了同一块内存地址
names_copy2 = si_hi(names[:]) #此处是另外指向了一块内存区域,函数内部对列表的操作并不影响实参的值
print("*****************************")
print("Names_copy1:%s" %(names_copy1))
print("*****************************")
print("Names_copy2:%s" %(names_copy2))
print("*****************************")
print("Names:%s" %(names))
