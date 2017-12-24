# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:37:13 2017

@author: Gavin
"""

#2017 .12 .22 
class Gen():# 一个标准类
    #构造
    def __init__(self,name,age,preference): # init 前后必须是两个下划线
        self.name = name
        self.age = age
        self.preference = preference
        self.high = 0
        
    def show(self):#显示数据
        print("Name:"+str(self.name)+"\nAge"+str(self.age)
        +"\nPreference:"+str(self.preference))
        print(" ")
    def inse_info(self,name,age,preference,high):
        self.human = {}#字典
        self.human[name] = name
        self.human[age]  = age
        self.human[preference] = preference
        self.human[high] = high
        return self.human
    
stu = Gen("张万玉","20","Good")#创建实例
com = []
stu.show()
Flag = 1
while(Flag):
#print("Name：")
    name = input("Name:")
    age = input("Age")
    preference = input("Preference:")
    high = input("High:")
    com.append(stu.inse_info(name,age,preference,high))
    Flag = input ("Do you want enter information again!:")
    Flag = int(Flag)
print("Coming.........\n",com)











