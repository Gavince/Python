import pygame
from plane_sprites import *


#初始化
pygame.init()

#绘制图像
screen = pygame.display.set_mode((480, 700))#相当于构建了一张画布

#1.1绘制背景图片
bg = pygame.image.load("./images/background.png")

#1.2绘制在屏幕上
screen.blit(bg, (0,0))

#2绘制英雄
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 500))
#更新显示(所有绘制结果完成之后在update)
pygame.display.update() #1如果不调用此方法 不会绘制图片
                        # 2可以统一更新
clock = pygame.time.Clock()
i = 0

#4.定义英雄的初始位置
hero_rect = pygame.Rect(150, 500, 102, 126)

#创建敌机精灵
enemy1 = GameSprite("./images/enemy1.png")
enemy2 = GameSprite("./images/enemy1.png",2)
#创建了精灵组
enemy_group = pygame.sprite.Group(enemy1, enemy2)


#游戏循环
while True:

    #每一秒 刷新帧率
    clock.tick(60)#设置频率的1/60

    #捕获时间(并且退出游戏)
    for even in pygame.event.get():#得到一个事件的列表

        if even.type == pygame.QUIT:
            print("退出游戏！")

            pygame.quit()

            exit()

    hero_rect.y -= 1

    if hero_rect.y + hero_rect.height <= 0:
        hero_rect.y = 700
    #每次要刷新背景图片(来消除重影)
    screen.blit(bg, (0, 0))
    #绘制英雄
    screen.blit(hero, hero_rect)


    #跟新精灵组
    enemy_group.update()
    #在ｓｃｒｅｅｎ上绘制敌机
    enemy_group.draw(screen)

    #统一更新显示
    pygame.display.update()

#退出
pygame.quit()