import pygame

#from game import execute_game
from config import *  # importing colors and the like

import sys

pygame.init()  # calling pygame


store_dict = {
    "others": {
                "coin": {"image": None},
                "shop": {"text": None, "position": shop_text_position},
                "chest": {
                            "image": None,
                            "text": None,
                            "tag": None,
                            "combined": {
                                            "width": None,
                                            "height": None,
                                            "surface": None,
                                            "rect": None,
                                            "position": chest_shop_position,
                                            },
                            },
                },

    "powerup": {
                "invincibility": {
                                    "image": None,
                                    "text": None,
                                    "tag": None,
                                    "combined": {
                                                    "width": None,
                                                    "height": None,
                                                    "surface": None,
                                                    "rect": None,
                                                    "position": invincibility_powerup_shop_position,
                                                    },
                                    },
                "de_spawner": {
                                    "image": None,
                                    "text": None,
                                    "tag": None,
                                    "combined": {
                                                    "width": None,
                                                    "height": None,
                                                    "surface": None,
                                                    "rect": None,
                                                    "position": de_spawner_powerup_shop_position,
                                                    },
                                    },
                "double_jump": {
                                    "image": None,
                                    "text": None,
                                    "tag": None,
                                    "combined": {
                                                    "width": None,
                                                    "height": None,
                                                    "surface": None,
                                                    "rect": None,
                                                    "position": double_jump_powerup_shop_position,
                                                    },
                                    },
                "double_coins": {
                                    "image": None,
                                    "text": None,
                                    "tag": None,
                                    "combined": {
                                                    "width": None,
                                                    "height": None,
                                                    "surface": None,
                                                    "rect": None,
                                                    "position": double_coins_powerup_shop_position,
                                                    },
                                    },
        },
    "elixir": {
                "health": {
                                    "image": None,
                                    "text": None,
                                    "tag": None,
                                    "combined": {
                                                    "width": None,
                                                    "height": None,
                                                    "surface": None,
                                                    "rect": None,
                                                    "position": health_elixir_shop_position,
                                    },
                },
                "speed": {
                                    "image": None,
                                    "text": None,
                                    "tag": None,
                                    "combined": {
                                                    "width": None,
                                                    "height": None,
                                                    "surface": None,
                                                    "rect": None,
                                                    "position": speed_elixir_shop_position,
                                                    },
                                    },
                },
    }



def get_image(type, name, image, size):
    store_dict[type][name]["image"] = pygame.image.load(f"images/icons/{image}").convert_alpha()
    store_dict[type][name]["image"] = pygame.transform.scale(store_dict[type][name]["image"], size)



def get_combined(type, name):

    text = store_dict[type][name]["text"]
    image = store_dict[type][name]["image"]
    tag = store_dict[type][name]["tag"]
    coin = store_dict["others"]["coin"]["image"]

    text_width = text.get_width()
    image_width = image.get_width()
    tag_width = tag.get_width()
    coin_width = coin.get_width()

    text_height = text.get_height()
    image_height = image.get_height()
    tag_height = tag.get_height()
    coin_height = coin.get_height()

    combined_width = store_dict[type][name]["combined"]["width"]
    combined_height = store_dict[type][name]["combined"]["height"]
    combined_surface = store_dict[type][name]["combined"]["surface"]
    combined_position = store_dict[type][name]["combined"]["position"]
    combined_rect = store_dict[type][name]["combined"]["rect"]



    combined_width = max(image_width, text_width, coin_width + tag_width)
    combined_height = image_height + text_height + max(coin_width, tag_width) + 30
    combined_surface = pygame.Surface((combined_width + 50, combined_height + 50), pygame.SRCALPHA)


    wood_board = pygame.image.load(f"images/menus/wood_board.png").convert_alpha()
    wood_board = pygame.transform.scale(wood_board,(combined_width + 50, combined_height + 70))

    combined_surface.blit(wood_board, (0, 0))
    combined_surface.blit(text, (30, 40))
    combined_surface.blit(image, (30, text_height + 10 + 40))
    combined_surface.blit(tag, (30, text_height + image_height + 10 + 10 + 40))
    combined_surface.blit(coin, (tag_width + 10 + 30, text_height + image_height + 10 + 10 + 40))
    combined_rect = combined_surface.get_rect(topleft=combined_position)




    store_dict[type][name]["text"] = text
    store_dict[type][name]["image"] = image
    store_dict[type][name]["tag"] = tag
    store_dict["others"]["coin"]["image"] = coin

    store_dict[type][name]["combined"]["width"] = combined_width
    store_dict[type][name]["combined"]["height"] = combined_height
    store_dict[type][name]["combined"]["surface"] = combined_surface
    store_dict[type][name]["combined"]["position"] = combined_position
    store_dict[type][name]["combined"]["rect"] = combined_rect


def shop():
    scroll_y = 0
    scroll_speed = 1

    screen = pygame.display.set_mode(screen_resolution)

    scroll_surface = pygame.Surface(scrollable_shop_resolution, pygame.SRCALPHA)
    scroll_surface.fill((0, 0, 0, 0))



    background_image_shop = pygame.image.load(f"images/backgrounds/back_of_credits.jpg").convert_alpha()
    background_image_shop = pygame.transform.scale(background_image_shop, screen_resolution)




    store_dict["others"]["shop"]["text"] = corbelfont().render("SHOP", True, white)
    store_dict["others"]["chest"]["text"] = corbelfont().render("CHEST", True, white)
    store_dict["elixir"]["health"]["text"] = corbelfont().render("HEALTH ELIXIR", True, white)
    store_dict["elixir"]["speed"]["text"] = corbelfont().render("SPEED ELIXIR", True, white)
    store_dict["powerup"]["invincibility"]["text"] = corbelfont().render("INVINCIBILITY", True, white)
    store_dict["powerup"]["de_spawner"]["text"] = corbelfont().render("DE-SPAWNER", True, white)
    store_dict["powerup"]["double_jump"]["text"] = corbelfont().render("DOUBLE JUMP", True, white)
    store_dict["powerup"]["double_coins"]["text"] = corbelfont().render("DOUBLE COINS", True, white)

    store_dict["others"]["chest"]["tag"] = corbelfont(50).render(f"{chest_price}", True, white)
    store_dict["elixir"]["health"]["tag"] = corbelfont(50).render(f"{health_elixir_price}", True, white)
    store_dict["elixir"]["speed"]["tag"] = corbelfont(50).render(f"{speed_elixir_price}", True, white)
    store_dict["powerup"]["invincibility"]["tag"] = corbelfont(50).render(f"{invincibility_powerup_price}", True, white)
    store_dict["powerup"]["de_spawner"]["tag"] = corbelfont(50).render(f"{de_spawner_powerup_price}", True, white)
    store_dict["powerup"]["double_jump"]["tag"] = corbelfont(50).render(f"{double_jump_powerup_price}", True, white)
    store_dict["powerup"]["double_coins"]["tag"] = corbelfont(50).render(f"{double_coins_powerup_price}", True, white)

    get_image("others", "coin", "coin.png", coin_shop_image_size)
    get_image("others", "chest", "chest.png", shop_image_size)
    get_image("elixir", "health", "chest.png", shop_image_size)
    get_image("elixir", "speed", "chest.png", shop_image_size)
    get_image("powerup", "invincibility", "chest.png", shop_image_size)
    get_image("powerup", "de_spawner", "chest.png", shop_image_size)
    get_image("powerup", "double_jump", "double_jump.png", shop_image_size)
    get_image("powerup", "double_coins", "double_coins.png", shop_image_size)

    get_combined("others", "chest")
    get_combined("elixir", "health")
    get_combined("elixir", "speed")
    get_combined("powerup", "invincibility")
    get_combined("powerup", "de_spawner")
    get_combined("powerup", "double_jump")
    get_combined("powerup", "double_coins")

    store_dict["others"]["shop"]["rect"] = store_dict["others"]["shop"]["text"].get_rect(midtop=shop_text_position)



    while True:

        # getting the mouse position
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



            if ev.type == pygame.MOUSEBUTTONDOWN:
                if store_dict["elixir"]["health"]["combined"]["rect"].collidepoint(mouse):  # Check if mouse is inside the box
                    print("Box clicked!")

                if store_dict["elixir"]["speed"]["combined"]["rect"].collidepoint(mouse):  # Check if mouse is inside the box
                    print("Box clicked!")

                if store_dict["powerup"]["invincibility"]["combined"]["rect"].collidepoint(mouse):  # Check if mouse is inside the box
                    print("Box clicked!")

                if store_dict["powerup"]["de_spawner"]["combined"]["rect"].collidepoint(mouse):  # Check if mouse is inside the box
                    print("Box clicked!")

                if store_dict["powerup"]["double_jump"]["combined"]["rect"].collidepoint(mouse):  # Check if mouse is inside the box
                    print("Box clicked!")

                if store_dict["powerup"]["double_coins"]["combined"]["rect"].collidepoint(mouse):  # Check if mouse is inside the box
                    print("Box clicked!")

                if store_dict["others"]["chest"]["combined"]["rect"].collidepoint(mouse):  # Check if mouse is inside the box
                    print("Box clicked!")



        scroll_surface.blit(store_dict["others"]["shop"]["text"], store_dict["others"]["shop"]["rect"] )
        scroll_surface.blit(store_dict["others"]["chest"]["combined"]["surface"], store_dict["others"]["chest"]["combined"]["rect"].topleft)
        scroll_surface.blit(store_dict["elixir"]["health"]["combined"]["surface"], store_dict["elixir"]["health"]["combined"]["rect"].topleft)
        scroll_surface.blit(store_dict["elixir"]["speed"]["combined"]["surface"], store_dict["elixir"]["speed"]["combined"]["rect"].topleft)
        scroll_surface.blit(store_dict["powerup"]["invincibility"]["combined"]["surface"], store_dict["powerup"]["invincibility"]["combined"]["rect"].topleft)
        scroll_surface.blit(store_dict["powerup"]["de_spawner"]["combined"]["surface"], store_dict["powerup"]["de_spawner"]["combined"]["rect"].topleft)
        scroll_surface.blit(store_dict["powerup"]["double_jump"]["combined"]["surface"], store_dict["powerup"]["double_jump"]["combined"]["rect"].topleft)
        scroll_surface.blit(store_dict["powerup"]["double_coins"]["combined"]["surface"], store_dict["powerup"]["double_coins"]["combined"]["rect"].topleft)


        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            scroll_y = max(scroll_y - scroll_speed, 0)  # Prevent scrolling above content
        if keys[pygame.K_DOWN]:
            scroll_y = min(scroll_y + scroll_speed,scrollable_shop_height - 720)  # Prevent scrolling below content





        #screen.fill(deep_black)
        screen.blit(background_image_shop, (0,0))
        screen.blit(scroll_surface, (0, -scroll_y))

        pygame.display.flip()

    pygame.quit
    sys.exit()