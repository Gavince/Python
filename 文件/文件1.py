"""
操作文件三步走原则：

         1.打开文件
         2.读写文件
         3.关闭文件

        open("文件", "访问权限")
"""
file = open("/home/gavin/Desktop/demo.txt", "w")

file.write("Hello, World!")
file.write("你好！")

file.close()


