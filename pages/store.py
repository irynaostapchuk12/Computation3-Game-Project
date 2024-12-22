import pygame
from config import *  # importing colors and the like
from items.inventory import *
from .interface import interface
import sys



store_dict = {
    "others": {
                "coin": {"image": None},
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
    "skins": {  "Business Man"

    }
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



    combined_width = max(image_width, text_width, coin_width + tag_width) + 30
    combined_height = image_height + text_height + max(coin_width, tag_width) + 40
    combined_surface = pygame.Surface((combined_width + 90, combined_height + 90), pygame.SRCALPHA)



    wood_board = pygame.image.load(f"images/menus/wood_board.png").convert_alpha()
    wood_board = pygame.transform.scale(wood_board,(combined_width + 40, combined_height + 60))

    # to center the boards
    #wood_board_x = (combined_surface.get_width() - wood_board.get_width()) // 2
    #wood_board_y = (combined_surface.get_height() - wood_board.get_height()) // 2

    combined_surface.blit(wood_board, (25, 0))
    combined_surface.blit(text, (60, 40))
    combined_surface.blit(image, (75, text_height + 10 + 40))
    combined_surface.blit(tag, (60, text_height + image_height + 10 + 10 + 26))
    combined_surface.blit(coin, (tag_width + 10 +55, text_height + image_height + 10 + 38 ))
    combined_rect = combined_surface.get_rect(topleft=combined_position)

    print(combined_height)


    store_dict[type][name]["text"] = text
    store_dict[type][name]["image"] = image
    store_dict[type][name]["tag"] = tag
    store_dict["others"]["coin"]["image"] = coin

    store_dict[type][name]["combined"]["width"] = combined_width
    store_dict[type][name]["combined"]["height"] = combined_height
    store_dict[type][name]["combined"]["surface"] = combined_surface
    store_dict[type][name]["combined"]["position"] = combined_position
    store_dict[type][name]["combined"]["rect"] = combined_rect


def store():


    pygame.display.set_caption("Store")

    scroll_y = 0
    scroll_speed = 1

    screen = pygame.display.set_mode(screen_resolution)

    scroll_surface = pygame.Surface(scrollable_shop_resolution, pygame.SRCALPHA)
    scroll_surface.fill((0, 0, 0, 0))



    #background_image_shop = pygame.image.load(f"images/backgrounds/back_of_credits.jpg").convert_alpha()
    #background_image_shop = pygame.image.load(f"images/menus/menus_back.png").convert_alpha()
    background_image_shop = pygame.image.load(f"images/menus/menus_back.png").convert_alpha()
    background_image_shop = pygame.transform.scale(background_image_shop, screen_resolution)

    balance_board = pygame.image.load("images/menus/wooden_board_3.png").convert_alpha()
    balance_board_rect = balance_board.get_rect(center = (650, 70))

    balance = inventory_dict["others"]["coin"]
    balance_text = verdana_store.render(f"{balance}", True, deep_black)
    balance_text_rect = balance_text.get_rect(center=(630, 70))

    back_board = pygame.image.load("images/menus/wooden_board_4.png").convert_alpha()
    back_board_rect = back_board.get_rect(center=(100, 70))

    back_text = verdana_settings.render("Back", True, deep_black)
    back_text_rect = back_text.get_rect(center=(100, 74))

    store_dict["others"]["chest"]["text"] = verdana_store.render("CHEST", True, white)
    store_dict["elixir"]["health"]["text"] = verdana_store.render("HEALTH ELIXIR", True, white)
    store_dict["elixir"]["speed"]["text"] = verdana_store.render("SPEED ELIXIR", True, white)
    store_dict["powerup"]["invincibility"]["text"] = verdana_store.render("INVINCIBILITY", True, white)
    store_dict["powerup"]["de_spawner"]["text"] = verdana_store.render("DE-SPAWNER", True, white)
    store_dict["powerup"]["double_jump"]["text"] = verdana_store.render("DOUBLE JUMP", True, white)
    store_dict["powerup"]["double_coins"]["text"] = verdana_store.render("DOUBLE COINS", True, white)

    store_dict["others"]["chest"]["tag"] = verdana_store.render(f"{chest_price}", True, white)
    store_dict["elixir"]["health"]["tag"] = verdana_store.render(f"{health_elixir_price}", True, white)
    store_dict["elixir"]["speed"]["tag"] = verdana_store.render(f"{speed_elixir_price}", True, white)
    store_dict["powerup"]["invincibility"]["tag"] = verdana_store.render(f"{invincibility_powerup_price}", True, white)
    store_dict["powerup"]["de_spawner"]["tag"] = verdana_store.render(f"{de_spawner_powerup_price}", True, white)
    store_dict["powerup"]["double_jump"]["tag"] = verdana_store.render(f"{double_jump_powerup_price}", True, white)
    store_dict["powerup"]["double_coins"]["tag"] = verdana_store.render(f"{double_coins_powerup_price}", True, white)
    my_coins_text = verdana_store.render(f"{inventory_dict['others']['coin']}", True, white)

    get_image("others", "coin", "coin.png", coin_shop_image_size)
    get_image("others", "chest", "chest.png", (150, 105))
    get_image("elixir", "health", "heart+1.png", (180, 122))
    get_image("elixir", "speed", "blue_potion.png", (100, 144))
    get_image("powerup", "invincibility", "invincibility.png", (150, 151))
    get_image("powerup", "de_spawner", "yellow_potion.png", (100, 148))
    get_image("powerup", "double_jump", "double_jump.png", (120, 120))
    get_image("powerup", "double_coins", "double_coins.png", (120, 120))

    get_combined("others", "chest")
    get_combined("elixir", "health")
    get_combined("elixir", "speed")
    get_combined("powerup", "invincibility")
    get_combined("powerup", "de_spawner")
    get_combined("powerup", "double_jump")
    get_combined("powerup", "double_coins")

    combined_width = store_dict["others"]["coin"]["image"].get_width() + my_coins_text.get_width() + 10
    combined_height = max(store_dict["others"]["coin"]["image"].get_height(), my_coins_text.get_height()) + 10
    combined_surface = pygame.Surface((combined_width, combined_height), pygame.SRCALPHA)
    combined_surface.blit(my_coins_text, (0, 0))
    combined_surface.blit(store_dict["others"]["coin"]["image"], (my_coins_text.get_width() + 10, 0))
    combined_rect = combined_surface.get_rect(topleft=(0, 0))
    while True:

        # getting the mouse position
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



            if ev.type == pygame.MOUSEBUTTONDOWN:
                if store_dict["elixir"]["health"]["combined"]["rect"].collidepoint(mouse):  # Check if mouse is inside the box
                    purchase_item("elixir", "health", health_elixir_price)
                    print("Box clicked!")

                if store_dict["elixir"]["speed"]["combined"]["rect"].collidepoint(mouse):  # Check if mouse is inside the box
                    purchase_item("elixir", "speed", speed_elixir_price)
                    print("Box clicked!")

                if store_dict["powerup"]["invincibility"]["combined"]["rect"].collidepoint(mouse):  # Check if mouse is inside the box
                    purchase_item("powerup", "invincibility", invincibility_powerup_price)
                    print("Box clicked!")

                if store_dict["powerup"]["de_spawner"]["combined"]["rect"].collidepoint(mouse):  # Check if mouse is inside the box
                    purchase_item("powerup", "de_spawner", de_spawner_powerup_price)
                    print("Box clicked!")

                if store_dict["powerup"]["double_jump"]["combined"]["rect"].collidepoint(mouse):  # Check if mouse is inside the box
                    purchase_item("powerup", "double_jump", double_jump_powerup_price)
                    print("Box clicked!")

                if store_dict["powerup"]["double_coins"]["combined"]["rect"].collidepoint(mouse):  # Check if mouse is inside the box
                    purchase_item("powerup", "double_coins", double_coins_powerup_price)
                    print("Box clicked!")

                if store_dict["others"]["chest"]["combined"]["rect"].collidepoint(mouse):  # Check if mouse is inside the box
                    purchase_item("others", "chest", chest_price)
                    print("Box clicked!")

                if back_board_rect.collidepoint(mouse):
                    return "interface"

            if back_text_rect.collidepoint(mouse):
                back_text = custom_font_intro.render("Back", True, green)
            else:
                back_text = custom_font_intro.render("Back", True, deep_black)

        scroll_surface.blit(back_board, back_board_rect)
        scroll_surface.blit(back_text, back_text_rect)

        scroll_surface.blit(balance_board, balance_board_rect)
        scroll_surface.blit(balance_text, balance_text_rect)

        scroll_surface.blit(store_dict["others"]["coin"]["image"], (645, 61))
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