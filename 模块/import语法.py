"""

基本语法：
1.from A import B   从某一个模块中导入部分函数来使用
2.import A as a
3.import A, B
4.from A模块 import *  (知道,函数重名不好处理)
注意：
    1.如果同时调用两个模块,出现了调用相同的函数,后一个函数会覆盖前一个函数
    2.导入时先在当前目录进行导入,随后在其他目录导入
    3.(全局变量, 函数, 类)直接执行的代码不是向外界提供的工具
    4.再导入文件时，文件中所有没有任何缩进的代码都会执行一遍  举例如下：
"""
import file1 #
import gavin
gavin.send_message.send("Hello")#必须在__init__ 中引入指定的函数

print("*"*50)






