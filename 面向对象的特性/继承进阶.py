class Person:
    """
    基类
    """
    def __init__(self, name, age):

        self.name = name
        self.age = age

    def eat(self):

        print("一日三餐！")


class Student(Person):
    """
    学生类
    """
    def __init__(self, name, age, grade):
        #重写父类的方法　并且出事呼哈
        super(Student, self).__init__(name, age) #初始父类　保证子类中有基类的属性
        self.grade = grade

    def eat(self):

        print("大口大口")
        super().eat() #重写方法　并且继承父类的方法


gavin = Student("gavin", 25, 99)
print(gavin.grade)
print(gavin.age)
print(gavin.name)
gavin.eat()


"""
总结：
1.一定要用 super(Student, self).__init__(name, gender) 
去初始化父类,否则,继承自 Person 的 Student 将没有 name 和 gender.

2.函数super(Student, self)将返回当前类继承的父类,
即 Person,然后调用__init__()方法,注意self参数已在super()中传入,
在__init__()中将隐式传递,不需要写出（也不能写）.
"""
