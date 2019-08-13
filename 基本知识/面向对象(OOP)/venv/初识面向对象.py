#类名使用大驼峰命名法(StudentNum)　中间不许连接在一起

class Cat: #语法格式

    def __init__(self, new_name): #1.定义一个类中的属性,是一个初始化的方法
                                  #2.定义一个初始化的参数　进行对属性变量的修改
        print("Init!")
        #增加属性的格式
        self.name = new_name #默认初始化

    def drink(self):
        print("I want to drink!")

    def eat(self):
        print("I want to eat!")

    def __del__(self):#自动执行
        print("Over!")

    def __str__(self):
        return "我是小猫[%s]" % self.name

#tom是一个全局变量
tom = Cat("Tom") #类的对象化
print(tom)
tom.drink()
tom.eat()
print(tom.name)
del tom #可以删除一个对象
print("-"*52)


"""
___del___ 自动消除对象

"""