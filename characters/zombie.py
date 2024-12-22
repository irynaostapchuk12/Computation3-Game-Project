
"""
from config import *
import pygame
from weapon import *


class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, 60, 80, ZOMBIE_COLOR)

        self.image = pygame.Surface(width, height)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 1

    def update(self, left_side_platform=0, right_side_platform=720):
        self.rect.y += self.speed
        if self.rect.left < left_side_platform or self.rect.right > right_side_platform:
            self.speed *= -1
"""

import weapons
from config import *
import pygame
from weapon import *

class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y, avatar, left_side_platform=0, right_side_platform=720):
        super().__init__()
        self.speed = 1

        self.direction = True
        self.x = x
        self.y = y

        self.left_side_platform = left_side_platform
        self.right_side_platform = right_side_platform


        self.zombie_1, self.zombie_2, self.zombie_stopped = self.load_skin("zombie")
        self.image = self.zombie_stopped

        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        # animation control variables
        self.animation_timer = 0
        self.animation_interval = 500  # 500ms between frame switches
        self.current_frame = 0  # 0 for run_1, 1 for run_2
        self.is_moving = False #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        self.avatar = avatar


    def load_skin(self, skin):
        run_1 = pygame.image.load(f"images/enemy/{skin} (1).png").convert_alpha()
        run_1 = pygame.transform.scale(run_1, (avatar_width, avatar_height))

        run_2 = pygame.image.load(f"images/enemy/{skin} (2).png").convert_alpha()
        run_2 = pygame.transform.scale(run_2, (avatar_width, avatar_height))

        stopped = pygame.image.load(f"images/enemy/{skin} (3).png").convert_alpha()
        stopped = pygame.transform.scale(stopped, (avatar_width, avatar_height))

        return run_1, run_2, stopped

    def animate(self, image_1, image_2, image_stop):
        current_time = pygame.time.get_ticks()

        image_1_inv = pygame.transform.flip(image_1, True, False)
        image_2_inv = pygame.transform.flip(image_2, True, False)
        image_stop_inv = pygame.transform.flip(image_stop, True, False)

        if self.direction:
            # switching frames every 500ms
            if current_time - self.animation_timer > self.animation_interval:
                self.animation_timer = current_time
                self.current_frame = 1 - self.current_frame  # Toggle between 0 and 1

            # updating the image based on the current frame
            self.image = image_1 if self.current_frame == 0 else image_2

        elif not self.direction:
            # switching frames every 500ms
            if current_time - self.animation_timer > self.animation_interval:
                self.animation_timer = current_time
                self.current_frame = 1 - self.current_frame  # Toggle between 0 and 1

            # updating the image based on the current frame
            self.image = image_1_inv if self.current_frame == 0 else image_2_inv

    def movement(self):
        if self.direction:
            self.rect.x += self.speed

        else:
            self.rect.x -= self.speed



        if self.rect.left < self.left_side_platform:
            self.direction = True

        elif self.rect.right > self.right_side_platform:
            self.direction = False


    def attack(self):
        if self.rect.colliderect(self.avatar.rect):
            print("Zombie attacked!") # MUDAR PARA TIRAR 1 VIDA


    def update(self, left_side_platform=0, right_side_platform=720):
        self.movement()
        self.animate(self.zombie_1, self.zombie_2, self.zombie_stopped)
        self.attack()

