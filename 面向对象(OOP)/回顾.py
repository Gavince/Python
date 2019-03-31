class Gun:
    """
    枪
    """
    def __init__(self, model):

        self.model = model
        self.bullet_count = 0

    def add_bollet(self, count):

        self.bullet_count += count

    def shoot(self):

        if self.bullet_count <= 0:

            print("BULLET OVER!")
            return
        self.bullet_count -= 1
        print("[%s]突突突[%d]" % (self.model, self.bullet_count))

class Soilder:
    """

    """
    def __init__(self, name):

        self.name = name
        self.gun = None

    def fire(self):

        if self.gun is None:

            print("NO GUN!")
            return

        print("冲冲冲......！")

        self.gun.shoot()

gun = Gun("Ak47")
gun.add_bollet(5000)
xm = Soilder("wangduoyu")
xm.gun = gun
xm.fire()
xm.fire()
xm.fire()
xm.fire()
xm.fire()
xm.fire()
