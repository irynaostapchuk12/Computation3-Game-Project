import sys
import pygame.image
from pygame import mouse
from game import game_loop
from utils import *  # no need to import pygame because the import is in utils
from config import *  # importing colors and the like
from utils import under_construction


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

    # setting the fonts
    poppins = pygame.font.Font("leters/Cocogoose-Classic-Medium-trial.ttf")
    font_size = 45
    custom_font_intro = pygame.font.SysFont("poppins", font_size)

    # poppins = pygame.font.SysFont("letere", 40)
    verdana = pygame.font.SysFont("Verdana", 55)

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
                    game_loop()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if store_rect.collidepoint(ev.pos):
                    under_construction()

            # settings button - click
            # if ev.type == pygame.MOUSEBUTTONDOWN:
            #   if start_rect.collidepoint(ev.pos):
            #      under_construction()

            # rules button - click
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if rules_rect.collidepoint(ev.pos):
                    under_construction()

            # credits button - click
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if credits_rect.collidepoint(ev.pos):
                    credits_()

            # quit button - click
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if quit_rect.collidepoint(ev.pos):
                    pygame.quit()

            # settings image - click
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if settings_rect.collidepoint(ev.pos):
                    settings_()

            # if the user has the mouse over the word-changes color
            # for quit
            if quit_rect.collidepoint(mouse):
                quit_text = custom_font_intro.render("QUIT", True, dry_green)
            else:
                quit_text = custom_font_intro.render("QUIT", True, deep_black)

            # for rules
            if rules_rect.collidepoint(mouse):
                rules_text = custom_font_intro.render("RULES", True, dry_green)
            else:
                rules_text = custom_font_intro.render("RULES", True, deep_black)

            # for settings
            if start_rect.collidepoint(mouse):
                start_text = custom_font_intro.render("START", True, dry_green)
            else:
                start_text = custom_font_intro.render("START", True, deep_black)

            # for credits
            if credits_rect.collidepoint(mouse):
                credits_text = custom_font_intro.render("CREDITS", True, dry_green)
            else:
                credits_text = custom_font_intro.render("CREDITS", True, deep_black)

            # for store
            if store_rect.collidepoint(mouse):
                store_text = custom_font_intro.render("STORE", True, dry_green)
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
    x = (width - resolution_credits[0]) // 2
    y = (height - resolution_credits[1]) // 2

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
                back_text = poppins.render("BACK", True, dry_green)
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


def settings_():
    pygame.init()  # calling pygame

    # definições da tela
    screen = pygame.display.set_mode(screen_resolution)  # show the user something
    pygame.display.set_caption("Jungle Rex")
    clock = pygame.time.Clock()

    # letra
    poppins = pygame.font.SysFont("Poppins-Regular.ttf", 35)

    # text "back"
    back_text = poppins.render("BACK", True, deep_black)
    back_of_credits = pygame.image.load("backgroundgame_level/menus_back.png")
    botao_atras = pygame.image.load("backgroundgame_level/botao_atras_das_palavras.png")
    back_of_credits_ = pygame.transform.scale(back_of_credits, screen_resolution)

    # retângulo para o butão
    back_rect = back_text.get_rect(center=(349,440))
    botao_atras_rect = botao_atras.get_rect(center=(266 + 200 // 2, 493 + 60 // 2))


    # main interface loop (will run until the user quits)
    while True:
        # filling the screen
        screen.fill(deep_black)

        # getting the mouse position (future need)
        mouse = pygame.mouse.get_pos()

        # event detection (future work)
        for ev in pygame.event.get():
            # seeing if the user hits the red x button
            if ev.type == pygame.QUIT:
                pygame.quit()
                return

            # clicar no "back"
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(ev.pos):
                    return # se clicar volta à página do menu principal
                # Mudar a cor do botão quando o rato está por cima

            if back_rect.collidepoint(mouse):
                back_text = poppins.render("BACK", True, dry_green)

            else:
                back_text = poppins.render("BACK", True, deep_black)



        #inserir fundo
        screen.blit(back_of_credits_, (0, 0))
        # desenhar o botão back
        screen.blit(botao_atras,botao_atras_rect)
        screen.blit(back_text, back_rect)

        # update the display so that the loop changes will appear
        pygame.display.update()
        # Controlar os FPS
        clock.tick(fps)


def wilderness_explorer():
    under_construction()

##    pygame.init()  # calling pygame

# screen = pygame.display.set_mode(resolution)  # show the user something

# clock = pygame.time.Clock()
# while True:

# getting the mouse position (future need)
#   mouse = pygame.mouse.get_pos()
#  for ev in pygame.event.get():
#     if ev.type == pygame.MOUSEBUTTONDOWN:
# 3           game_loop()
#
##               # update the display so that the loop changes will appear
#         pygame.display.update()
#        # Controlar os FPS
#       clock.tick(fps)


##########################MENU DENTRO DO JOGO#########################################
#menu = pygame.image.load("backgroundgame_level/menu_inside_game.png")
 #   menu_esta = pygame.transform.scale(menu,(530,420))
#menu_rect = menu_esta.get_rect(center=(360, 360))

#screen.blit(menu_esta, menu_rect)

