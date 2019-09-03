# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 11:18:05 2018

@author: Gavin
"""

""" 2018.01.03  morning  snow  delight """

import json

""" patr1: Exception  cauth"""
def calculate_num(F_name):
    """ 计算文本数目"""
    try:
        with open(F_name) as py:  #打开目标文件 
            txt = py.read()
    except:
        pass # 文件位置不存在  什么都不做
       # print("Location isn't exit!")
    else:
       
        sli = txt.split() #以空格为分隔符将字符串拆分成许多部分
        print("The length is",len(sli))
   
"""part2: jaso operate"""
#存储
def Story_data(data):
    with open("Data.json","w") as js:# 要加文件格式  
        print("Data:",data)
        json.dump(data,js)  #存储数据 
#下载
def Load_data():
    with open("Data.json") as Ljs:
        data = json.load(Ljs)
        print("数据：",data)

#主函数
Files = ["the know.txt","报告.txt","none.txt"]
for file in Files:
    calculate_num(file)
    
Data = {"张万玉":"男", "李春琳":"女"}
Story_data(Data)
 
Load_data()