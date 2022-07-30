import pygame
import random

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)#设置常量(使用大写来表示一个常量)
FRAME = 60 #设置帧率
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT =  pygame.USEREVENT+1


class GameSprite(pygame.sprite.Sprite):
    """ 精灵类"""

    def __init__(self, image_name, speed=1):

       #1.初始化父类
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):

        self.rect.y += self.speed


class BackGround(GameSprite):
    """背景类"""
    def __init__(self, alt_id=False):
        super().__init__("./images/background.png")

        #判断是否移动
        if alt_id is True:
            self.rect.y = -self.rect.height

    def update(self, *args):

        super().update()

        if self.rect.y >=  SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机类"""
    def __init__(self):
        super().__init__("./images/enemy1.png")
        #随机化速度
        self.speed = random.randint(1, 3)
        #初始位置
        self.rect.bottom = 0
        #飞机的边缘速度
        max_margin = SCREEN_RECT.width - self.rect.x
        self.rect.x = random.randint(0, max_margin)

    def update(self, *args):
        #父类的方法
        super().update()
        #判断是否费出底部
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        pass


class Hero(GameSprite):
    """英雄类"""
    def __init__(self):
        super().__init__("./images/me1.png", 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.height - 120
        #创建一个子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self, *args):

        #初始化速度
        self.rect.x += self.speed

        #判断是否已经超出边界
        if self.rect.x<0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("Fire......")

        for i in (0,1,2):
            #窗机精灵组
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹类"""
    def __init__(self):
        super().__init__("./images/bullet1.png", -2)

    def update(self, *args):

        super().update()

        if self.rect.y < 0:
            self.kill()


