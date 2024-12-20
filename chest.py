import pygame
from config import*

pygame.init()
clock = pygame.time.Clock()


def chest():
    screen = pygame.display.set_mode(screen_resolution)

    background = pygame.image.load("backgroundgame_level/menus_back.png")
    background = pygame.transform.scale(background, screen_resolution)

    chest = pygame.image.load("images/icons/chest.png")
    chest_rect = chest.get_rect(center = (360, 360))

    card = pygame.image.load("images/icons/card.png")
    card_rect = card.get_rect(center = (200, 200))

    while True:

        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if chest_rect.collidepoint(ev.pos):
                    screen.blit(card, card_rect)

        screen.blit(background, (0,0))
        screen.blit(chest, chest_rect)

        clock = pygame.time.Clock()
        pygame.display.flip()
        clock.tick(fps)
