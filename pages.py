import sys
import pygame
import pygame.image
from pygame import mouse
from game import *
from config import *  # importing colors and the like


def interface():
    pygame.init()  # calling pygame

    # creating the screen at the set resolution
    screen = pygame.display.set_mode(screen_resolution)  # show the user something

    # Carregar a imagem e redimensionar
    imagem_inicial = pygame.image.load("backgroundgame_level/principal_page_menu_segundatentativa.png")
    imagem_inicial = pygame.transform.scale(imagem_inicial, screen_resolution)
    settings = pygame.image.load("backgroundgame_level/settings_button.png")
    # load image for background levels
    # image_level_one  = pygame.image.load("backgroundgame_level/background_of_level1.png").convert()

    # Configurar a tela
    pygame.display.set_caption("Jungle Rex")

    # Configurar o relógio para controlar os FPS
    clock = pygame.time.Clock()



    # render the text (will be used in the game button)
    game_name_text = verdana.render("JungleRex", True, deep_black)
    start_text = custom_font_intro.render("START", True, deep_black)
    store_text = custom_font_intro.render("STORE", True, deep_black)
    rules_text = custom_font_intro.render("RULES", True, deep_black)
    credits_text = custom_font_intro.render("CREDITS", True, deep_black)
    quit_text = custom_font_intro.render("QUIT", True, deep_black)

    # Configurar as posições dos retângulos dos botões

    game_name_rect = game_name_text.get_rect(center=(90 + 540 // 2, 123 + 60 // 2))  # text centered in the button
    start_rect = start_text.get_rect(center=(266 + 200 // 2, 280 + 60 // 2))  # text centered in the button
    store_rect = store_text.get_rect(center=(266 + 200 // 2, 350 + 60 // 2))
    rules_rect = rules_text.get_rect(center=(266 + 200 // 2, 420 + 60 // 2))  # text centered in the button
    credits_rect = credits_text.get_rect(center=(266 + 200 // 2, 493 + 60 // 2))  # text centered in the button
    quit_rect = quit_text.get_rect(center=(266 + 200 // 2, 565 + 60 // 2))  # text centered in the button
    settings_rect = settings.get_rect(topleft=(30, 50))  # position ajusted

    # main interface loop (will run until the user quits)
    while True:

        # getting the mouse position (future need)
        mouse = pygame.mouse.get_pos()

        # event detection (future work)
        for ev in pygame.event.get():
            # seeing if the user hits the red x button
            if ev.type == pygame.QUIT:
                pygame.quit()

            # JungleRex button - START
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(ev.pos):
                    return "level_1"

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if store_rect.collidepoint(ev.pos):
                    return "store"


            # settings button - click
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(ev.pos):
                    return "level_1"

            # rules button - click
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if rules_rect.collidepoint(ev.pos):
                    return "rules"
            # credits button - click
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if credits_rect.collidepoint(ev.pos):
                    return "credits"

            # quit button - click
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if quit_rect.collidepoint(ev.pos):
                    pygame.quit()

            # settings image - click
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if settings_rect.collidepoint(ev.pos):
                    return settings_function()



            # if the user has the mouse over the word-changes color
            # for quit
            if quit_rect.collidepoint(mouse):
                quit_text = custom_font_intro.render("QUIT", True, green)
            else:
                quit_text = custom_font_intro.render("QUIT", True, deep_black)

            # for rules
            if rules_rect.collidepoint(mouse):
                rules_text = custom_font_intro.render("RULES", True, green)
            else:
                rules_text = custom_font_intro.render("RULES", True, deep_black)

            # for settings
            if start_rect.collidepoint(mouse):
                start_text = custom_font_intro.render("START", True, green)
            else:
                start_text = custom_font_intro.render("START", True, deep_black)

            # for credits
            if credits_rect.collidepoint(mouse):
                credits_text = custom_font_intro.render("CREDITS", True, green)
            else:
                credits_text = custom_font_intro.render("CREDITS", True, deep_black)

            # for store
            if store_rect.collidepoint(mouse):
                store_text = custom_font_intro.render("STORE", True, green)
            else:
                store_text = custom_font_intro.render("STORE", True, deep_black)

        # filling the screen
        screen.fill(deep_black)

        # Desenhar a imagem "placa"
        # screen.blit(back_of_credits, (x, y))
        screen.blit(imagem_inicial, (0, 0))

        # showing the title of the project
        screen.blit(game_name_text, game_name_rect)

        # showing settings image
        screen.blit(settings, (30, 50))

        # rules button
        screen.blit(rules_text, rules_rect)

        # options button
        # pygame.draw.rect(screen, grey, [250, 400, 200, 60])
        screen.blit(start_text, start_rect)

        # quit button
        # pygame.draw.rect(screen, grey, [250, 480, 200, 60])
        screen.blit(quit_text, quit_rect)

        # credits button
        # pygame.draw.rect(screen, grey, [250, 560, 200, 60])
        screen.blit(credits_text, credits_rect)

        # store button
        # pygame.draw.rect(screen, grey, [250, 640, 200, 60])
        screen.blit(store_text, store_rect)

        # update the display so that the loop changes will appear
        pygame.display.update()
        # Controlar os FPS
        clock.tick(fps)
















# Under construction screen
def credits_():
    # setting up the background and the screen
    back_of_credits = pygame.image.load("backgroundgame_level/menus_back.png")
    background_credits = pygame.image.load("backgroundgame_level/credits_on_back.png")
    botao_atras = pygame.image.load("backgroundgame_level/botao_atras_das_palavras.png")

    # scaling the background image into our selected resolution
    back_of_credits = pygame.transform.scale(back_of_credits, resolution_back_jungle)
    background_credits = pygame.transform.scale(background_credits, resolution_credits)

    # setting up the screen
    credit_screen = pygame.display.set_mode(resolution_credits)

    # setting up the clock for fps
    clock = pygame.time.Clock()

    # basic settings #

    screen = pygame.display.set_mode(screen_resolution)

    # creating the fonts:
    custom_font = "leters/Cocogoose-Classic-Medium-trial.ttf"
    font_size = 30
    custom_font = pygame.font.SysFont(custom_font, font_size)
    poppins = pygame.font.SysFont("Poppins-Regular.ttf", 35)
    # verdana = pygame.font.SysFont("Verdana", 40)

    # creating the rendered texts for the credits
    produced_by = poppins.render("Produced by:", True, dark_red)
    rita_text = custom_font.render("Rita Graça", True, deep_black)
    iryna_text = custom_font.render("Iryna Ostapchuk", True, deep_black)
    neves_text = custom_font.render("Rodrigo Neves", True, deep_black)
    ines_text = custom_font.render("Inês Palma", True, deep_black)
    professors_text = poppins.render("Professors:", True, dark_red)
    augusto_text = custom_font.render("Augusto Santos", True, deep_black)
    diogo_text = custom_font.render("Diogo Rasteiro", True, deep_black)
    liah_text = custom_font.render("Liah Rosenfeld", True, deep_black)
    back_text = custom_font.render("BACK", True , deep_black)

    # Calcular as dimensões da imagem
    background_width = background_credits.get_width()
    background_height = background_credits.get_height()

    # Calcular as coordenadas para centralizar
    x = (screen_width - resolution_credits[0]) // 2
    y = (screen_height - resolution_credits[1]) // 2

    # Margem superior dentro da imagem
    margin_top = 100
    line_spacing = 30  # Espaço entre linhas
    line_spacing_prof = 45

    # Calcular as posições horizontais e verticais do texto
    produced_by_x = x + (600 - produced_by.get_width()) // 2
    produced_by_y = y + margin_top

    ines_x = x + (600 - ines_text.get_width()) // 2
    ines_y = produced_by_y + line_spacing

    iryna_x = x + (600 - iryna_text.get_width()) // 2
    iryna_y = ines_y + line_spacing

    rita_x = x + (600 - rita_text.get_width()) // 2
    rita_y = iryna_y + line_spacing

    neves_x = x + (600 - neves_text.get_width()) // 2
    neves_y = rita_y + line_spacing

    professors_x = x + (600 - professors_text.get_width()) // 2
    professors_y = neves_y + line_spacing_prof

    augusto_x = x + (600 - augusto_text.get_width()) // 2
    augusto_y = professors_y + line_spacing

    diogo_x = x + (600 - diogo_text.get_width()) // 2
    diogo_y = augusto_y + line_spacing

    liah_x = x + (600 - liah_text.get_width()) // 2
    liah_y = diogo_y + line_spacing

    botao_atras_rect = botao_atras.get_rect(center=(278 + 200 // 2,540 + 60 // 2))

    back_rect = back_text.get_rect(center=(355,487))


    while True:

        mouse = pygame.mouse.get_pos()

        # Detectar eventos
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(ev.pos):
                    interface()
            if back_rect.collidepoint(mouse):
                back_text = poppins.render("BACK", True, green)
            else:
                back_text = poppins.render("BACK", True, deep_black)

        # Preencher a tela com a imagem de fundo primeiro
        screen.blit(back_of_credits, (0, 0))
        screen.blit(background_credits, (x, y))
        screen.blit(botao_atras, botao_atras_rect)

        # Desenhar o texto centralizado
        screen.blit(produced_by, (produced_by_x, produced_by_y))
        screen.blit(ines_text, (ines_x, ines_y))
        screen.blit(iryna_text, (iryna_x, iryna_y))
        screen.blit(rita_text, (rita_x, rita_y))
        screen.blit(neves_text, (neves_x, neves_y))
        screen.blit(professors_text, (professors_x, professors_y))
        screen.blit(augusto_text, (augusto_x, augusto_y))
        screen.blit(diogo_text, (diogo_x, diogo_y))
        screen.blit(liah_text, (liah_x, liah_y))
        screen.blit(back_text, back_rect)




        # Atualizar o display
        pygame.display.update()
        clock.tick(fps)


##
def rules():
    print("???")



def settings_function():
    screen = pygame.display.set_mode(screen_resolution)

    # BACKGROUND
    background = pygame.image.load("backgroundgame_level/menus_back.png")
    background = pygame.transform.scale(background, screen_resolution)

    settings_menu = pygame.image.load("images/menus/settings_menu.png").convert_alpha()
    settings_menu_rect = settings_menu.get_rect(center= (360, 360))

    # BACK BUTTON
    back_board = pygame.image.load("images/menus/wooden_board_2.png").convert_alpha()
    back_board_rect = back_board.get_rect(center = (360, 550))

    back_text = verdana_settings.render("Back", True, deep_black)

    # BRIGHTNESS
    brightness_text = verdana_settings.render("Brightness", True, deep_black)
    brightness_text_rect = brightness_text.get_rect(center = (360, 242))

    add_br_button = pygame.image.load("images/menus/add_button.png").convert_alpha()
    add_br_button_rect = add_br_button.get_rect(center = (535, 315))

    subtract_br_button = pygame.image.load("images/menus/subtract_button.png").convert_alpha()
    subtract_br_button_rect = subtract_br_button.get_rect(center=(185, 315))

    # VOLUME
    volume_text = verdana_settings.render("Volume", True, deep_black)
    volume_text_rect = volume_text.get_rect(center=(360, 395))

    add_vol_button = pygame.image.load("images/menus/add_button.png").convert_alpha()
    add_vol_button_rect = add_vol_button.get_rect(center=(535, 470))

    subtract_vol_button = pygame.image.load("images/menus/subtract_button.png").convert_alpha()
    subtract_vol_button_rect = subtract_vol_button.get_rect(center=(185, 470))

    br_level_images = [
        pygame.image.load(f"images/menus/brightness_level_{i}.png").convert_alpha() for i in range(1, 6)]

    vol_level_images = [
        pygame.image.load(f"images/menus/brightness_level_{i}.png").convert_alpha() for i in range(0, 6)]

    # Brightness control variables
    brightness_level = 255  # 0 is darkest, 255 is brightest
    brightness_step = 51
    min_brightness = 51

    # Music control variables
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/Ian Post - Super Duper.mp3")  # Replace with your music file path
    pygame.mixer.music.play(-1)  # Loop the music indefinitely
    music_volume = 2  # Initial volume
    pygame.mixer.music.set_volume(music_volume)
    volume_step = 1
    min_vol = 0
    max_vol = 5


    clock = pygame.time.Clock()


    # Main loop
    while True:
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                #BRIGHTNESS
                if add_br_button_rect.collidepoint(ev.pos):
                    brightness_level = min(brightness_level + brightness_step, 255)
                if subtract_br_button_rect.collidepoint(ev.pos):
                    brightness_level = max(brightness_level - brightness_step, min_brightness)

                # VOLUME
                if add_vol_button_rect.collidepoint(ev.pos):
                    music_volume = min(music_volume + volume_step, max_vol)
                    pygame.mixer.music.set_volume(music_volume)
                if subtract_vol_button_rect.collidepoint(ev.pos):
                    music_volume = max(music_volume - volume_step, min_vol)
                    pygame.mixer.music.set_volume(music_volume)  # Normalize for Pygame

                # BACK
                if back_board_rect.collidepoint(ev.pos):
                    interface()

        # BRIGHTNESS level bar
        br_level_index = (brightness_level - min_brightness) // brightness_step
        br_level_image = br_level_images[br_level_index]
        br_level_image_rect = br_level_image.get_rect(center = (360, 315))

        # VOLUME level bar
        vol_level_index = (music_volume - min_vol) // volume_step
        vol_level_image = vol_level_images[vol_level_index]
        vol_level_image_rect = vol_level_image.get_rect(center=(360, 470))

        screen.blit(background, (0, 0))
        screen.blit(settings_menu, settings_menu_rect)

        # BRIGHTNESS
        screen.blit(brightness_text, brightness_text_rect)
        screen.blit(add_br_button, add_br_button_rect)
        screen.blit(subtract_br_button, subtract_br_button_rect)

        # VOLUME
        screen.blit(volume_text, volume_text_rect)
        screen.blit(add_vol_button, add_vol_button_rect)
        screen.blit(subtract_vol_button, subtract_vol_button_rect)

        # BACK
        screen.blit(back_text, back_board_rect)

        # Draw level bar image
        screen.blit(br_level_image, br_level_image_rect)
        screen.blit(vol_level_image, vol_level_image_rect)

        # Apply brightness overlay
        overlay = pygame.Surface(screen.get_size())
        overlay.fill(deep_black)
        overlay.set_alpha(255 - brightness_level)  # Adjust transparency based on brightness
        screen.blit(overlay, (0, 0))


        pygame.display.flip()


        clock.tick(fps)












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
    combined_surface = pygame.Surface((combined_width + 50, combined_height + 50), pygame.SRCALPHA)


    wood_board = pygame.image.load(f"images/menus/wood_board.png").convert_alpha()
    wood_board = pygame.transform.scale(wood_board,(combined_width + 40, combined_height + 60))

    combined_surface.blit(wood_board, (0, 0))
    combined_surface.blit(text, (30, 40))
    combined_surface.blit(image, (30, text_height + 10 + 40))
    combined_surface.blit(tag, (30, text_height + image_height + 10 + 10 + 40))
    combined_surface.blit(coin, (tag_width + 10 + 30, text_height + image_height + 10 + 10 + 40))
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



    background_image_shop = pygame.image.load(f"images/backgrounds/back_of_credits.jpg").convert_alpha()
    background_image_shop = pygame.transform.scale(background_image_shop, screen_resolution)




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