#一个对象的属性可以是另外一个类创建的对象
class Gun:

    def __init__(self, model):

        #类型
        self.model = model

        #子弹
        self.bullet_count = 0

    def add_bullet(self, count):

        self.bullet_count += count

    def shoot(self):
        """
        射击
        :return:
        """
        if self.bullet_count <= 0:

            print("[%s]没有子弹了"%self.model)

            return
        self.bullet_count -= 1
        print("[%s] 突突突 ......[%d]" % (self.model, self.bullet_count))


class Solider():

    def __init__(self, name):

        #士兵的名字
        self.name = name
        #枪
        self.gun = None #可以先添加一个属性　后面在外部进行赋值

    def fire(self):

        #判断士兵是否有枪
        if self.gun == None:

            print("[%s]还没有枪..." % self.name)

            return

        print("冲啊！兄弟们.....")

        #Add bullet
        self.gun.add_bullet(100)

        #Fire
        self.gun.shoot()

gun1 = Gun("AK47")
gun1.add_bullet(555)
gun1.shoot()

#创建士兵
sanduo = Solider("许三多")
#给他把枪
sanduo.gun = gun1
sanduo.fire()


