class Earth(object):
    """
    单例模式
    """
    _instance = None#类属性来判断
    flag = False

    def __new__(cls, *args, **kwargs):

        if cls._instance is None:#如果是第一次创建实例对象，需要重新改写父类的方法

            #1.在内存中为对象分配空间
            cls._instance = object.__new__(cls)#需要自己手动闯入一个cls参数
            #2.返回对象的引用
            return cls._instance

        else:

            return cls._instance#若不是第一次创建对象直接返回一个

    def __init__(self):

        if not Earth.flag:#通过设置flag标记来实现之初始化一次

            print("Initalizing.......!")
            Earth.flag = True

a = Earth()
print(id(a))
b = Earth()
print(id(b))
