from plane_sprites import *
import pygame

#创建敌机
enemy1 = GameSprite("./images/enemy1.png")
enemy2 = GameSprite("./images/enemy2.png")

enemy2.rect.x = 200

enemy_group = pygame.sprite.Group(enemy1, enemy2)
enemy_group.update()
enemy_group.draw(screen)

pygame.display.update()