import pygame
from config import *
import avatar



class Powerups(pygame.sprite.Sprite):
    def __init__(self, powerups_time):
        super().__init__()
        self.powerups_time = powerups_time

class Invincibility(pygame.sprite.Sprite):

    def __init__(self, invincibility_x_spawn, invincibility_y_spawn):
        super().__init__()

        self.invincibility_x_spawn = invincibility_x_spawn
        self.invincibility_y_spawn = invincibility_y_spawn

        self.invincibility_image = pygame.image.load(f"images/icons/").convert_alpha()
        self.invincibility_image = pygame.transform.scale(self.invincibility_image, game_icons_size)
        self.invincibility_rect = self.invincibility_image.get_rect(topleft=(self.invincibility_x_spawn, self.invincibility_y_spawn))

        self.invincibility_used = False
        self.invincibility_timer = fps * 4

    def invincibility_icon(self): # criar parametro em get_dameage para nulificar

        if not self.invincibility_used:
            screen.blit(self.invincibility_image, (self.invincibility_x_spawn, self.invincibility_y_spawn))


        if avatar.Avatar.rect_avatar.colliderect(self.invincibility_rect): or self.invincibility_in_use:
            self.invincibility_timer = fps*4


            self.invincibility_in_use = True

        if self.invincibility_in_use is True and self.invincibility_timer > 0:
            pass





    def de_spawner_icon(self):
        pass

    def double_jump_icon(self): # usar double_jump parameter
        pass

    def double_coins_icon(self):
        pass