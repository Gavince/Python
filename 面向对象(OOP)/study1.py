class Dog():
    """
    描述狗的信息
    """
    def __init__(self, name, kind, age):
        """

        :param name:姓名
        :param kind:种类
        :param age:年龄
        """
        self.name = name
        self.kind = kind
        self.age = age

    def bark(self):
        """
        吠叫
        :return:
        """
        print("%s正在吠叫"%(self.name))


dog1 = Dog("金毛", "hai", 4)
dog2 = Dog("labuladuo", "mm", 3)
dog1.bark()
dog2.bark()