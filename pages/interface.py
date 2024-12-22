import pygame.image
from pygame import mouse
from game import *
from config import *  # importing colors and the like
from .settings import Settings


def interface():
    pygame.init()  # calling pygame

    settings = Settings()

    #settings_instance = settings.Settings()

    # creating the screen at the set resolution
    screen = pygame.display.set_mode(screen_resolution)  # show the user something

    # Carregar a imagem e redimensionar
    imagem_inicial = pygame.image.load("backgroundgame_level/principal_page_menu_segundatentativa.png")
    imagem_inicial = pygame.transform.scale(imagem_inicial, screen_resolution)
    settings_icon = pygame.image.load("backgroundgame_level/settings_button.png")
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
    settings_rect = settings_icon.get_rect(topleft=(30, 50))  # position ajusted

    # main interface loop (will run until the user quits)
    while True:

        # getting the mouse position (future need)
        mouse = pygame.mouse.get_pos()

        # event detection (future work)
        for ev in pygame.event.get():
            # seeing if the user hits the red x button
            if ev.type == pygame.QUIT:
                pygame.quit()

            # quit button - click
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if quit_rect.collidepoint(ev.pos):
                    pygame.quit()


                # JungleRex button - START
                if start_rect.collidepoint(ev.pos):
                    return "level_1"

                if store_rect.collidepoint(ev.pos):
                    return "store"

                # rules button - click
                if rules_rect.collidepoint(ev.pos):
                    return "rules"

                # credits button - click
                if credits_rect.collidepoint(ev.pos):
                    return "credits"

                # settings image - click
                if settings_rect.collidepoint(ev.pos):
                    return "settings"



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
        screen.blit(settings_icon, (30, 50))

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






