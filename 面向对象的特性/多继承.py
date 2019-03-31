class A:

    def test(self):

        print("Hello xm!")

    def demo(self):

        pass

class B:

    def train(self):

        print("Hello kk!")

    def demo(self):

        pass


class C(A, B): #多继承的方法使用(如果A,B类中有相同的方法,按照继承顺序调用)
               #多继承可以同时具有两个父类的方法
    pass


c = C()
c.test()
print(C.__mro__) #方法的搜索顺序
c.train()
"""
总结：class 类名(object)：

    pass
    
"""