import pygame


class HealthElixir(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.regeneration  = 1


    def use(self, avatar):
        avatar.health += self.regeneration
        self.kill()
