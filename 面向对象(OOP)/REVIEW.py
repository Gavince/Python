class Bike:
    """

    """
    def __init__(self):

        print("You are buy a bike!")

    def cost(self, money):

        if money<100:
            print("It's very cheap!")

        elif (money >= 100) and (money < 500):
            print("Good")

        else:
            print("Expensive!")


class Car:
    """

    """
    def __init__(self, name, age, car_type):

        self.name = name
        self.age = age
        self.car_type = car_type

    def __str__(self):

        return ("Name:%s\nAge:%d\nCar_type:%s" % (self.name, self.age, self.car_type))

    def perferance(self):
        """
        描述机车性能
        :return:
        """
        print("High perferance!")

    # def time(self, used_time, free_time):
    #
    #      self.userd_time = used_time
    #      self.free_time = free_time


single_bike = bike()
single_bike.cost(5555)
car = Car("dazhong", 15, "old car")
print(car)
car.perferance()
# car.time()