import math
from config import *


class BowArrow(pygame.sprite.Sprite):

    def __init__(self, image, screen):
        super().__init__()

        self.x_avatar = None
        self.y_avatar = None
        self.direction = None

        self.x = None
        self.y = None

        self.screen = screen

        self.speed = 7

        self.image = pygame.image.load(f"{image}")
        self.image = pygame.transform.scale(self.image, arrow_size)

        self.left_angle = 180
        self.right_angle = 0

    def update(self):
        self.move_arrow()

    def generate_arrow(self, x_avatar, y_avatar, direction):
        self.x = x_avatar + (avatar_width // 2)
        self.y = y_avatar + (avatar_height // 2)

        self.rect = self.image.get_rect(center=(self.x, self.y))

        if direction:  # for the right
            self.image = pygame.transform.rotate(self.image, self.right_angle)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.screen.blit(self.image, self.rect)


        else:  # for the left
            self.image = pygame.transform.rotate(self.image, self.left_angle)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.screen.blit(self.image, self.rect)

    def move_arrow(self):
        if self.direction:
            self.x += self.speed

        else:
            self.x -= self.speed

        # in here i need the vars of the screen size
        if (self.rect.x < 0 or self.rect.x > screen_width):

            self.kill()
