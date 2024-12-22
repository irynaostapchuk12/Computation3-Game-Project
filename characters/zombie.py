
"""
from config import *
import pygame
from weapon import *


class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, 60, 80, ZOMBIE_COLOR)

        self.image = pygame.Surface(width, height)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 1

    def update(self, left_side_platform=0, right_side_platform=720):
        self.rect.y += self.speed
        if self.rect.left < left_side_platform or self.rect.right > right_side_platform:
            self.speed *= -1
"""