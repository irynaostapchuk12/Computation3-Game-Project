# Config file used to set global variables and other settings
# COLORS AND PICTURES HERE FOR NOW
from typing import Tuple
import pygame
import sys
pygame.init()


# COLORS
dark_red = (138, 0, 0)  # Dark red for buttons
deep_black: tuple[int, int, int] = (19, 20, 20)  # Almost black for background
grey = (59, 60, 60)  # Dark grey for alternate buttons
white = (254, 255, 255)  # White for readable text
glowing_light_red = (239, 128, 128)  # Light red for brighter text
blue = (0, 0, 255)
green = (34, 139, 34)
yellow = (255, 255, 0)
red = (150, 0, 24)
cute_purple = (128, 0, 128)
greenish = (182, 215, 168)



# SCREEN RESOLUTION
screen_resolution = (720, 720)  # height/width
screen_width = screen_resolution[0]
screen_height = screen_resolution[1]


resolution_title = (350,350)  #--------------------------------------------------------
resolution_back_jungle = (720, 720)  #------------------------------------------------
resolution_credits = (600, 600)

scrollable_shop_resolution = (720, 1400)
scrollable_shop_width = scrollable_shop_resolution[0]
scrollable_shop_height = scrollable_shop_resolution[1]

fps = 60




# SIZES
chest_image_size = (150, 150)
coin_shop_image_size = (20, 20)
double_coins_image_size = (190, 144)
avatar_size = (50, 100)
avatar_width = avatar_size[0]
avatar_height = avatar_size[1]

enemy_size = (40, 40)


arrow_size = (100, 100)

game_icons_size = (10,10)

rule_board_size = (720, 720)



#CHARACTER STATS

speed_avatar = 3
health_avatar = 0



# SHOP POSITIONS

# 30 is the padding
# 50 is the letter
# 60 for space between rects
# 30+50+60=140+110=250
health_elixir_shop_position = (30, 100)
speed_elixir_shop_position = (390, 100)

# 250 is the previous space
# 50 is the letter
# 300 is the size of the image
# 10 is the space between image and word
# 60 is the new space between rects
# 110 for coin and tag
# 140+50+300+10+60=560+110=780
invincibility_powerup_shop_position = (30,420)
de_spawner_powerup_shop_position = (390,420)


# 670 is previous space
# 50 is the letter
# 300 is the size of the image
# 10 is the space between image and word
# 60 is the new space between rects
# 110 is coin and tag
# 560+50+300+10+60=980
double_jump_powerup_shop_position = (30,740)
double_coins_powerup_shop_position = (390,740)


chest_shop_position = (210, 1060)







#FONT
def corbelfont(size=20):
    return pygame.font.SysFont("Corbel", size)

#corbelfont = pygame.font.SysFont("Corbel", 20)
poppins = pygame.font.Font("fonts/Cocogoose-Classic-Medium-trial.ttf")
comicsansfont = pygame.font.SysFont("Comic Sans MS", 50)
# creating the fonts:
custom_font = "leters/Cocogoose-Classic-Medium-trial.ttf"
font_size = 30
custom_font = pygame.font.SysFont(custom_font, font_size)
poppins = pygame.font.SysFont("Poppins-Regular.ttf", 35)
verdana = pygame.font.SysFont("Verdana", 40)






# setting the fonts
font_size = 45

custom_font_intro = pygame.font.SysFont("poppins", font_size)
poppins = pygame.font.SysFont("letere", 40)
verdana = pygame.font.SysFont("Verdana", 55)
verdana_settings = pygame.font.SysFont("Verdana", 28)
verdana_store = pygame.font.SysFont("Verdana", 20)

# PRICES
chest_price = 0
health_elixir_price = 0
speed_elixir_price = 0
invincibility_powerup_price = 0
de_spawner_powerup_price = 0
double_jump_powerup_price = 0
double_coins_powerup_price = 0



# ENEMIES (change later)
VAMPIRE_COLOR = (255, 0, 0)
BAT_COLOR = (0, 0, 255)
SKELETON_COLOR = (200, 200, 200)
ZOMBIE_COLOR = (0, 255, 0)