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
import config



class Sword:
    def __init__(self, x_character, y_character, direction_character, weapon_reach):
        self.x_character = x_character
        self.y_character = y_character

        self.direction_character = direction_character
        self.weapon_reach = weapon_reach

    def attack_area(self):
        if self.direction_character: # if direction is the right
            return pygame.Rect(self.x_character + config.width_character, self.y_character ,self.x_character + config.width_character + self.weapon_reach,  self.y_character + config.height_character)

        elif self.direction_character: # if direction is false then left
            return pygame.Rect(self.x_character, self.y_character, - self.weapon_reach, config.height_character)


class Fist:
    def __init__(self, x_character, y_character, direction_character):
        self.x_character = x_character
        self.y_character = y_character

        self.direction_character = direction_character


    def attack_area(self):
        if self.direction_character: # if direction is the right
            return pygame.Rect(self.x_character + (config.width_character//2), self.y_character, config.width_character // 2, config.height_character)

        elif self.direction_character: # if direction is false then left
            return pygame.Rect(self.x_character + (config.width_character//2), self.y_character, - config.width_character//2, config.height_character)


    # tert cuidado que aqui o direction é 1 ou -1

class BowArrow:

    def __init__(self, x_arrow_spawn, y_arrow_spawn, x_size, y_size, x_location, y_location, direction_character, image):
        self.x_spawn = x_spawn
        self.y_spawn = y_spawn

        self.x_size = x_size
        self.y_size = y_size

        self.x_location = x_location
        self.y_location = y_location

        self.direction_character = direction_character
        self.speed = 7

        self.arrow_image = pygame.image.load(f"{image}")
        self.arrow_image = pygame.transform.scale(self.arrow_image, (self.x_size, self.y_size))




    def generate(self):
        # needs to have screen created
        screen.blit(self.arrow_image, (self.x_spawn, self.y_spawn))

        if self.direction_character: # for the right
            pass

        elif self.direction_character: # for the left
            pass


    def movement(self):

        self.x_location += int(self.speed * math.cos(self.direction))
        self.y_location += int(self.speed * math.sin(self.direction))



        # in here i need the vars of the screen size
        if self.rect.x < 0 or self.rect.x > config.width_character or self.rect.y < 0 or self.rect.y > config.height_character:
            self.kill()


