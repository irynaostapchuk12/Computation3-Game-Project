from config import *
import pygame
from weapon import *

class Skeleton(pygame.sprite.Sprite):
    def __init__(self, x, y, left_side_platform=0, right_side_platform=720):
        super().__init__()
        self.speed = 1

        self.direction = True
        self.x = x
        self.y = y

        self.left_side_platform = left_side_platform
        self.right_side_platform = right_side_platform


        self.skeleton_1, self.skeleton_2, self.skeleton_stopped = self.load_skin("skeleton")
        self.image = self.skeleton_stopped

        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        # animation control variables
        self.animation_timer = 0
        self.animation_interval = 500  # 500ms between frame switches
        self.current_frame = 0  # 0 for run_1, 1 for run_2
        self.is_moving = False


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



    def update(self, left_side_platform=0, right_side_platform=720):
        self.movement()
        self.animate(self.skeleton_1, self.skeleton_2, self.skeleton_stopped)

