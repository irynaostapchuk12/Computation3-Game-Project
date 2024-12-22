import pygame

class Bat(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, bat_image):
        super().__init__()
        self.image = pygame.image.load(bat_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))  # Adjust size as needed
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5  # Adjust the speed as needed
        self.direction = direction  # True for right, False for left

    def update(self):
        # Move the bat in the appropriate direction
        self.rect.x += self.speed if self.direction else -self.speed

        # Remove the bat if it goes off-screen
        if self.rect.right < 0 or self.rect.left > 720:
            self.kill()