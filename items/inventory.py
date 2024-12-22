import pygame

#from game import execute_game
from config import *  # importing colors and the like

import sys

inventory_dict = {
                  "others": {"coin" : 100},

                  "powerup": {
                            "invincibility": 0,

                            "de_spawner":   0,

                            "double_jump":   0,

                            "double_coins": 0,

                  },
                  "elixir": {
                            "health": 0,

                            "speed": 0
                  },
                  "skin": {
                            "JungleRex": True,
                            "BusinessMan": False,
                            "Princess": False,
                            "Warrior": False
                  },
                  "weapons": {
                            "fist": True,
                            "sword": False,
                            "bow": False
                  }



                  }





def purchase_item(type, name, price):
    if price <= inventory_dict["others"]["coin"]:
        if type == "skin" or type == "weapons":
            inventory_dict[type][name] = True
            inventory_dict["others"]["coin"] -= price

        else:
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


