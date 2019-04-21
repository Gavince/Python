#1.open file
file1 = open("README(复制)")
file2 = open("复制", "w")

#2.file copy
text = file1.read()
file2.write(text)

#3.close file
file1.close()
file2.close()