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
resolution = (720, 720)  # height/width
resolution_scrollable_shop = (720, 3440)

resolution_title = (350,350)
resolution_back_jungle = (720, 720)
resolution_credits = (600, 600)


screen_width, screen_height = resolution[0], resolution[1]
scrollable_width = resolution_scrollable_shop[0]
scrollable_height = resolution_scrollable_shop[1]

fps = 60




# SIZES

shop_image_size = (300, 300)
coin_shop_image_size = (50, 50)
player_size = (50, 100)
enemy_size = (40, 40)
bullet_size = 10



#CHARACTER
height_character = 0
width_character = 0

speed_character = 0
health_character = 0





# SHOP POSITIONS

shop_text_position = (360, 30)


# 30 is the padding
# 50 is the letter
# 60 for space between rects
# 30+50+60=140+110=250
health_elixir_shop_position = (30, 140)
speed_elixir_shop_position = (390, 140)

# 250 is the previous space
# 50 is the letter
# 300 is the size of the image
# 10 is the space between image and word
# 60 is the new space between rects
# 110 for coin and tag
# 140+50+300+10+60=560+110=780
invincibility_powerup_shop_position = (30,670)
de_spawner_powerup_shop_position = (390,670)


# 670 is previous space
# 50 is the letter
# 300 is the size of the image
# 10 is the space between image and word
# 60 is the new space between rects
# 110 is coin and tag
# 560+50+300+10+60=980
double_jump_powerup_shop_position = (30,1200)
double_coins_powerup_shop_position = (390,1200)


chest_shop_position = (210, 2000)










#FONT
corbelfont = pygame.font.SysFont("Corbel", 40)






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