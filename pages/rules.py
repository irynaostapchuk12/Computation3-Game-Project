import pygame.image
from pygame import mouse
from config import *
import sys

def rules():
    screen = pygame.display.set_mode(screen_resolution)
    background = pygame.image.load("images/backgrounds/back_of_credits.jpg")

    back_text = corbelfont().render("back", True, white)
    back_rect = back_text.get_rect(center=(360,360))

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

    botao_atras_rect = botao_atras.get_rect(center=(278 + 200 // 2, 540 + 60 // 2))
    back_rect = back_text.get_rect(center=(355, 487))



    rule_index = 0


    while True:



        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            mouse = pygame.mouse.get_pos()

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

        screen.blit(background, (0, 0))
        screen.blit(rule_images[rule_index], (0, 0))
        screen.blit(back_text, back_rect)

        pygame.display.update()