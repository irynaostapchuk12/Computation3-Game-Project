from config import *
import pygame
import weapon
import config


class Avatar(pygame.sprite.Sprite):
    def __init__(self, x_avatar_spawn, y_avatar_spawn, image, screen):
        super().__init__()

        self.x = x_avatar_spawn
        self.y = y_avatar_spawn

        self.image = pygame.image.load(image).convert_alpha()  # Ensure image is loaded correctly
        self.image = pygame.transform.scale(self.image, (config.avatar_width, config.avatar_height))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        # gravity and movement attributes
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

        # load animation frames
        self.run_1 = pygame.image.load("run_1.png").convert_alpha()
        self.run_1 = pygame.transform.scale(self.run_1, (config.avatar_width, config.avatar_height))

        self.run_2 = pygame.image.load("run_2.png").convert_alpha()
        self.run_2 = pygame.transform.scale(self.run_2, (config.avatar_width, config.avatar_height))

        self.stopped = pygame.image.load("stopped.png").convert_alpha()
        self.stopped = pygame.transform.scale(self.stopped, (config.avatar_width, config.avatar_height))

        # animation control variables
        self.animation_timer = 0
        self.animation_interval = 500  # 500ms between frame switches
        self.current_frame = 0  # 0 for run_1, 1 for run_2
        self.is_moving = False

        # weapons        
        self.sword = weapon.Sword(999, self.x, self.y, self.direction)    # # need to fill it with var necessary
        self.bow_arrow = weapon.BowArrow("images/weapon/Weapon_Arrow.png", self.x, self.y, self.direction, screen)  # need to fill it with var necessary

    def update(self, list_of_left_wall, list_of_right_wall, list_of_grounds, double_jump, list_of_roofs):
        self.lateral_movement(list_of_left_wall, list_of_right_wall)
        self.fall(list_of_grounds)
        self.jump(double_jump, list_of_roofs)
        self.attack()
        self.animate()

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

    def animate(self):
        current_time = pygame.time.get_ticks()

        if self.is_moving:
            # switching frames every 500ms
            if current_time - self.animation_timer > self.animation_interval:
                self.animation_timer = current_time
                self.current_frame = 1 - self.current_frame  # Toggle between 0 and 1

            # updating the image based on the current frame
            self.image = self.run_1 if self.current_frame == 0 else self.run_2
        else:
            # stopped image when not moving
            self.image = self.stopped


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
