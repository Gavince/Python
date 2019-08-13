import pygame
from game_sprites import *


#游戏的主程序
class PlaneGame(object):
    """游戏类"""
    def __init__(self):
        """初始化"""
        #1.游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #2.设置时钟
        self.clock = pygame.time.Clock()
        #3.创建精灵和精灵组
        self.__create_sprites()
        #4.设置监听
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)

    def __create_sprites(self):

        # 背景组
        bp1 = BackGround()
        bp2 = BackGround(True)
        self.back_group = pygame.sprite.Group(bp1, bp2)
        # 敌机组
        self.enemy_group = pygame.sprite.Group()
        # 英雄组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        """开始游戏"""
        print("开始游戏！")

        #游戏循环
        while True:
            # 1. 设置刷新帧率
            self.clock.tick(FRAME)

            # 2. 事件监听
            self.__event_handler()

            # 3. 碰撞检测
            self.__check_collide()

            # 4. 更新精灵组
            self.__update_sprites()

            # 5. 更新屏幕显示
            pygame.display.update()

    def __event_handler(self):
        """检测事件"""
        for event in pygame.event.get():

            #检测到退出
            if event.type == pygame.QUIT:
                PlaneGame.__game_over

            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                print("发射子弹！")
                self.hero.fire()

            #检测键盘
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_RIGHT]:
                self.hero.speed = 2
            elif key_pressed[pygame.K_LEFT]:
                self.hero.speed = -2
            else:
                self.hero.speed = 0

    def __check_collide(self):
        #子弹摧毁飞机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True,True)
        #敌机摧毁英雄
        enemys = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        print("Enemy",enemys)
        #判断是否撞击
        if len(enemys):
            self.hero.kill()
            self.__game_over()

    def __update_sprites(self):
        """更新精灵组"""

        for group in [self.back_group, self.enemy_group, self.hero_group]:
            group.update()
            group.draw(self.screen)
        #更新子弹精灵
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("退出游戏")
        pygame.quit()
        exit()


if __name__ == "__main__":
    game = PlaneGame()
    game.start_game()