import pygame.image
from pygame import mouse
from config import *
import sys

def rules():
    screen = pygame.display.set_mode(screen_resolution)
    background = pygame.image.load("images/backgrounds/back_of_credits.jpg")

    back_text = corbelfont().render("back", True, white)
    back_rect = back_text.get_rect(center=(355,487))

    rule_images = [
        pygame.image.load('images/menus/rule_1.png'),
        pygame.image.load('images/menus/rule_2.png'),
        pygame.image.load('images/menus/rule_3.png'),
    ]
    rule_index = 0

    mouse = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    while True:



        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            # rules button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 90 <= mouse[0] <= 230 and 480 <= mouse[1] <= 540:
                    return "interface"

                if back_rect.collidepoint(mouse):
                    back_text = corbelfont().render("BACK", True, green)
                else:
                    back_text = corbelfont().render("BACK", True, deep_black)

            if keys[pygame.K_LEFT] and rule_index > 0:
                rule_index -= 1

            if keys[pygame.K_RIGHT] and rule_index < len(rule_images) - 1:
                rule_index += 1

        screen.blit(background, (0, 0))
        screen.blit(rule_images[rule_index], (0, 0))
        screen.blit(back_text, back_rect)

        pygame.display.update()