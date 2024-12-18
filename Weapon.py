
# direction:  left or right, if direction True = right, if direction False = left
# image, list of different images
#size, size of the image


#x
#y
#height
#width
#direction


import pygame
import math
from config import *
import avatar



class Sword:
    def __init__(self, weapon_reach, x, y, direction):

        self.x = x
        self.y = y
        self.direction = direction


        self.weapon_reach = weapon_reach


    def attack_area(self):
        if self.direction: # if direction is the right
            return pygame.Rect(self.x + avatar_width, self.y, self.x + avatar_width + self.weapon_reach,  self.y + avatar_height)

        elif self.direction: # if direction is false then left
            return pygame.Rect(self.x, self.y, - self.weapon_reach, avatar_height)




class Fist:
    def __init__(self, x, y, direction):

        self.x = x
        self.y = y
        self.direction = direction


    def attack_area(self):
        if self.direction: # if direction is the right
            return pygame.Rect(self.x + (avatar_width//2), self.y, avatar_height // 2, avatar_height)

        elif self.direction: # if direction is false then left
            return pygame.Rect(self.x + (avatar_width//2), self.y, - avatar_width//2, avatar_height)


    # tert cuidado que aqui o direction é 1 ou -1

class BowArrow(pygame.sprite.Sprite):

    def __init__(self, image, x_avatar, y_avatar, direction_avatar):
        super().__init__()

        self.x_avatar = x_avatar
        self.y_avatar = y_avatar
        self.direction_avatar = direction_avatar



        self.speed = 7

        self.image = pygame.image.load(f"{image}")
        self.image = pygame.transform.scale(self.image, arrow_size)



        self.left_angle = 0
        self.right_angle = 0




    def generate_arrow(self):



        self.x_arrow_spawn = self.x_avatar + (avatar_width // 2)
        self.y_arrow_spawn = self.y_avatar + (avatar_height // 2)

        self.x_arrow = self.x_arrow_spawn
        self.y_arrow = self.y_arrow_spawn

        self.arrow_rect = self.arrow_image.get_rect(center=(self.x_arrow, self.y_arrow))


        if self.direction_avatar: # for the right
            self.rotated_arrow_image = pygame.transform.rotate(self.arrow_image, self.right_angle)
            self.rotated_arrow_rect = self.rotated_arrow_image.get_rect(center=self.rotated_arrow_image)
            screen.blit(self.rotated_arrow_image, self.rotated_arrow_rect)

        else: # for the left
            self.rotated_arrow_image = pygame.transform.rotate(self.arrow_image, self.left_angle)
            self.rotated_arrow_rect = self.rotated_arrow_image.get_rect(center=self.rotated_arrow_image.center)
            screen.blit(self.rotated_arrow_image, self.rotated_arrow_rect)


    def move_arrow(self):

        self.x_arrow += int(self.speed * math.cos(self.direction_avatar))
        self.y_arrow += int(self.speed * math.sin(self.direction_avatar))



        # in here i need the vars of the screen size
        if (self.rotated_arrow_rect < 0 or
            self.rotated_arrow_rect.x > avatar_width or
            self.rotated_arrow_rect.y < 0 or
            self.rotated_arrow_rect.y > avatar_height):
            
            self.kill()
