import pygame
import sys

def check_events(ship):
    '''响应鼠标键盘事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship):
    '''更新屏幕'''
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()

def check_keydown_events(event, ship):
    """处理键盘按下事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """处理键盘弹起事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
