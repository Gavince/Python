import random
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)#设置常量(使用大写来表示一个常量)
FRAME = 60 #设置帧率
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT =  pygame.USEREVENT+1

class GameSprite(pygame.sprite.Sprite):
        """游戏精灵的基类"""

        def __init__(self, image_name, speed=1):

            #初始化父类
            super().__init__()

            #添加属性
            #加载图片
            self.image = pygame.image.load(image_name)
            #返回图像的尺寸
            self.rect = self.image.get_rect()
            #初始化速度为１
            self.speed = speed

        def update(self, *args):

            self.rect.y += self.speed


class Background(GameSprite):
    """背景类"""

    #重写父类的方法
    def __init__(self, is_alt=False):
        """"""
        #加载背景类图片
        super().__init__("./images/background.png")

        #判断是第几张图片(实现滚动)
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        #1.调用父类的方法
        super().update()

        #2.添加子类烦方法
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机类"""

    def __init__(self):
        #1.父类创建敌机精灵
        super().__init__("./images/enemy1.png")
        #2.初始化敌机的随机速度
        self.speed = random.randint(1,3)
        #3.初始化敌机的初始化位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width- self.rect.width#获取最大的敌机移动速度
        self.rect.x = random.randint(0,max_x)

    def update(self, *args):

        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            #print("敌机飞出屏幕")
            self.kill()

    def __del__(self):

        #print("敌机挂了！！！")
        pass


class Hero (GameSprite):

    def __init__(self):

        super().__init__("./images/me1.png",0)

        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom-120

        #创建子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self, *args):

        self.rect.x +=self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        for i in (0, 1, 2):
            # 创建精灵
            bullet = Bullet()
            # 位置
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx
            # 添加到精灵组
            self.bullets.add(bullet)
            print("fire...")


class Bullet(GameSprite):
    """子弹类"""

    def __init__(self):
        super().__init__("./images/bullet1.png", -2)

    def update(self, *args):

        super().update()

        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        pass


