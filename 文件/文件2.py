#读取每一行的数据

file = open("/home/gavin/Desktop/demo.txt")

while True:

    text = file.readline()

    if not text:#判断是否已经到文件的末尾
        break

    print(text, end="")

file.close()