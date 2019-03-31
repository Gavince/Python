class Game(object):

    top_score = 0

    def __init__(self, player):

        self.name = player

    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门！")

    @classmethod
    def show_top_score(cls):

        print("历史记录 %d" % cls.top_score)

    def start_game(self):

        print("%s开始游戏了" % self.name)


Game.show_help() #静态方法
Game.show_top_score() #动态方法

#实例一个对象

game = Game("zhang")
game.start_game() #实例方法

"""
小结：
(1):实例方法内部需要访问实例属性
(2):类方法--方法内部只需要访问类属性
(3):静态方法--方法内部,不需要访问实例属性和类属性
"""
