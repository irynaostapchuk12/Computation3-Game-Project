
"""

from config import *
import pygame
from weapon import *

class Vampire(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50, VAMPIRE_COLOR)

        self.image = pygame.Surface(width, height)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.last_bullet_time = 0


    def shoot_bat(self, bats_group):
        now = pygame.time.get_ticks()
        if now - self.last_bullet_time > 1000:  # Shoot every second
            self.last_bullet_time = now
            bat = Bat(self.rect.centerx, self.rect.bottom, BAT_COLOR)
            bats_group.add(bat)

"""