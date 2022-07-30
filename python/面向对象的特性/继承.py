# 继承的复习
class Animal:
    """

    """
    def eat(self):
        pass

    def drink(self):
        pass

    def run(self):
        pass

    def sleep(self):
        pass


class Dog(Animal):
    """
    """
    def bark(self):
        print("ooooo")


class XiaoTianQuan(Dog):
    """

    """
    def fly(self):
        pass

    def bark(self):
        print("aaaa")

    def call_dad(self):
        super().bark()

dog1 = XiaoTianQuan()
dog1.bark()
dog1.call_dad()