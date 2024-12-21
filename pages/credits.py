import pygame.image
from pygame import mouse
from game import *
from config import *  # importing colors and the like
from store import store
from settings import Settings



def credits_():
    # setting up the background and the screen
    back_of_credits = pygame.image.load("../backgroundgame_level/menus_back.png")
    background_credits = pygame.image.load("../backgroundgame_level/credits_on_back.png")
    botao_atras = pygame.image.load("../backgroundgame_level/botao_atras_das_palavras.png")

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
