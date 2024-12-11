# Config file used to set global variables and other settings
# COLORS AND PICTURES HERE FOR NOW
from typing import Tuple

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
resolution_title = (350,350)
resolution_back_jungle = (720, 720)
resolution_credits = (600, 600)
width, height = resolution[0], resolution[1]
fps = 60

# SIZES
player_size = (50, 100)
enemy_size = (40, 40)
bullet_size = 10



#CHARACTER
height_character = 0
width_character = 0
speed_character = 0
health_character = 0


# ENEMIES (change later)
VAMPIRE_COLOR = (255, 0, 0)
BAT_COLOR = (0, 0, 255)
SKELETON_COLOR = (200, 200, 200)
ZOMBIE_COLOR = (0, 255, 0)