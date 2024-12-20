from config import *
import pygame
import weapon
import config
import math



class Avatar(pygame.sprite.Sprite):
    def __init__(self, x_avatar_spawn, y_avatar_spawn, image, screen):
        super().__init__()

        self.x = x_avatar_spawn
        self.y = y_avatar_spawn

        self.image = pygame.image.load(image).convert_alpha()  # Ensure image is loaded correctly
        self.image = pygame.transform.scale(self.image, (config.avatar_width, config.avatar_height))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))


        self.gravity = 2
        self.jumping = False
        self.invincibility_in_use = False
        self.double_jump = False

        self.rise_timer = 0
        self.in_ground = True



        self.speed = config.speed_avatar
        self.health = config.health_avatar


        self.direction = True  # true if it is to the right

        self.current_weapon = "sword"

        self.sword = weapon.Sword(999, self.x, self.y, self.direction)    # # need to fill it with var necessary
        self.bow_arrow = weapon.BowArrow("images/weapon/Weapon_Arrow.png", self.x, self.y, self.direction, screen)  # need to fill it with var necessary

    def update(self, list_of_left_wall, list_of_right_wall, list_of_grounds, double_jump, list_of_roofs):
        self.lateral_movement(list_of_left_wall, list_of_right_wall)
        self.fall(list_of_grounds)
        self.jump(double_jump, list_of_roofs)
        self.attack()

        self.rect.topleft = (self.x, self.y)

    def lateral_movement(self, list_of_left_wall, list_of_right_wall):
        key = pygame.key.get_pressed()

        collided_left_wall = False
        for left_wall in list_of_left_wall:
            if self.rect.colliderect(left_wall):
                collided_left_wall = True
                break

        collided_right_wall = False
        for right_wall in list_of_right_wall:
            if self.rect.colliderect(right_wall):
                collided_right_wall = True
                break



        if key[pygame.K_LEFT] and self.x > 0 and not collided_left_wall:
            self.x -= self.speed
            self.direction_avatar = False
            print(self.x)


        elif key[pygame.K_RIGHT] and self.x < 720 and not collided_right_wall:
            self.x += self.speed
            self.direction = True
            print(self.x)




    def fall(self, list_of_grounds):
        collided_ground = False


        for ground in list_of_grounds:
            if self.rect.colliderect(ground):
                collided_ground = True
                break

        if not collided_ground:
            self.y += self.gravity
            self.in_ground = False


        else:
            self.in_ground = True
    def jump(self, double_jump, list_of_roofs):
        key = pygame.key.get_pressed()

        collided_roof = False
        for roof in list_of_roofs:
            if self.rect.colliderect(roof):
                collided_roof = True
                break

        if key[pygame.K_UP] and not self.jumping and self.in_ground:
            self.jumping = True
            self.in_ground = False
            self.rise_timer = fps*2

        elif key[pygame.K_UP] and self.jumping and double_jump:
            self.rise_timer = 0
            Avatar.jump(self, False, list_of_roofs)

        elif self.jumping and self.rise_timer > 0:
            self.y -= self.gravity*2

        if self.rise_timer <= 0 or collided_roof:
            self.rise_timer = 0
            self.jumping = False



        if self.in_ground:
            collided_roof = False
            jumping = False

        self.rise_timer -= 1


    def get_hurt(self, damage):
        if self.invincibility_in_use:
            self.health -= damage

    def attack(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:  # attack
            if self.current_weapon == "bow and arrow":
                self.bow_arrow.generate_arrow()
                self.bow_arrow.move_arrow()
                print("space")

            if self.current_weapon == "sword":
                self.sword.attack_area()


        if key[pygame.K_a]:       # switch to bow and arrow
            self.current_weapon = "bow and arrow"
            print("arrow")

        if key[pygame.K_s]:      # switch to sword
            self.current_weapon = "sword"








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

    def shoot_bat(self, bats_group):
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
        self.x_arrow = self.x_avatar + (avatar_width // 2)
        self.y_arrow = self.y_avatar + (avatar_height // 2)

        self.rect = self.image.get_rect(center=(self.x_arrow, self.y_arrow))

        if self.direction:  # for the right
            self.image = pygame.transform.rotate(self.image, self.right_angle)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.screen.blit(self.image, self.rect)


        else:  # for the left
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


