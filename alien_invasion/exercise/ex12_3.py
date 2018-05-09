import pygame
import sys

class Rocket():
    def __init__(self, screen):
        self.screen = screen

        self.speed = 2 # 移动速度
        self.image = pygame.image.load("rocket.png") # 加载rocket图片
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # rocket 位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # 移动标志
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志更新rocket位置"""
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)

def check_events(rocket):
    '''响应鼠标键盘事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = True
            elif event.key == pygame.K_LEFT:
                rocket.moving_left = True
            elif event.key == pygame.K_UP:
                rocket.moving_up = True
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = False
            elif event.key == pygame.K_LEFT:
                rocket.moving_left = False
            elif event.key == pygame.K_UP:
                rocket.moving_up = False
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = False

pygame.init()
screen = pygame.display.set_mode((800, 800)) # 创建屏幕
rocket = Rocket(screen)
bg_color = (255, 255, 255) # 背景颜色
# 主循环
while True:
    screen.fill(bg_color)
    rocket.blitme()
    check_events(rocket)
    rocket.update()
    pygame.display.flip()
