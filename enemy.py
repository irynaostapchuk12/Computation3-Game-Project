from config import *
import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_x, enemy_y, enemy_width, enemy_height, color):
        super().__init__()
        self.image = pygame.Surface((enemy_width, enemy_height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(enemy_x, enemy_y))
        self.color = color

class Vampire(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50, VAMPIRE_COLOR)
        self.last_bullet_time = 0

    def shoot_bat(self, bullets_group):
        now = pygame.time.get_ticks()
        if now - self.last_bullet_time > 1000:  # Shoot every second
            self.last_bullet_time = now
            bat = Bat(self.rect.centerx, self.rect.bottom, BAT_COLOR)
            bats_group.add(bat)



class Bat(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self, left_side_platform=0, right_side_platform=720):
        self.rect.y += self.speed
        if self.rect.left < left_side_platform or self.rect.right > right_side_platform:  # Remove bullet if off screen
            self.kill()

class Skeleton(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, 40, 60, SKELETON_COLOR)
        self.speed = 1

    def update(self, left_side_platform=0, right_side_platform=720):
        self.rect.x += self.speed
        if self.rect.left < left_side_platform or self.rect.right > right_side_platform:
            self.speed *= -1

class Zombie(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, 60, 80, ZOMBIE_COLOR)
        self.speed = 1

    def update(self, left_side_platform=0, right_side_platform=720):
        self.rect.y += self.speed
        if self.rect.left < left_side_platform or self.rect.right > right_side_platform:
            self.speed *= -1


# create the groups
all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bats_group = pygame.sprite.Group()

# Create enemies
vampire = Vampire(200, 100)
skeleton = Skeleton(400, 200)
zombie = Zombie(600, 50)

# add enemies to the groups
all_sprites.add(vampire, skeleton, zombie)
enemy_group.add(vampire, skeleton, zombie)

