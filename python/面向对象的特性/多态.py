class HumanBeing (object):

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def work(self):

        print("Hunman!")


class Designer (HumanBeing):

    def __init__(self, name, age, temper):

        super(Designer,self).__init__(name, age)
        self.temper = temper

    def work(self):

        print("Work!")


class Painter (HumanBeing):

    def __init__(self, name, age, work):
        super(Painter, self).__init__(name, age)

        self.work = work

    def work(self):

        print("Paint!")


xm = Designer("xm", 18, open)
xm.work()