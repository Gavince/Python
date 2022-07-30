def say_hello():
    """

    :return:
    """
    print("你好")


#如果直接执行文件会输出__main__
#测试模块时可以实现调用,而其他类调用时不会被执行
print(__name__)
if __name__ == "__main__":

    say_hello()