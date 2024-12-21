from config import *
from characters import avatar


class Powerup(pygame.sprite.Sprite):
    def __init__(self, x, y, powerup, screen):
        super().__init__()

        self.x = x
        self.y = y

        self.screen = screen

        self.image = pygame.image.load(f"images/icons/{powerup}.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, game_icons_size)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.invincibility_not_used = True
        self.invincibility_timer = 0

    def invincibility_icon(self):

        if self.invincibility_not_used:
            self.screen.blit(self.image, (self.x, self.y))


        if avatar.Avatar.rect.colliderect(self.rect) and self.invincibility_not_used:
            self.invincibility_not_used = False
            self.invincibility_timer = fps*4
            avatar.Avatar.invincibility_in_use = True



        if not self.invincibility_not_used and self.invincibility_timer > 0:
            self.invincibility_timer -= 1


        elif not self.invincibility_not_used and self.invincibility_timer <= 0:
            avatar.Avatar.invincibility_in_use = False
            self.kill()



































class Invincibility(pygame.sprite.Sprite):

    def __init__(self, invincibility_x_spawn, invincibility_y_spawn):
        super().__init__()

        self.invincibility_x_spawn = invincibility_x_spawn
        self.invincibility_y_spawn = invincibility_y_spawn

        self.invincibility_image = pygame.image.load(f"../images/icons/invincibility.png").convert_alpha()
        self.invincibility_image = pygame.transform.scale(self.invincibility_image, game_icons_size)
        self.invincibility_rect = self.invincibility_image.get_rect(topleft=(self.invincibility_x_spawn, self.invincibility_y_spawn))

        self.invincibility_not_used = True
        self.invincibility_timer = 0

    def invincibility_icon(self): 

        if self.invincibility_not_used:
            screen.blit(self.invincibility_image, (self.invincibility_x_spawn, self.invincibility_y_spawn))


        if avatar.Avatar.rect.colliderect(self.invincibility_rect) and self.invincibility_not_used:
            self.invincibility_not_used = False
            self.invincibility_timer = fps*4
            avatar.Avatar.invincibility_in_use = True



        if not self.invincibility_not_used and self.invincibility_timer > 0:
            self.invincibility_timer -= 1


        elif not self.invincibility_not_used and self.invincibility_timer <= 0:
            avatar.Avatar.invincibility_in_use = False
            self.kill()



class Double_jump(pygame.sprite.Sprite):
    def __init__(self, double_jump_x_spawn, double_jump_y_spawn):
        super().__init__()

        self.double_jump_x_spawn = double_jump_x_spawn
        self.double_jump_y_spawn = double_jump_y_spawn

        self.double_jump_image = pygame.image.load(f"../images/icons/double_jump.png").convert_alpha()
        self.double_jump_image = pygame.transform.scale(self.double_jump_image, game_icons_size)
        self.double_jump_rect = self.double_jump_image.get_rect(topleft=(self.double_jump_x_spawn, self.double_jump_y_spawn))

        self.double_jump_not_used = True
        self.double_jump_timer = 0

    def double_jump_icon(self):
        if self.double_jump_not_used:
            screen.blit(self.double_jump_image, (self.double_jump_x_spawn, self.double_jump_y_spawn))

        if avatar.Avatar.avatar_rect.colliderect(self.double_jump_rect) and self.double_jump_not_used:
            self.double_jump_not_used = False
            self.double_jump_timer = fps * 4
            avatar.Avatar.double_jump_in_use = True  



        if not self.double_jump_not_used and self.double_jump_timer > 0:
            self.double_jump_timer -= 1

        elif not self.double_jump_not_used and self.double_jump_timer <= 0:
            avatar.Avatar.double_jump_in_use = False
            self.kill()  






def double_coins_icon(self):
        pass

class De_spawner(pygame.sprite.Sprite):


    def de_spawner_icon(self):
        pass

