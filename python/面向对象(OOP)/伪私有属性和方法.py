class Person:

    def __init__(self, name, age, gender):
        # 加上两个下划线　表示一个私有属性
        # 不能被外部调用　只能在内部调用
        self.__name = name
        self.__age = age
        self.gender = gender

    def __get_heigh(self):  # 加上两个下划线　表示一个私有方法
        print("178")

    def get_info(self):
        print("name:{}, age:{}, gender:{}".format(self.__name, self.__age, self.gender))

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if 0 <= age <= 120:
            self.__age = age
        else:
            raise ValueError("年龄范围错误！")


class Woman(Person):

    def __init__(self):
        super().__init__("zhang", 25, "female")


if __name__ == "__main__":
    person = Person("zhang", 25, "male")
    xm = Woman()
    print(xm.set_age(10))
    print(xm.get_age())
    print(xm.get_info())
    # print(person.get_name())
    # print(person._Person__name)
    # print(person.name)
    # print(person.get_height())
"""
总结：
私有属性和方法是不希望被外部访问的的内容，并且其子类也不能实现访问,只能实现的访问公有属性和方法
单个下划线＋类名＋私有属性和方法,可以直接访问私有(也即在python不存在正真的私有)
"""
