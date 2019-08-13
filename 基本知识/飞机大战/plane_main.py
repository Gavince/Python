from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化！")

        #1.创建窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #2.设置时钟
        self.clock = pygame.time.Clock()
        #3.调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)

    def __create_sprites(self):
        """创建精灵组"""

        #背景组1.0
        # bg1 = Background("./images/background.png")
        # bg2 = Background("./images/background.png")
        # bg2.rect.y = -bg2.rect.height#实现交替滚动的效果
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        #敌机组
        self.enemy_group = pygame.sprite.Group()
        #英雄组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        """
        开始游戏
        :return:
        """
        print("开始游戏！")

        while True:

            #1.设置时钟频率60HZ
            self.clock.tick(FRAME)

            #2.事件监听
            self.__event_hunder()

            #3.碰撞检测
            self.__check_collide()

            #4.更新精灵组
            self.__update_sprites()

            #5.更新屏幕
            pygame.display.update()

    def __event_hunder(self):
        """监听"""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场！！！")
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                print("发射子弹！")
                self.hero.fire()
           # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT
        #键盘模式
        #检测按键
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif key_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0


    def __check_collide(self):
        #子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        #敌机摧毁英雄
        enemys = pygame.sprite.spritecollide(self.hero, self.enemy_group, True,)
        #判断是否撞击敌机
        if len(enemys):

            #英雄牺牲
            self.hero.kill()
            #游戏结束
            self.__game_over()

    def __update_sprites(self):
        """更新精灵组"""

        for group in [self.back_group, self.enemy_group, self.hero_group]:
            group.update()
            group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        """ 结束游戏"""
        print("游戏结束")

        pygame.quit()
        exit()


if __name__ == '__main__':

    #创建一个实例的对象
    game = PlaneGame()
    #调用开始游戏的实例方法
    game.start_game()