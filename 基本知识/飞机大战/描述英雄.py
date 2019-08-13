import pygame

#x, y, width, heigh
hero_rec = pygame.Rect(100, 500, 120, 125)

print("英雄的原点 %d %d " % (hero_rec.x, hero_rec.y))
print("英雄的尺寸 %d %d " % (hero_rec.width, hero_rec.height))

print("%d %d" % hero_rec.size)