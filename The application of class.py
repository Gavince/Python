# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 13:16:01 2017

@author: Gavin
"""

#2017.12.30 sunday  
#类的继承与重写的应用
class Female():#小类 或者独立类
    def __init__(self):
        self.Lover = "lichunli"
    def show(self):
        print("Lover:",self.Lover) 
        
        
class Student():#父类
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.lover = "none"
    def display(self):
        print("Name:",self.name,"Age:",self.age,"Sex:",self.sex)
    def favorite(self,*love):
        for i in love:
            print("Favorinte:",i)
            

class Xatu(Student):#子类
    def __init__(self,name,age,sex,grade="大一"):#设置默认值 grade 为子类的属性
        super().__init__(name,age,sex)#继承 无self
        self.grade = grade
        self.female = Female()#定义一个小类  注意有一个self
        
    def display(self):#重写父类的方法 不能添加新的元素
        print("Name:",name,"Age:",age,"Sex:",sex)
    def show1(self):#子类的方法
        print("Grade:",self.grade)
        
#主函数        
name = input("Name=")
age = input("Age=")
sex = input("Sex=")

xatu = Xatu(name,age,sex)
xatu.display()

like1 = input("Please enter your favorite:")
like2 = input("Please enter your favorite:")
xatu.favorite(like1,like2)

xatu.show1()

xatu.female.show()









