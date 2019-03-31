#读写文件
file1 = open("/home/gavin/File/aa", "a")

file1.write("nihhhihihih")

print(file1)

file1.close()

#读写readline只读取一行数据
file2 = open("README.txt")
i = 0
while True:
    text = file2.readline()

    if not text:

        break
    print("Row %d:%s" %(i,text))
    i +=1

file2.close()