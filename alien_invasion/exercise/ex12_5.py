import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group
class Rocket():
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load("rocket.png")
        self.image = pygame.transform.rotozoom(self.image, -90.0, 0.5)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

        # 移动标志
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ 移动 rocket"""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= 2
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 2

class Bullet(Sprite):
    """管理子弹的类"""
    def __init__(self, screen, rocket):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.right = rocket.rect.right
        self.rect.centery = rocket.rect.centery

        self.bullet_color = (0, 0, 0)
        self.bullet_speed_factor = 2

    def update(self):
        self.rect.x += self.bullet_speed_factor
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)

def check_events(screen, rocket, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rocket.moving_up = True # 更改移动标志
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = True
            elif event.key == pygame.K_SPACE:
                #创建子弹
                new_bullet = Bullet(screen, rocket)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                rocket.moving_up = False # 更改移动标志
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = False

def run_game():

    bg_color = (255, 255, 255)

    screen = pygame.display.set_mode((800, 800))
    rocket = Rocket(screen)
    bullets = Group()
    while True:
        check_events(screen, rocket, bullets)
        screen.fill(bg_color)
        rocket.blitme()
        rocket.update()
        for bullet in bullets:
            bullet.draw_bullet()
            bullet.update()
            if bullet.rect.right > 800:
                bullets.remove(bullet)
        print(len(bullets))
        pygame.display.flip()

run_game()
