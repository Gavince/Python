class Car:
    """
    描述车的一些基本特性
    """
    count = 0#定义一个类属性,来记录现在已经创建了多少台车

    def __init__(self, brand, perference, mode):
        """

        :param brand:品牌
        :param perference:性能
        :param mode: 生产地
        """
        self.brand = brand
        self.perference = perference
        self.mode = mode
        self.__designer = "Tom"
        Car.count += 1 #类属性的写法格式，能够被多个实例化的对象所共享

    def describe(self):
        """
        描述车的信息
        :return:
        """
        print("%s的性能：%s,生产地：%s"%(self.brand, self.perference, self.mode))


class Truck(Car):
    """
    大卡车类
    """
    def __init__(self, brand, perference, mode, load):
        """

        :param brand:
        :param perference:
        :param mode:
        :param load:
        """
        super().__init__(brand, perference, mode)
        self.load = load

    def cost(self):
        """

        :return:
        """
        print("大卡车真的好")

    def describe(self):
        """
        重写父类的方法,子类的实例化对象会调用其方法,忽略父类的方法
        :return:
        """
        print("%s的性能：%s，生产地:%s,载重量:%s"%(self.brand, self.perference, self.mode, self.load))


car1 = Truck("大众", "良好", "中国", "10kg")
car1.describe()
car2 = Truck("奥迪", "优秀", "美国", "100kg")
car2.describe()
#car2.__designer  私有属性
print(car2.__module__)
print("总共有多少台车：%d"%(Car.count))