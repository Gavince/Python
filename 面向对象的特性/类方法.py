class Tool(object):

    count = 0 #一个类属性

    @classmethod  #类方法需要用(修饰器)标识符标明方法
    def show_tool_count(cls):

        print("工具的对象的数量 %d" % cls.count)

    #如果不访问类属性/实例属性
    @staticmethod
    def method():

        print("静态方法！")

    def __init__(self, name):

        self.name = name
        Tool.count += 1


#调用类方法
Tool.method() #通过类名 调用静态方法 - 不需要创建对象
tool1 = Tool("斧头")
tool1.show_tool_count()

tool1.count += 10 #外部创建了一个实例属性
print(tool1.count)#实例属性
del tool1.count

Tool.count += 10
print(Tool.count)#类属性
print(tool1.count)
Tool.show_tool_count()


"""
小结：
二：方法

　　1：实例方法：

　　　　def fun_name(self,...):

　　　　　　pass

　　　　外部用实例调用

　　2：静态方法：@staticmethod            

　　　　　　不能访问实例属性！！！   参数不能传入self！！！

　　　　　　与类相关但是不依赖类与实例的方法！！

　　3:类方法：@classmethod

　　　　　　不能访问实例属性！！！   参数必须传入cls！！！

　　　　　　必须传入cls参数（即代表了此类对象-----区别------self代表实例对象），并且用此来调用类属性：cls.类属性名

　　*静态方法与类方法都可以通过类或者实例来调用。其两个的特点都是不能够调用实例属性

"""