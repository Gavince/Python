# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 13:48:52 2017

@author: Gavin
"""

#银行家 算法
from copy import deepcopy;
import numpy as np
#初始化
def Init_pro(p,n):
    Data = {}
    Fa = []
    Requ = np.zeros((1,n))# 多少行 多少列 不是零  唉......
    Max = np.zeros((p,n))
    All = np.zeros_like(Max)#创建一个Max一样的0矩阵
    Need = np.zeros_like((Max))
    Ava = np.zeros((1,n))
    Work = np.zeros_like(Ava)
    for i in range(p):
        Fa.append("F")
        print("\nProcessor = "+str(i))
        for j in range(n):
            Max[i][j] = int(input("Please enter Max: "))
            All[i][j] = int(input("please enter All: "))
            Need[i][j] = Max[i][j]-All[i][j]
    print("Input have finished!\n")
    for i in range(n):
       # print("N==:",n)
        Ava[0][i] = int(input("Please enter Ava: "))
        Work[0][i] = Ava[0][i]
    Data = { 
            "Max":Max,"All":All,
            "Need":Need,"Ava":Ava,
            "Work":Work,"Requ":Requ,
            "n": n,"p":p,
            "False":Fa
            }
    return Data
# 开始执行
def Start_Bank(Data): #预分配
    #声明为局部变量
    Data0 = {} 
    Requ1 = {}
    Data1 = {}
    Need1 = {}
    Work1 = {}
    Fa1 = {}
    All1 ={} 
    Ava1 = {} 
    po = 0
    Data0 = Data
    p = Data0["p"]
    n = Data0["n"] 
    Requ1 = Data0["Requ"]
    print("Start you reqire\n")
    for i in range(n):
        Requ1[0][i] = int(input("Please enter reqire"))
    print("Require  finish !\n")
    
    po = input("please choice a process for you:")
    po = int(po)
    Need1 = Data0["Need"]
    All1 = Data0["All"]
    Work1 = Data0["Work"]
    Ava1 = Data0["Ava"]
    Fa1 = Data0["False"]
# 预分配
    if np.all(Need1[po,:] >= Requ1[0,:]) and np.all(Requ1[0,:] <= Ava1[0,:]):
  #判断进程需求资源是否满足     
        Need1[po,:] -= Requ1[0,:]  #加减号紧挨着等于号  唉.......
        All1[po,:] += Requ1[0,:]
        
        Ava1[0,:] -= Requ1[0,:]
        Work1[0,:] = Ava1[0,:]
        
        Data1 = {"Need":Need1,"All":All1,
                "Work":Work1,"False":Fa1,
                "p":p
                }
        return Data1
    else :
        return False
    
#试分配
def Distrbution(Data3):#安全性检测
    Data1 = {}
    #声明为局部变量
    Fa2 = []
    Se_qu = []
    Need2 ={}
    Work2 ={}
    All2 ={}
    Flag = 0  #计算FALSE的个数
    cnt = 0  #标志
    Data1 = Data3
    Need2 = Data1["Need"]
    Work2 = Data1["Work"]
    All2 = Data1["All"]
    Fa2 = Data1["False"]
    p1 = Data1["p"]
    while(1):
        for i in range(p1):
            if( Fa2[i] =='F') and ( np.all( Need2[i,:] <= Work2[0,:])):
                Work2[0,:] += All2[i,:]
                Fa2[i] = 'T'
                Flag +=1
               # print("i=="+str(i))
                Se_qu.append(i)
            else:
                continue
        cnt +=1
       #""" for j in range(p):
        #    if(Fa[i] == "T"):
         #       Flag +=1
        #print("Flag="+str(Flag))
      #"""  
        if (cnt == 15) and (Flag != p1):#
            print("No the sequence of security!\n")
            break
        if Flag==p1:
            print("Find a the sequence  of security\n")
            print("Show=")
            
            k =len(Se_qu)
           # print("K===="+str(k))
            for i in range(k):
                print("  "+str(Se_qu[i]))
            global a
            a = 1 
            break
#主函数
p = int(input("Please enter the number of processor!\n"))
n = int(input("Please enter the resource of computer\n"))
DataA = deepcopy (Init_pro(p,n))

DataC = deepcopy(DataA)
DataB = deepcopy(DataA)

#Data4 ={}
#Data4 = Data     
print("找寻一个安全性序列\n") 
print("Data1 ",DataA)
DataAA = Start_Bank(DataA)
if DataAA == False:
    print("Memory isn't full")
else:
    Distrbution(DataAA)

if=
#Mark = 1
#while(Mark):
print("Second processoer!\n")
print("Data1 ",DataB)  
DataBB = Start_Bank(DataB)

if DataBB == False:
    print("Memory isn't full")
else:
    Distrbution(DataBB)
    print("Do you want choice again!\n")
    if a == 1:
        
  #  Mark = int(input("Do you want to try again! = (Yes/1 No/0)"))
print("Data1 ",DataC)  

DataCC = Start_Bank(DataC)

if DataCC == False:
    print("Memory isn't full")
else:
    Distrbution(DataCC)









