import math
from config import *

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


