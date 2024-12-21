import math
from config import *

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
