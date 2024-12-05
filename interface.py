import sys
import pygame.image
from pygame import mouse
# from game import game_loop
from utils import *  # no need to import pygame because the import is in utils
from config import *  # importing colors and the like
from utils import under_construction


def interface():
    pygame.init()  # calling pygame

    # creating the screen at the set resolution
    screen = pygame.display.set_mode(resolution)  # show the user something

    imagem_inicial = pygame.image.load("images/menus/principal_page_menu_segundatentativa.png")

    imagem_inicial = pygame.transform.scale(imagem_inicial, resolution)

    # Configurar a tela
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Interface Project")

    # Configurar o relógio para controlar os FPS
    clock = pygame.time.Clock()

    # setting the fonts
    poppins = "leters/Cocogoose-Classic-Medium-trial.ttf"
    font_size = 45
    custom_font_intro = pygame.font.SysFont("poppins", int(font_size))

    # poppins = pygame.font.SysFont("letere", 40)
    verdana = pygame.font.SysFont("Verdana", 100)

    # render the text (will be used in the game button)
    game_name_text = verdana.render("DinoX", True, deep_black)
    quit_text = custom_font_intro.render("QUIT", True, deep_black)
    rules_text = custom_font_intro.render("RULES", True, deep_black)
    settings_text = custom_font_intro.render("SETTINGS", True, deep_black)
    credits_text = custom_font_intro.render("CREDITS", True, deep_black)
    store_text = custom_font_intro.render("STORE", True, deep_black)
    title_text = custom_font_intro.render("Computation III - Project", True, red)

    # Configurar as posições dos retângulos dos botões
    game_name_rect = game_name_text.get_rect(center=(90 + 540 // 2, 123 + 60 // 2))  # text centered in the button
    rules_rect = rules_text.get_rect(center=(266 + 200 // 2, 280 + 60 // 2))  # text centered in the button
    settings_rect = settings_text.get_rect(center=(266 + 200 // 2, 350 + 60 // 2))  # text centered in the button
    store_rect = store_text.get_rect(center=(266 + 200 // 2, 420 + 60 // 2))
    credits_rect = credits_text.get_rect(center=(266 + 200 // 2, 565 + 60 // 2))  # text centered in the button
    quit_rect = quit_text.get_rect(center=(266 + 200 // 2, 493 + 60 // 2))  # text centered in the button
    title_rect = title_text.get_rect(midtop=(360, 10))

    # main interface loop (will run until the user quits)
    while True:

        # getting the mouse position (future need)
        mouse = pygame.mouse.get_pos()

        # event detection (future work)
        for ev in pygame.event.get():
            # seeing if the user hits the red x button
            if ev.type == pygame.QUIT:
                pygame.quit()

            # quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if quit_rect.collidepoint(ev.pos):
                    pygame.quit()

            # credits button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if credits_rect.collidepoint(ev.pos):
                    credits_()

            # game_name button
            # if ev.type == pygame.MOUSEBUTTONDOWN:
            # if game_name_rect.collidepoint(ev.pos):
            # wilderness_explorer()

            # settings button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if settings_rect.collidepoint(ev.pos):
                    under_construction()

            # rules button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if rules_rect.collidepoint(ev.pos):
                    under_construction()

            # store button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if store_rect.collidepoint(ev.pos):
                    under_construction()



        # filling the screen
        screen.fill(deep_black)

        # Desenhar a imagem "placa"
        # screen.blit(back_of_credits, (x, y))
        screen.blit(imagem_inicial, (0, 0))
        # showing the title of the project
        screen.blit(game_name_text, game_name_rect)

        # Centralizar o nome "DinoX" na imagem "placa"
        # screen.blit(game_name_text, (texto_x, texto_y))

        # rules button
        # pygame.draw.rect(screen, grey, [250, 320, 200, 60])
        screen.blit(rules_text, rules_rect)

        # options button
        # pygame.draw.rect(screen, grey, [250, 400, 200, 60])
        screen.blit(settings_text, settings_rect)

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
    back_of_credits = pygame.image.load("images/menus/menus_back.png")
    background_credits = pygame.image.load("images/backgrounds/credits_on_back.png")

    # scaling the background image into our selected resolution
    back_of_credits = pygame.transform.scale(back_of_credits, resolution_back_jungle)
    background_credits = pygame.transform.scale(background_credits, resolution_credits)

    # setting up the screen
    credit_screen = pygame.display.set_mode(resolution_credits)

    # setting up the clock for fps
    clock = pygame.time.Clock()

    # basic settings #

    screen = pygame.display.set_mode(resolution)

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

    # main loop to detect user input and displaying the credits page

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

    while True:
        # Detectar eventos
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 450 <= mouse[0] <= 590 and 600 <= mouse[1] <= 660:
                    interface()

        # Preencher a tela com a imagem de fundo primeiro
        screen.blit(back_of_credits, (0, 0))

        screen.blit(background_credits, (x, y))
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

        # Dimensões do botão
        button_width = 140
        button_height = 60
        margin_bottom = 50  # Margem inferior para o botão

        # Calcular as coordenadas do botão
        button_x = x + (600 - button_width) // 2
        button_y = y + (
                    600 - button_height - margin_bottom) - 80  # 80 pixels para cima, em python o y cresce de cima para baixo

        # Desenhar o botão
        pygame.draw.rect(screen, dark_red, [button_x, button_y, button_width, button_height])

        # Centralizar o texto "Back" dentro do botão
        back_text = poppins.render("back", True, white)
        back_rect = back_text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        screen.blit(back_text, back_rect)
        # Atualizar o display
        pygame.display.update()
        clock.tick(fps)


def rules():
    print("???")


#def wilderness_explorer():
 #   game_loop()
