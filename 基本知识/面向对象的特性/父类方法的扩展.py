# 实现了代码的重用　简化代码的复杂性
#子类可以继承父类中所有的方法
class Anaminal:

    def eat(self):
        pass

    def run(self):
        pass


class Dog(Anaminal): #继承了父类的方法 格式：class 类名（父类名）:

    def park(self):

        print("汪汪叫！")


class ChineseDog(Dog):

    def speak(self):

        pass

    def park(self): #override method

        #1 子类的需求
        print("Chinese is dog!")

        #2 使用super().　调用父类中封装的方法，既可以使用子类中的方法的使用(标准语法格式)，调用父类的方法
        super().park()

        #2.1
        #Dog.park(self)
        #注意：子类调用子类　会出现递归的故障
        #ChineseDog.park(self)

        #3 写入其他方法
        print("%$$$&*&^*&^*@#$%^&*()#$^&*")

class Fish(Anaminal):

    def swimming(self):

        pass


xiaotianquan = Dog()
xiaotianquan.run()

ChDog = ChineseDog()
ChDog.park()#重写方法后　只会调用子类重写的方法
dir(object)