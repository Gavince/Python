#打开文件
file_read = open("README.txt")
file_write = open("README(复制2)","w")

#复制文件

# text = file_read.read()
# file_write.write(text)

#复制大文件
while True:

    text_line = file_read.readline()

    if not text_line:
        break

    file_write.write(text_line)

    #close
file_read.close()
file_write.close()