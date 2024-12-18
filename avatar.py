from config import *
import pygame
import weapon
import config


class Avatar(pygame.sprite.Sprite):
    def __init__(self, x_avatar_spawn, y_avatar_spawn, image):
        super().__init__()

        self.x_avatar = x_avatar_spawn
        self.y_avatar = y_avatar_spawn

        self.avatar_image = pygame.image.load(image)
        self.avatar_image = pygame.transform.scale(self.avatar_image, (config.avatar_width, config.avatar_height))
        self.avatar_rect = self.avatar_image.get_rect(topleft=(self.x_avatar, self.y_avatar))


        self.gravity = 1
        self.jumping = False
        self.invincibility_in_use = False
        self.double_jump = False



        self.speed_avatar = config.speed_avatar
        self.health_avatar = config.health_avatar


        self.direction_avatar = True  # true if it is to the right

        self.current_weapon = "sword"

        self.sword = weapon.Sword(999, self.x_avatar, self.y_avatar, self.direction_avatar)    # # need to fill it with var necessary
        self.bow_arrow = weapon.BowArrow("images/icons/chest.png", self.x_avatar, self.y_avatar, self.direction_avatar)  # need to fill it with var necessary





    def generate(self):


        return self.avatar_image, (self.x_avatar, self.y_avatar)





    def lateral_movement(self, list_of_left_wall=list, list_of_right_wall=list):
        key = pygame.key.get_pressed()

        collided_left_wall = False
        for left_wall in list_of_left_wall:
            if Avatar.rect.colliderect(left_wall):
                collided_left_wall = True
                break

        collided_right_wall = False
        for right_wall in list_of_right_wall:
            if Avatar.rect.colliderect(right_wall):
                collided_right_wall = True
                break



        if key[pygame.K_LEFT] and self.x_avatar > 0 and not collided_left_wall:
            self.x_avatar -= self.speed_avatar
            self.direction_avatar = False

        if key[pygame.K_RIGHT] and self.x_avatar < 720 and not collided_right_wall:
            self.x_avatar += self.speed_avatar
            self.direction_avatar = True


    def fall(self, list_of_grounds=list):
        collided_ground = False

        for ground in list_of_grounds:
            if self.avatar_rect.colliderect(ground):
                collided_ground = True
                break

        if not collided_ground:
            self.y_avatar += self.gravity
            self.in_ground = False


        else:
            self.in_ground = True



    def jump(self, double_jump, list_of_roofs=list):
        key = pygame.key.get_pressed()

        collided_roof = False
        for roof in list_of_roofs:
            if self.avatar_rect.colliderect(roof):
                collided_roof = True
                break

        if key[pygame.K_UP] and not self.jumping and self.in_ground:
            self.jumping = True
            self.in_ground = False
            self.rise_timer = fps*2


        elif key[pygame.K_UP] and self.jumping and double_jump:
            self.rise_timer = 0
            Avatar.jump(self, False, list_of_roofs)

        elif self.jumping and self.rise_timer > 0:
            self.y_avatar += self.gravity*2

        if self.rise_timer <= 0 or collided_roof:
            rise = 0



        if self.in_ground:
            collided_roof = False
            jumping = False


        self.rise_timer -= 1


    def get_hurt(self, damage):
        if self.invincibility_in_use:
            self.health_avatar -= damage



    def attack(self):
        key = pygame.key.get_pressed()


        if key[pygame.K_SPACE]:  # attack

            if self.current_weapon == "bow and arrow":
                self.bow_arrow.generate_arrow()
                self.bow_arrow.move_arrow()


            if self.current_weapon == "sword":
                self.sword.attack_area()


        if key[pygame.K_a]:       # switch to bow and arrow
            self.current_weapon = "bow and arrow"

        if key[pygame.K_s]:      # switch to sword
            self.current_weapon = "sword"