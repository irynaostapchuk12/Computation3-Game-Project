import pygame
from config import *
from settings import *
from avatar import Avatar
from settings import settings

# define the tile size
tile_size = 130
screen = pygame.display.set_mode(screen_resolution)


class World:
    def __init__(self, data):
        self.tile_list = []
        self.platform_for_game = pygame.image.load("backgroundgame_level/platform_levels.png")
        self.load_data(data)

    def load_data(self, data):
        self.tile_list = []
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(self.platform_for_game, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, None)  # Add a timer placeholder
                    self.tile_list.append(tile)

                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


# Platform configurations
world_data = [
    # draw the first row
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

]

world = World(world_data)


def execute_game(avatar):
    # SETUP:

    # setting up the background:
    bigimage = pygame.image.load("backgroundgame_level/background_of_level1.png").convert()

    # using the clock to control the time frame.
    clock = pygame.time.Clock()

    # screen setup:
    pygame.display.set_caption("Jungle Rex")

    # MAIN GAME LOOP
    running = True

    # Background position
    bg_x = 0

    # Create a sprite group and add the player
    all_sprites = pygame.sprite.Group()
    all_sprites.add(avatar)

    while running:

        # controlling the frame rate
        clock.tick(fps)

        # Get the mouse position
        mouse = pygame.mouse.get_pos()

        # Update and draw all sprites
        all_sprites.update()

        # Check if the player is moving
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
        # Update background position based on player movement
        #   if keys[pygame.K_RIGHT]:
        #      bg_x -= player.speed
        # elif keys[pygame.K_LEFT]:
        #    bg_x += player.speed

        # Update world tiles' positions based on player movement
        # for tile in world.tile_list:
        #   if keys[pygame.K_RIGHT]:
        #      tile[1].x -= player.speed
        # elif keys[pygame.K_LEFT]:
        #    tile[1].x += player.speed

        # Draw the background image
        screen.blit(bigimage, (bg_x, -125))

        # Draw the world
        world.draw()

        # Draw all sprites
        #all_sprites.draw(screen)
        # settings image - click
        settings = pygame.image.load("backgroundgame_level/settings_button.png")

        settings_rect = settings.get_rect(topleft=(30, 50))  # position ajusted


        # handling events:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if settings_rect.collidepoint(event.pos):
                    settings()

            # showing settings image
        screen.blit(settings, (30, 50))

        # Update the display
        pygame.display.flip()
    pygame.display.update()

    # the main while game loop has terminated and the game ends
    pygame.quit()


def game_loop():
    # creating the player for the game - only done once :)
    avatar = Avatar(100, 100, "images/icons/chest.png")

    # by default I start the game in the main area
    current_state = "main"

    # "endless" game loop:
    while True:
        current_state = execute_game(avatar)
        screen.blit(avatar.generate())


