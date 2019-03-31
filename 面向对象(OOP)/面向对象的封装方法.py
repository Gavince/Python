class Person:
    """
    声明一个人物类
    """
    def __init__(self, new_name, new_weight):

        self.name = new_name
        self.weight = new_weight

    def __str__(self):

        pass

    def run(self):
        print("%s is an running man, wight is %d" % (self.name, self.weight))

    def eat(self):
        print("%s is a big eator!" % self.name)
        self.weight += 10

#初始化第一个对象gavin
gavin = Person("gavin", 140.0)
gavin.eat()
gavin.run()
print(gavin.name)
print(gavin.weight)

#初始化第二个对象xiaomei
xiaomei = Person("xiaomei", 120.0)
xiaomei.eat()
xiaomei.run()
print(xiaomei.weight)

"""

总结：
01.创建的两个对象互相不干扰
02.同类创建的对象,不会产生重叠

"""