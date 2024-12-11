from config import *
import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.color = color

class Vampire(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50, VAMPIRE_COLOR)
        self.last_bullet_time = 0

    def shoot_bat(self, bullets_group):
        now = pygame.time.get_ticks()
        if now - self.last_bullet_time > 1000:  # Shoot every second
            self.last_bullet_time = now
            bat = Bullet(self.rect.centerx, self.rect.bottom, BAT_COLOR)
            bullets_group.add(bat)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 720:  # Remove bullet if off screen
            self.kill()

class Skeleton(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, 40, 60, SKELETON_COLOR)
        self.speed = random.choice([-2, 2])

    def update(self):
        self.rect.x += self.speed
        if self.rect.left < 0 or self.rect.right > 720:
            self.speed *= -1

class Zombie(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, 60, 80, ZOMBIE_COLOR)
        self.speed = 1

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 720:
            self.rect.y = -self.rect.height  # Reset position if off screen


# create the groups
all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

# Create enemies
vampire = Vampire(200, 100)
skeleton = Skeleton(400, 200)
zombie = Zombie(600, 50)

# add enemies to the groups
all_sprites.add(vampire, skeleton, zombie)
enemy_group.add(vampire, skeleton, zombie)

