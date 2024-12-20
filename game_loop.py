from pages import *
from character import *




def game_loop():
    # by default I start the game in the main area
    current_state = "interface"
    avatar = Avatar()


    # "endless" game loop:
    while True:
        if current_state == "interface":
            current_state = interface()


        elif current_state == "store":
            current_state = store()

        elif current_state == "settings":
            current_state = settings_function()

        elif current_state == "rules":
            current_state = rules()

        elif current_state == "credits":
            current_state = credits_()


        elif current_state == "level_1":
            current_state = execute_game(avatar)

        elif current_state == "level_2":
            current_state = shed(avatar)

        elif current_state == "level_3":
            current_state = shed(avatar)