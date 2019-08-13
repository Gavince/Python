class Gun:
    """
    枪类
    """
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0#初始化为0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print("没有子弹")
        else:
            self.bullet_count -= 1
            print("Tutututu.......")

    def __str__(self):
        return '剩余子弹%d'%self.bullet_count


class Solider:
        """
        士兵类
        """
        def __init__(self, name):
            self.name = name
            self.gun = None

        def fire(self):
            if self.gun is None:
                print("士兵没有枪！")
                return
            else:
                self.gun.shoot()


AK = Gun("AK47")
AK.add_bullet(500)
xm = Solider("xm")
print("我要打仗了")
xm.gun = AK
for i in range(100):
    xm.fire()
print(AK)

"""
总结：
    （1）is　是用来判断引用地址是否相等(是否为同一个对象的引用)
    （2）==　是用来判断值是否相等
"""
