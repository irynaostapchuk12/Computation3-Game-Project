from characters.avatar import Avatar
from config import *

# from second_level import execute_game_second_level


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

        self.list_of_left_wall = []
        self.list_of_right_wall = []
        self.list_of_roofs = []
        self.list_of_grounds = []


    def load_data(self, data):
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    self.image = pygame.transform.scale(self.platform_for_game,(tile_size, tile_size))  # Load the platform image
                    self.rect = self.image.get_rect()  # Get the rectangle of the platform image
                    self.rect.x = col_count * (tile_size * 0.715)  # Position the platform in the column
                    self.rect.y = row_count * (tile_size * 0.715)  # Position the platform in the row
                    tile = (self.image, self.rect)  # Add a timer placeholder
                    self.tile_list.append(tile)

                col_count += 1
            row_count += 1

    def draw(self, scroll_speed):
        for tile in self.tile_list:  # Draw each platform
            tile[1].x += scroll_speed
            screen.blit(tile[0], tile[1])  # Draw the platform image at the platform rectangle


    def get_limits(self):

        for tile in self.tile_list:
            self.rect = tile[1]
            left_wall = pygame.Rect(self.rect.x, self.rect.y + 80, 1, self.rect.height)  # (x=100, y=100, width=200, height=150)
            right_wall = pygame.Rect(self.rect.x + self.rect.width, self.rect.y +80, 1, self.rect.height)  # (x=100, y=100, width=200, height=150)
            roof = pygame.Rect(self.rect.x, self.rect.y + self.rect.height, self.rect.width, 1)  # (x=100, y=100, width=200, height=150)
            ground = pygame.Rect(self.rect.x, self.rect.y + 70, self.rect.width, 1)  # (x=100, y=100, width=200, height=150)

            self.list_of_left_wall.append(left_wall)
            self.list_of_right_wall.append(right_wall)
            self.list_of_roofs.append(roof)
            self.list_of_grounds.append(ground)


world_data = [
    # draw the first row
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

]

world = World(world_data)
world.get_limits()

list_of_left_wall = world.list_of_left_wall
list_of_right_wall = world.list_of_right_wall
list_of_roofs = world.list_of_roofs
list_of_grounds = world.list_of_grounds


def button_when_scroll_stop():
    poppins = pygame.font.Font("fonts/Cocogoose-Classic-Medium-trial.ttf", 35)

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


def execute_game():
    # SETUP:

    double_jump = False
    bigimage = pygame.image.load("backgroundgame_level/background_of_level1.png").convert()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Jungle Rex")

    running = True
    bg_x = 0
    bg_width = bigimage.get_width()

    avatar = Avatar(40, 0, "images/avatar/JungleRex (1).png", bigimage)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(avatar)

    while running:
        clock.tick(fps)  # Control frame rate
        mouse = pygame.mouse.get_pos()
        all_sprites.update(list_of_left_wall, list_of_right_wall, list_of_grounds, double_jump, list_of_roofs)
        scroll_speed = 0
        # world.update()  # Update the world to scroll platforms





        # Check if the player is in the middle of the screen
        if avatar.rect.centerx > 750 // 2:
            # Ensure scrolling stops when the background reaches its extremity
            if bg_x > -(bg_width - screen.get_width()):  # Limit scroll to the image width
                scroll_speed -= avatar.speed  # Scroll the platforms
                bg_x -= avatar.speed  # Scroll the background
                avatar.rect.centerx = 750 // 2  # Keep player in the center of the screen
            else:
                scroll_speed = 0  # Stop scrolling completely
                button_when_scroll_stop()

        elif avatar.rect.centerx < 750 // 2 and bg_x < 0:
            # Allow scrolling back when the player moves left
            scroll_speed += avatar.speed  # Scroll the platforms back
            bg_x += avatar.speed  # Scroll the background back
            avatar.rect.centerx = 750 // 2  # Keep player in the center of the screen

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




def game_loop():
    # by default I start the game in the main area
    current_state = "level_1"

    # "endless" game loop:
    while True:
        if current_state == "level_1":
            current_state = execute_game()
        elif current_state == "level_2":
            pass
            #current_state = shed(avatar)



