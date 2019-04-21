"""20190413 下午 阴天"""

num = [1, 2, 3, 4, 5, 6]

target = 7

for i in num:
    for j in num:
        if (i+j) == target:
            print("i=%d, j=%d" % (i, j))