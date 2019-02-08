class HouseItem:
    """
    家具格式
    """
    def __init__(self, name, area):

        self.name = name
        self.area = area

    def __str__(self): #必须返回一个string

        return "[%s] 占地　%0.2f" % (self.name, self.area)


class House:
    """
    房子
    """
    def __init__(self, house_type, area):

        self.house_type = house_type
        self.area = area
        self.free_area = area #开始时:空闲面积等于总面积
        self.item_list = [] #添加家具

    def add_item(self, item):
        """
        :param item: 家具
        :return:
        """
        print("添加的家具为：%s" % item)  #作为__str__的返回
        #判断家具的面积
        if self.free_area < item.area:

            print("%s 面积太大,无法添加！" % item.name)

            return

        #添加家具
        self.item_list.append(item.name)

        #计算剩余面积
        self.free_area -= item.area

    def __str__(self):

        #【tip】python可以自动连接一个括号里的内容
        return ("户型：　%s\n 总面积：%.2f[剩余面积%.2f]\n家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))


house = House("三室一厅", 600)

bed = HouseItem("席梦思", 454)
chest = HouseItem("餐桌",10)

house.add_item(chest)
house.add_item(bed)
print(house)
