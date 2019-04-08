class Tool(object):

    count = 0 #一个类属性

    def __init__(self, name):#每次创建对象后都会创建一个初始化对象

        self.name = name
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("起子")

tool3.count = 99 #添加一个count属性,不是一个个类属性(强烈推荐使用这种方法)
print("对象的总数：%d" % tool3.count)
print(tool1.count) #可以使用类名.类属性的名称

print("工具对象的总数%d" % Tool.count)


"""
小结：
实例属性属于各个实例所有,互不干扰；
类属性属于类所有，所有实例共享一个属性；
不要对实例属性和类属性使用相同的名字,否则将产生难以发现的错误
"""