
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
import avatar



class Sword(avatar):
    def __init__(self, weapon_reach):

        super.__init__(self.x_avatar, self.y_avatar, self.direction_avatar)

        self.weapon_reach = weapon_reach

    def attack_area(self):
        if self.direction_character: # if direction is the right
            return pygame.Rect(self.x_avatar + config.width_avatar, self.y_avatar, self.x_avatar + config.width_avatar + self.weapon_reach,  self.y_avatar + config.height_avatar)

        elif self.direction_character: # if direction is false then left
            return pygame.Rect(self.x_avatar, self.y_avatar, - self.weapon_reach, config.height_avatar)




class Fist(avatar):
    def __init__(self):

        super.__init__(self.x_avatar, self.y_avatar, self.direction_avatar)



    def attack_area(self):
        if self.direction_character: # if direction is the right
            return pygame.Rect(self.x_avatar + (config.width_avatar//2), self.y_avatar, config.width_avatar // 2, config.height_avatar)

        elif self.direction_character: # if direction is false then left
            return pygame.Rect(self.x_avatar + (config.width_avatar//2), self.y_avatar, - config.width_avatar//2, config.height_avatar)


    # tert cuidado que aqui o direction é 1 ou -1

class BowArrow(avatar):

    def __init__(self, x_location, y_location,  image):

        super.__init__(self.x_avatar, self.y_avatar, self.direction_avatar)


        self.x_arrow_spawn = self.x_avatar + (config.width_avatar//2)
        self.y_arrow_spawn = self.y_avatar + (config.height_avatar//2)


        self.x_location = x_location
        self.y_location = y_location

        self.speed = 7

        self.arrow_image = pygame.image.load(f"{image}")
        self.arrow_image = pygame.transform.scale(self.arrow_image, config.arrow_size)
        self.arrow_rect = self.arrow_image.get_rect(center=(x_arrow_spawn, y_arrow_spawn))

        self.left_angle = 0
        self.right_angle = 0


    def arrow(self):
        # needs to have screen created
        screen.blit(self.arrow_image, (self.x_arrow_spawn, self.y_arrow_spawn))



        if self.direction_avatar: # for the right
            rotated_arrow_image = pygame.transform.rotate(self.arrow_image, self.right_angle)
            rotated_arrow_rect = rotated_arrow_image.get_rect(center=rotated_arrow_image.center)
            screen.blit(rotated_arrow_image, rotated_arrow_rect)




        else: # for the left
            rotated_arrow_image = pygame.transform.rotate(self.arrow_image, self.left_angle)
            rotated_arrow_rect = rotated_arrow_image.get_rect(center=rotated_arrow_image.center)
            screen.blit(rotated_arrow_image, rotated_arrow_rect)



        self.x_location += int(self.speed * math.cos(self.direction_avatar))
        self.y_location += int(self.speed * math.sin(self.direction_avatar))



        # in here i need the vars of the screen size
        if (rotated_arrow_rect < 0 or
            rotated_arrow_rect.x > config.width_avatar or
            rotated_arrow_rect.y < 0 or
            rotated_arrow_rect.y > config.height_avatar):

            self.kill()

