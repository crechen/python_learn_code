import pygame
import sys
from pygame.sprite import Group
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, screen):
        super(Star, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("star.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def blitme(self):
        self.screen.blit(self.image, self.rect)

def create_a_row_star(screen, stars):
    star = Star(screen)
    available_space_x = 800 - 2 * star.rect.width
    number_stars_x = int(available_space_x / (2 * star.rect.width))
    for star_number in range(number_stars_x):
        star = Star(screen)
        star.rect.x = star.rect.width + 2 * star.rect.width * star_number
        stars.add(star)

def run_game():
    screen = pygame.display.set_mode((800,800))
    bg_color = (255,255,255)
    stars = Group()
    create_a_row_star(screen, stars)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        stars.draw(screen)
        pygame.display.flip()

run_game()
