import pygame
import sys
from ex12_2 import Malio

bg_color = (0, 0, 255) # 蓝色
screen = pygame.display.set_mode((800,800))
malio = Malio(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(bg_color)
    malio.blitme()
    pygame.display.flip()
