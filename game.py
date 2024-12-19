import pygame
import sys
from avatar import Avatar
from settings import settings_function
from config import *

# from second_level import execute_game_second_level


# define the tile size
tile_size = 150
screen = pygame.display.set_mode((720, 720))

global all_sprites


class World:
    def _init_(self, data):
        self.tile_list = []
        self.platform_for_game = pygame.image.load("backgroundgame_level/platform_levels.png")
        self.load_data(data)
        self.scroll_speed = 55  # Speed at which platforms scroll
        self.scroll_timer = 0  # Timer to control scrolling

    def load_data(self, data):
        self.tile_list = []
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(self.platform_for_game,(tile_size, tile_size))  # Load the platform image
                    img_rect = img.get_rect()  # Get the rectangle of the platform image
                    img_rect.x = col_count * (tile_size * 0.715)  # Position the platform in the column
                    img_rect.y = row_count * (tile_size * 0.715)  # Position the platform in the row
                    tile = (img, img_rect, None)  # Add a timer placeholder
                    self.tile_list.append(tile)

                col_count += 1
            row_count += 1

    def draw(self, scroll_speed):
        for tile in self.tile_list:  # Draw each platform
            tile[1].x += scroll_speed
            screen.blit(tile[0], tile[1])  # Draw the platform image at the platform rectangle


world_data = [
    # draw the first row
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

]

world = World()

fps = 60

















































# Classe para as Plataformas
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=GREEN):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.list_of_left_wall = []
        self.list_of_right_wall = []
        self.list_of_roofs = []
        self.list_of_grounds = []


    def get_limits(self):


        left_wall = pygame.Rect(self.rect.x, self.rect.y, 0, self.rect.get_height())  # (x=100, y=100, width=200, height=150)
        right_wall = pygame.Rect(self.rect.x + self.rect.get_width(), self.rect.y, 0, self.rect.get_height())  # (x=100, y=100, width=200, height=150)
        roof = pygame.Rect,(self.rect.x, self.rect.y, self.rect.get_width(), 0)  # (x=100, y=100, width=200, height=150)
        ground = pygame.Rect(self.rect.x, self.rect.y + self.rect.get_height(), self.rect.get_width(), 0)  # (x=100, y=100, width=200, height=150)

        self.list_of_left_wall.append(left_wall)
        self.list_of_right_wall.append(right_wall)
        self.list_of_roofs.append(roof)
        self.list_of_grounds.append(ground)






# Grupo de plataformas
platforms = pygame.sprite.Group()

# Criar as plataformas
ground = Platform(0, HEIGHT - 20, WIDTH, 20, GRAY)  # Chão
platform1 = Platform(200, 600, 200, 20)
platform2 = Platform(450, 450, 150, 20)
platform3 = Platform(100, 300, 180, 20)
platform4 = Platform(350, 150, 200, 20)

list_of_left_wall = []
list_of_right_wall = []
list_of_roofs = []
list_of_grounds = []
list_of_list = [list_of_left_wall, list_of_right_wall, list_of_roofs, list_of_grounds]

for a in range(4):
    pre_list = get_walls(eval(f"platform{a+1}"))
    for b in range(4):
        list_of_list.append(pre_list[b])




platforms.add(ground, platform1, platform2, platform3, platform4)
















def execute_game(player):
    # SETUP:
    bigimage = pygame.image.load("backgroundgame_level/background_of_level1.png").convert()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Jungle Rex")

    running = True
    bg_x = 0
    bg_width = bigimage.get_width()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    while running:
        clock.tick(fps)  # Control frame rate
        mouse = pygame.mouse.get_pos()
        all_sprites.update()
        scroll_speed = 0
        # world.update()  # Update the world to scroll platforms

        avatar = Avatar()
        avatar.update()
        avatar.lateral_movement()
        avatar.fall()
        avatar.jump()
        avatar.attack()


        # Check if the player is in the middle of the screen
        if player.rect.centerx > 750 // 2:
            # Ensure scrolling stops when the background reaches its extremity
            if bg_x > -(bg_width - screen.get_width()):  # Limit scroll to the image width
                scroll_speed -= player.speed  # Scroll the platforms
                bg_x -= player.speed  # Scroll the background
                player.rect.centerx = 750 // 2  # Keep player in the center of the screen
            else:
                scroll_speed = 0  # Stop scrolling completely
                button_when_scroll_stop()

        elif player.rect.centerx < 750 // 2 and bg_x < 0:
            # Allow scrolling back when the player moves left
            scroll_speed += player.speed  # Scroll the platforms back
            bg_x += player.speed  # Scroll the background back
            player.rect.centerx = 750 // 2  # Keep player in the center of the screen

        screen.blit(bigimage, (bg_x, -125))  # Draw the background
        world.draw(scroll_speed)  # Draw the platforms
        all_sprites.draw(screen)  # Draw the player

        # setting the settings button
        settings = pygame.image.load("backgroundgame_level/settings_button.png")
        settings_rect = settings.get_rect(topleft=(30, 50))
        screen.blit(settings, (30, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if settings_rect.collidepoint(event.pos):
                    settings_function()

        pygame.display.flip()
    pygame.display.update()


def button_when_scroll_stop():
    poppins = pygame.font.Font("leters/Cocogoose-Classic-Medium-trial.ttf", 35)

    # creating the button
    button_text = poppins.render("CLICK HERE TO NEXT LEVEL", True, deep_black)
    button_rect = button_text.get_rect(center=(90 + 540 // 2, 123 + 60 // 2))

    while True:

        # getting the mouse position (future need)
        mouse = pygame.mouse.get_pos()

        # event detection (future work)
        for ev in pygame.event.get():
            # seeing if the user hits the red x button
            if ev.type == pygame.QUIT:
                sys.exit()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(ev.pos):
                    execute_game_second_level()

            if button_rect.collidepoint(mouse):
                button_text = poppins.render("CLICK HERE TO NEXT LEVEL", True, (255, 255, 255))
            else:
                button_text = poppins.render("CLICK HERE TO NEXT LEVEL", True, (0, 0, 0))

        screen.blit(button_text, button_rect)
        pygame.display.update()


def game_loop():
    # by default I start the game in the main area
    current_state = "level_1"

    # "endless" game loop:
    while True:
        if current_state == "level_1":
            current_state = execute_game(avatar)
        elif current_state == "level_2":
            pass
            #current_state = shed(avatar)



