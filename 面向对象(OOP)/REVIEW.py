# class Bike:
#     """
#
#     """
#     def __init__(self):
#
#         print("You are buy a bike!")
#
#     def cost(self, money):
#
#         if money<100:
#             print("It's very cheap!")
#
#         elif (money >= 100) and (money < 500):
#             print("Good")
#
#         else:
#             print("Expensive!")
#
#
# class Car:
#     """
#
#     """
#     def __init__(self, name, age, car_type):
#
#         self.name = name
#         self.age = age
#         self.car_type = car_type
#
#     def __str__(self):
#
#         return ("Name:%s\nAge:%d\nCar_type:%s" % (self.name, self.age, self.car_type))
#
#     def perferance(self):
#         """
#         描述机车性能
#         :return:
#         """
#         print("High perferance!")
#
#     # def time(self, used_time, free_time):
#     #
#     #      self.userd_time = used_time
#     #      self.free_time = free_time
#
#
# single_bike = bike()
# single_bike.cost(5555)
# car = Car("dazhong", 15, "old car")
# print(car)
# car.perferance()
# # car.time()
class Gun:

    def __init__(self, mode):

        self.mode = mode
        self.bullet_count = 0

    def add_bullet(self, count):

        self.bullet_count += count

    def __buy(self):

        print("私有方法！")


class Solider:

    def __init__(self, name):

        self.name = name
        self.__position = "No find!"
        self.gun = None

    def fire(self):

        if self.gun is None:

            print("没得手枪,怎么打！")

            return
        self.gun.bullet_count -= 1
        print("Fire fire ........!(Bullet have %d)" % self.gun.bullet_count)


gun1 = Gun("Ak47")
gun1.add_bullet(400)

xm = Solider("老A")
kk = Solider("kk")
kk.gun = gun1

print(kk._Solider__position)#伪静态
xm.gun = gun1

#老kk开枪50
for j in range (0, 50):
    kk.fire()

print("*"*50)
#xm开枪100
for i in range (0, 100):
    #开枪
    xm.fire()



