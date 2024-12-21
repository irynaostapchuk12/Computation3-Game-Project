import pygame
from game import execute_game
from characters import *
from items import *
from pages import *
from config import *



def game_loop():
    # by default I start the game in the main area
    current_state = "interface"

    # "endless" game loop:
    while True:
        if current_state == "level_1":
            current_state = execute_game()
        elif current_state == "interface":
            current_state = interface()
        elif current_state == "settings":
            current_state = settings()




