class Cat: #语法格式

    def drink(self):
        """
        self:那个对象调用的方法　self就是哪一个对象的引用
        """
        print("I want to drink!")

    def eat(self):
        print("I want to eat!")

    def __str__(self):
        return "这是猫类"

#创建类
tom = Cat()
lazy_cat = Cat()
tom.name = "kk" #可以直接在外部添加所要求的属性,属于tom对象（谁是谁的属性）notice

#类的引用
gavin = tom
print("gavin",gavin)
gavin.eat()
gavin.drink()

#调用
print("tom",tom)
tom.eat()
tom.drink()

#调用
print("lazy_cat",lazy_cat)
lazy_cat.drink()
lazy_cat.eat()
"""
总结：
　１．两次对象的内存地址不一样　所以是同一个类的不同对象
　２．tom.name = "kk"　直接添加属性(不推荐使用)

"""




