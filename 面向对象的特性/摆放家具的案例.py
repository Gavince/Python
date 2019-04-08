class HouseItem:
    """
    定义一个家具类
    """
    def __init__(self, name, area):
        """

        :param name:
        :param area:
        """
        self.name = name
        self.area = area

    def __str__(self):

        return "[%s] 占地　%0.2f" %(self.name, self.area)


class House:
    """
    描述房子信息
    """
    def __init__(self, house_type, area):
        """

        :param house_type:
        :param area:
        """
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def add_item(self, item):
        """

        :param item:
        :return:
        """
        print("添加的家具为：%s"%item)

        if self.free_area < item.area:
            print("%s面积太大，无法添加！" % item.name)

            return
        self.item_list.append(item.name)
        self.free_area -= item.area

    def __str__(self):
        """

        :return:
        """
        return ("户型：　%s\n 总面积：%.2f[剩余面积%.2f]\n家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))


house = House("三室一厅", 600)

bed = HouseItem("席梦思", 454)
chest = HouseItem("餐桌", 10)

house.add_item(chest)
house.add_item(bed)
print(house)