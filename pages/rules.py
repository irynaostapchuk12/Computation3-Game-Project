import pygame.image
from pygame import mouse
from config import *
import sys

def rules():
    screen = pygame.display.set_mode(screen_resolution)
    background = pygame.image.load("backgroundgame_level/menus_back.png")
    final_background = pygame.transform.scale(background, screen_resolution)
    back_text = corbelfont().render("back", True, white)

    rule_images = [
        pygame.image.load('images/menus/rule_1.png'),
        pygame.image.load('images/menus/rule_2.png'),
        pygame.image.load('images/menus/rule_3.png'),
    ]
    rule_images[0] = pygame.transform.scale(rule_images[0], rule_board_size)
    rule_images[1] = pygame.transform.scale(rule_images[1], rule_board_size)
    rule_images[2] = pygame.transform.scale(rule_images[2], rule_board_size)


    botao_atras = pygame.image.load("backgroundgame_level/botao_atras_das_palavras.png")
    back_text = custom_font.render("BACK", True , deep_black)

    botao_atras_rect = botao_atras.get_rect(center=(375, 750))
    back_rect = back_text.get_rect(center=(350, 665))


#239, 300
#355, 487
    rule_index = 0


    while True:

        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()


            # rules button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(ev.pos):
                    return "interface"

            if back_rect.collidepoint(mouse):
                back_text = poppins.render("BACK", True, green)
            else:
                back_text = poppins.render("BACK", True, deep_black)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and rule_index > 0:
                rule_index -= 1

            if keys[pygame.K_RIGHT] and rule_index < len(rule_images) - 1:
                rule_index += 1

        screen.blit(final_background, (0, 0))
        screen.blit(rule_images[rule_index], (0, 0))
        screen.blit(botao_atras, botao_atras_rect)
        screen.blit(back_text, back_rect)


        pygame.display.update()