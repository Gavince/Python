# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 16:17:43 2017

@author: Gavin
"""

"""from untitled0 import Swap as us
A=["Hello","pia"]
B=[]
us(A,B)"""
def Buile(frist,second,**persion): # **name 表示一个字典 可以输入多个实参 保存在一个字典中
    name=frist+second
    persion["Boss"]=name
    return persion
def show_build(persion,*age): # *name 表示一个列表  可以输入多个实参 保存在一个列表中
    print(persion)
    for per,info in persion.items():
        print(per," ",info)
        #print(age)
persion=Buile("张","万玉",high="178",weight="140")   #此处字典的输入为 切记 “=”
show_build(persion,121,15,166,45,"tall")     

