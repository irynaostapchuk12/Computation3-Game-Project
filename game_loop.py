import pygame
from game import execute_game
from characters import *
from items import *
from pages import *
from config import *
from second_level import *
from third_level import *
from data import store_account

def game_loop():

    store_account.load_data()

    # by default I start the game in the main area
    current_state = "interface"
    settings = Settings()
    settings.play()

    # "endless" game loop:
    while True:

        if current_state == "store":
            current_state = store()

        elif current_state == "rules":
            current_state = rules()

        elif current_state == "credits":
            current_state = credits_()

        elif current_state == "interface":
            current_state = interface()

        elif current_state == "settings":
            current_state = settings.run()

        elif current_state == "level_1":
            current_state = execute_game()

        elif current_state == "level_2":
            current_state = execute_game_second_level()

        elif current_state == "level_3":
            current_state = execute_game_third_level()




