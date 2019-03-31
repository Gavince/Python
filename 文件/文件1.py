"""
操作文件三步走原则：

         1.打开文件
         2.读写文件
         3.关闭文件

        open("文件", "访问权限")
"""
file = open("/home/gavin/File/file") #读取文件内容

text = file.read()#文件读取完后 文件指针已经到了文件的末尾
print(text)

print("*"*50)

text = file.read()
print(text)

file.close()

