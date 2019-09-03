# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 13:27:47 2018

@author: Gavin
"""

#2012.01.02  13.28 

"""with open("file.txt") as fi:
    lines = fi.readlines() #读出文件内容 并且存人一个列表
    print(lines)
    #character = fi.read()
   # print(character.rstrip())
#part 1
#逐行读取
#       for line in fi:
#        print(line.strip())
#part 2
#表示可在with的作用范围外使用文件调用的内容        
for line in lines:
    print(line.strip())"""

#写模式 清除原有内容重新写入  要注意这一点  切记
"""with open("file.txt","w") as file:
    file.write("I'm zhangwanyu!")"""

#
with open("file.txt","a") as fi:
    for i in range(4):
        example = input("Input:")
        fi.write(example+"\n")