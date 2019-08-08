class HouseItem:
    """
    定义一个家具类
    """
    def __init__(self, name, area):
        """
        :param name:家具名称
        :param area: 家具面积
        """
        self.name = name
        self.area = area

    def __str__(self):
        return "%s的使用面积是%.2f" % (self.name, self.area)


class House:
    """
    定义一个房子类
    """
    def __init__(self, house_type, area):
        """
        :param house_type:户型
        :param area: 面积
        """

        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.list_item = [] #用来存放房子里面的家具

    def __str__(self):
        return "户型：%s, 面积：%.2f, 剩余面积：%.2f, 家具：%s" %(
            self.house_type, self.area, self.free_area, self.list_item
        )

    def add_item(self, item):
        """
        添加家具
        :param item:
        :return:
        """
        if item.area > self.area:
            return
        self.free_area -= item.area
        self.list_item.append(item.name)


sofa = HouseItem("沙发", 100)
table = HouseItem("桌子", 50)
myhouse = House("三室一厅", 2000)
print(myhouse)
myhouse.add_item(sofa)
myhouse.add_item(sofa)
myhouse.add_item(table)
print(sofa)
print(myhouse)

