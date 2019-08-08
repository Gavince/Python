#私有属性和方法是不希望被外部访问的的内容
class Woman:
    def __init__(self, name):

        self.name = name
        self.__age = 18 # 加上两个下划线　表示一个私有属性
                        # 不能被外部调用　只能在内部调用

    def __secret(self):# 加上两个下划线　表示一个私有方法

        print("%s的年龄是%d" % (self.name, self.__age))


xm = Woman("xiaomei")
xm.__age
xm._Woman__secret()








