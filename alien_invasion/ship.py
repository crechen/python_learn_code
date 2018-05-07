import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """飞船绘制在屏幕上"""
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.bmp') #加载飞船图像
        self.rect = self.image.get_rect() # 飞船矩形属性
        self.screen_rect = self.screen.get_rect() # 屏幕矩形属性

        #飞船的移动标志
        self.moving_right = False
        self.moving_left = False
        # 初始化飞船位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx) # 存储浮点数的矩形属性

    def blitme(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """通过移动标志控制飞船移动"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center # 更新飞船位置
