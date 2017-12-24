# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 13:48:52 2017

@author: Gavin
"""

#银行家 算法
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
def Start_Bank(Data):
    Requ = Data["Requ"]
    Data1 = {}
    p = Data["p"]
    n = Data["n"] 
    print("Start you reqire\n")
    for i in range(n):
        Requ[0][i] = int(input("Please enter reqire"))
    print("Require  finish !\n")
    
    po = input("please choice a process for you:")
    po = int(po)
    Need = Data["Need"]
    All = Data["All"]
    Work = Data["Work"]
    Ava = Data["Ava"]
    Fa = Data["False"]
# 预分配
    if np.all(Need[po,:] >= Requ[0,:]) and np.all(Requ[0,:] <= Ava[0,:]):
        Need[po,:] -= Requ[0,:]  #加减号紧挨着等于号  唉.......
        All[po,:] += Requ[0,:]
        
        Ava[0,:] -= Requ[0,:]
        Work[0,:] = Ava[0,:]
        Data1 = {"Need":Need,"All":All,
                "Work":Work,"False":Fa,
                "p":p
                }
        return Data1
    else :
        return False
    
#试分配
def Distrbution(Data1):
    Se_qu = []
    Flag = 0  #计算FALSE的个数
    cnt = 0  #标志
    Need = Data1["Need"]
    Work = Data1["Work"]
    All = Data1["All"]
    Fa = Data1["False"]
    p = Data1["p"]
    while(1):
        for i in range(p):
            if( Fa[i] =='F') and ( np.all( Need[i,:] <= Work[0,:])):
                Work[0,:] += All[i,:]
                Fa[i] = 'T'
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
        if (cnt == 15) and (Flag != p):#逻辑理不顺 就加括号
            print("No the sequence of security!\n")
            break
        if Flag==p:
            print("Find a the sequence  of security\n")
            print("Show=")
            
            k =len(Se_qu)
           # print("K===="+str(k))
            for i in range(k):
                print("  "+str(Se_qu[i]))
            break
#主函数
p = int(input("Please enter the number of processor!\n"))
n = int(input("Please enter the resource of computer\n"))
Data = Init_pro(p,n)       
Data1 = Start_Bank(Data)
if Data1 == False:
    print("Memory isn't full")
else:
    Distrbution(Data1)
    
#Data2 = Start_Bank(Data)
#if Data2 == False:
 #   print("Memory isn't full")
#else:
 #   Distrbution(Data2)











