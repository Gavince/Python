# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:39:33 2017
@author: Gavin

"""
"""2017.12.19 sunny """

def All_thing(name,age,sex=''): #sex形参 Default 为默认数值，可以在传入实参的过程中不予写入
    student={"name":name,"age":age}
    if sex:
        student["sex"]=sex
    return student
student={}
flag=True


while flag:
    name=input("please enter your name!\n")
    age=input("Please enter your age!\n")
    age=int(age) #input() 默认输入为字符
    student=All_thing(name,age)
    cmd=input("Do you will enter informations? yes or no \n ")
    if cmd=="no":
        flag=False
        
        
        
print("\nInformation : ",student)
for key,value in student.items():
#    print("Your name:",key)
    print("your age:",value)
student=All_thing(name,age,"femail")
print("\nInformation : ",student)

#2017.12.20  Sunny and Happy\
def Swap(passion,H):
    while passion:
        Tempory=passion.pop()
        H.append(Tempory)
        print(Tempory)
    
passion=["lone","love","devote","peace"]
H=[]    
Swap(passion[:],H)#passion 表示创建列表副本 及主程序列表中的内容未改变
for j in passion:
    print("passion:",j)
for i in H:
    print("Values:",i)






















    
