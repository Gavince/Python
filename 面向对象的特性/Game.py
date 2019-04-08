class Game(object):
    """
    定义了一个游戏类
    """
    top_score = 0

    @classmethod
    def show_score(cls):
        """
        显示最高分数
        :return:
        """
        print("最高的分数为%d",cls.top_score)

    @staticmethod
    def show_help():
        """
        显示帮助信息
        :return:
        """
        print("帮助信息！")

    def __init__(self, player_name):

        self.player_name = player_name

    def start_game(self, score):
        """
        开始游戏
        :return:
        """
        print("[%d]正在开始游戏",self.player_name)
        Game.top_score = score


#创建对象

kk = Game("kk")
kk.start_game(155)
Game.show_score()
Game.show_help()
