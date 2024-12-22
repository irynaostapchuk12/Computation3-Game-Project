from config import *
from abc import ABC, abstractmethod


class Powerup(ABC, pygame.sprite.Sprite):
    def __init__(self, name, x, y, screen, avatar, target, colour):
        super().__init__()


        self.name = name
        self.x = x
        self.y = y

        self.colour = colour

        self.target = target

        self.avatar = avatar
        self.screen = screen

        self.image = pygame.image.load(f"images/icons/{self.name}.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, game_icons_size)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.unused = True
        self.in_use = True

        self.timer = 0
        self.duration = 4


    @abstractmethod
    def update(self):
        self.generate()
        self.collision(self.avatar)
        self.tone()
        self.use(self.target)

    @abstractmethod
    def tone(self):
        self.avatar.image.fill(self.colour, special_flags=pygame.BLEND_RGBA_MULT

    @abstractmethod
    def generate(self):
        if self.unused:
            self.screen.blit(self.image, (self.x, self.y))

    @abstractmethod
    def collision(self, player):
        if pygame.sprite.spritecollideany(self, player):
            self.unused = False
            self.timer = fps * self.duration
            self.in_use = True

    @abstractmethod
    def affect_player(self):
        pass

    @abstractmethod
    def affect_game(self):
        pass


    @abstractmethod
    def use(self, type):
        if not self.unused:

            if self.timer > 0:
                self.timer -= 1

                if type == "player":
                    self.affect_player()
                elif type == "game":
                    self.affect_game()

            elif self.timer <= 0:
                self.in_use = False
                self.kill()




