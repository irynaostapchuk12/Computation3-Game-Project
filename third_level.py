from player import Player
from shed import shed
from pages.settings import Settings_
from config import *


# define the tile size
tile_size = 150
screen = pygame.display.set_mode((720, 720))

global all_sprites


class World:
    def __init__(self, data):
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
                    img = pygame.transform.scale(self.platform_for_game,
                                                 (tile_size, tile_size))  # Load the platform image
                    img_rect = img.get_rect()  # Get the rectangle of the platform image
                    img_rect.x = col_count * tile_size  # Position the platform in the column
                    img_rect.y = row_count * tile_size  # Position the platform in the row
                    tile = (img, img_rect, None)  # Add a timer placeholder
                    self.tile_list.append(tile)

                col_count += 1
            row_count += 1

    def draw(self, scroll_speed):
        for tile in self.tile_list:  # Draw each platform
            tile[1].x += scroll_speed
            screen.blit(tile[0], tile[1])  # Draw the platform image at the platform rectangle


# Platform configurations
world_data = [
    # draw the first row
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

]

world = World(world_data)

fps = 60


def execute_game_third_level(player):
    # SETUP:
    bigimage = pygame.image.load("backgroundgame_level/background_of_level3.png").convert()
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
                    Settings_()

        pygame.display.flip()
    pygame.display.update()


def button_when_scroll_stop_levelthree():
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
                    the_end_of_game()

            if button_rect.collidepoint(mouse):
                button_text = poppins.render("CLICK HERE TO NEXT LEVEL", True, (255, 255, 255))
            else:
                button_text = poppins.render("CLICK HERE TO NEXT LEVEL", True, (0, 0, 0))

        screen.blit(button_text, button_rect)
        pygame.display.update()


def game_loop():
    # creating the player for the game - only done once :)
    player = Player()

    # by default I start the game in the main area
    current_state = "main"

    # "endless" game loop:
    while True:
        if current_state == "main":
            current_state = execute_game(player)
        elif current_state == "shed":
            current_state = shed(player)
