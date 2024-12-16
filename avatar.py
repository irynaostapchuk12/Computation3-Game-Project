from config import *
import pygame
import weapon
import config


class avatar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.speed_avatar = config.speed_avatar
        self.health_avatar = config.health_avatar

        self.rect_avatar = self.avatar_image.get_rect()
        self.rect_avatar.topleft = (self.x_avatar, self.y_avatar)

        self.direction_avatar = True  # true if it is to the right

        self.current_weapon = "sword"

        self.sword = weapon.Sword(self.x_avatar, self.y_avatar, self.direction_avatar, 999, self.height_avatar, self.width_avatar )    # # need to fill it with var necessary
        self.bow_arrow = weapon.BowArrow(self.x_avatar, self.y_avatar, self.direction_avatar, None)  # need to fill it with var necessary




    def generation(self, x_avatar_spawn, y_avatar_spawn, image):

        self.x_avatar = x_avatar_spawn
        self.y_avatar = y_avatar_spawn

        self.avatar_image = pygame.image.load(f"{image}")
        self.avatar_image = pygame.transform.scale(self.avatar_image, (config.width_avatar, config.height_avatar))






    def lateral_movement(self):


        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT] and self.x_avatar > 0:
            self.x_avatar -= self.speed_avatar
            self.direction_avatar = False

        if key[pygame.K_RIGHT] and self.x_avatar < screen_width:
            self.x_avatar += self.speed_avatar
            self.direction_avatar = True




    def attack(self):
        key = pygame.key.get_pressed()


        if key[pygame.K_SPACE]:  # attack

            if self.current_weapon == "bow and arrow":
                self.bow_arrow.generate()
                self.bow_arrow.movement()


            if self.current_weapon == "sword":
                self.sword.attack_area()





        if key[pygame.K_a]:       # switch to bow and arrow
            self.current_weapon = "bow and arrow"

        if key[pygame.K_s]:      # switch to sword
            self.current_weapon = "sword"