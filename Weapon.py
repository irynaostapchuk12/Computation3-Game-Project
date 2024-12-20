
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

    def __init__(self, image, x_avatar, y_avatar, direction, screen):
        super().__init__()

        self.x_avatar = x_avatar
        self.y_avatar = y_avatar
        self.direction = direction

        self.screen = screen



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

        self.rect = self.image.get_rect(center=(self.x_arrow, self.y_arrow))


        if self.direction: # for the right
            self.image = pygame.transform.rotate(self.image, self.right_angle)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.screen.blit(self.image, self.rect)


        else: # for the left
            self.image = pygame.transform.rotate(self.image, self.left_angle)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.screen.blit(self.image, self.rect)
        print("generate")


    def move_arrow(self):

        self.x_arrow += int(self.speed * math.cos(self.direction))



        # in here i need the vars of the screen size
        if (self.rect.x < 0 or
            self.rect.x > avatar_width or
            self.rect.y < 0 or
            self.rect.y > avatar_height):
            
            self.kill()
