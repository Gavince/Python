class Gun:
    """
    枪类
    """
    def __init__(self, modle):
        """

        :param modle:枪的种类
        """
        self.modle = modle
        self.bullet = 0

    def add_bullet(self, count):
        """
        添加子弹
        :param count:添加子弹数量
        :return:
        """
        self.bullet += count

    def shoot(self):
        """
        射击
        :return:
        """
        if self.bullet <=0:
            print("子弹已经用完，请快速装弹！")
            return
        self.bullet -= 1
        print("子弹还有%d"%(self.bullet))


class soilder:
    """
    士兵类
    """
    def __init__(self, name):
        """

        :param name:
        """
        self.name = name
        self.gun = None  #添加另一个类的实例作为属性

    def fire(self):
        """

        :return:
        """
        if self.gun is None:
            print("我的士兵没有枪！")
        else:
            print("冲冲冲......!")
            #self.gun.add_bullet(100)
            self.gun.shoot()


gun = Gun("Ak47")
gun.add_bullet(140)
xm = soilder("xiaomei")
xm.gun = gun
for i in range(1,160):
    xm.fire()








