# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 12:05:46 2017

@author: Gavin
"""
import numpy as np
class Bank():
    def __init__(self):
        print(" ")
    def bank(self,pn):
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
    def Start_Bank(self,Data):
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
        self.p = Data0["p"]
        self.n = Data0["n"] 
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
            Need1[po,:] -= Requ1[0,:]  #加减号紧挨着等于号  唉.......
            All1[po,:] += Requ1[0,:]
        
            Ava1[0,:] -= Requ1[0,:]
            Work1[0,:] = Ava1[0,:]
            Data1 = {
                "Need":Need1,"All":All1,
                "Work":Work1,"False":Fa1,
                "p":p}
            return Data1
        else :
            return False
    
#试分配
    def Distrbution(self,Data3):
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
            if (cnt == 15) and (Flag != p1):#逻辑理不顺 就加括号
                print("No the sequence of security!\n")
                break
            if Flag==p1:
                print("Find a the sequence  of security\n")
                print("Show=")
            
            k =len(Se_qu)
           # print("K===="+str(k))
            for i in range(k):
                print("  "+str(Se_qu[i]))
            break
p = int(input("Please enter the number of processor!\n"))
n = int(input("Please enter the resource of computer\n"))
A  = Bank()
B = Bank()
DataA = A.bank
#Data4 ={}
#Data4 = Data      
print("Data1 ",DataA)
DataAA = A.Start_Bank(DataA)
if DataAA == False:
    print("Memory isn't full")
else:
    A.Distrbution(DataAA)

print("Second processoer!\n")
print("Data1 ",DataA)  
DataBB = B.Start_Bank(DataA)

if B.DataBB == False:
    print("Memory isn't full")
else:
    B.Distrbution(DataBB)

