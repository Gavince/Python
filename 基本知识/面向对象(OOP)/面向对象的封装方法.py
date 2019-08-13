class Person:
    """
    创建一个Person类，记录体重的增减
    """

    def __init__(self, name, weight):
        """

        :param name:
        :param weight:
        """
        self.name = name
        self.weight = weight

    def run(self):
        """

        :return:
        """
        self.weight -= 1
        print("你当前的体重"%self.weight)

    def eat(self):
        """

        :return:
        """
        self.weight += 1
        print(self)
        print("你当前的体重%d"%self.weight)

    def __str__(self):

        return "%s当前的体重是%d" %(self.name, self.weight)


tom = Person("tom", 145)
marry = Person("Marry", 100)
for i in range(10):
    tom.eat()
print(tom)
print(marry)


"""
总结：
01.创建的两个对象互相不干扰
02.同类创建的对象,不会产生重叠
"""


