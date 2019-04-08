class A:

    def __init__(self):

        self.num1 = 100
        self.__num2 = 10#私有属性

    def __test(self):#私有方法

        print("私有方法%d %d" % (self.num1,  self.__num2))

    def test(self): #本类中的方法可以调用本类中的私有属性和私有方法

        print("公有方法！")
        print("调用自己的私有属性%d"%(self.__num2))
        self.__test()


class B(A):

    #　1.访问私有属性

    """
    子类不可能继承父类的私有属性和私有方法
    """

    def demo1(self):

        print("访问父类的私有属性%d"%(self.__num2))

    def demo2(self):

        self.test()
#创建一个子类的对象
b = B()
#在外界不能访问私有属性和私有方法
b.demo2()
print(b)
