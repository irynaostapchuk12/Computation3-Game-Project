import pygame

#from game import execute_game
from utils import *  # no need to import pygame because the import is in utils
from config import *  # importing colors and the like

import sys
import inventory

inventory_dict = {
                "others": {"coin" : 0,

              "powerup": {
                            "invincibility": 0,

                            "de_spawner":   0,

                            "double_jump":   0,

                            "double_coins": 0,

              },
              "elixir": {
                            "health": 0,

                            "speed": 0}
              }

            }


def purchase_item(type, name, quantity, price):
    if price <= inventory_dict["others"]["coin"]:
        inventory_dict[type][name] += 1
        inventory_dict["others"]["coin"] -= price


    else:
        print("cannot purchase")




def use_item(type, name):
    if inventory_dict[type][name] >= 1:
        inventory_dict[type][name] -= 1
        print("used an item")

    else:
        print("dont have this item")

