def fun(num, *args):
    """test *args"""

    print("num",num)
    for number in args:
        print("number:",number)


def fun1(**kwargs):
    """"""
    print(kwargs)
    for key, value in kwargs.items():
        print("Key:",key)
        print("Value:",value)


#定义一个元组
args = (4, 5, "asda", 454)
print("test1")
fun(45,*args)

print("test2")
fun(1,"nihao", 45, 454, "asda")
dict = {"name":"beibei", "age":16, "favorite":"apple"}
fun1(**dict)
fun1(name="xiaomei", age = 16, )

"""
*args:表示不知道要传递几个参数(元组)
**kwarges:表示要传递一个字典
"""

