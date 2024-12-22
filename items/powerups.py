from config import *


class Powerup(pygame.sprite.Sprite):
    def __init__(self, x, y, powerup, screen, avatar):
        super().__init__()

        self.x = x
        self.y = y

        self.avatar = avatar
        self.powerup = powerup
        self.screen = screen

        self.image = pygame.image.load(f"images/icons/{self.powerup}.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, game_icons_size)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.unused = True
        self.in_use = True

        self.timer = 0

    def generate(self):

        if self.unused:
            self.screen.blit(self.image, (self.x, self.y))

    def use(self):
        if pygame.sprite.spritecollideany(self, self.avatar) and self.unused:
            self.unused = False
            self.timer = fps*4
            self.in_use = True

        if not self.unused:

            if self.timer > 0:
                self.timer -= 1

            elif self.timer <= 0:
                self.in_use = False
                self.kill()
