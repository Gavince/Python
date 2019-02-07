class Cat: #语法格式

    def drink(self):
        """
        self:那个对象调用方法,self就是哪一个对象的引用
        """
        print("%s want to drink!" % self.name)

    def eat(self):
        print("I want to eat!")

#创建类
tom = Cat()
#lazy_cat = Cat()
tom.name = "kk" #可以直接在外部添加所要求的属性,属于tom对象（谁是谁的属性）noti
tom.eat()
tom.drink()