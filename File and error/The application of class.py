# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 13:16:01 2017

@author: Gavin
"""


#2017.12.31  sunday 
from untitled0 import Xatu

'" 调用一个类'''


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









