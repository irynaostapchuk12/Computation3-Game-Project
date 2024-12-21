import pygame
import random
from config import*

clock = pygame.time.Clock()


def chest():
    screen = pygame.display.set_mode(screen_resolution)

    background = pygame.image.load("images/menus/menus_back.png")
    background = pygame.transform.scale(background, screen_resolution)

    chest = pygame.image.load("images/icons/chest.png")
    chest_rect = chest.get_rect(center = (360, 360))

    card_back = pygame.image.load("images/icons/card.png").convert_alpha()

    card_options = ["images/icons/card_1.png", "images/icons/card_2.png", "images/icons/card_3.png" ]

    card_positions = [(150, 400), (360, 400), (570, 400)]
    card_rects = [card_back.get_rect(center=pos) for pos in card_positions]

    text1 = verdana_settings.render("Click to open the chest!", True, deep_black)
    text1_rect = text1.get_rect(center = (360, 600))

    text2 = verdana_settings.render("Click on a chosen card to reveal it!", True, deep_black)
    text2_rect = text2.get_rect(center = (360, 600))

    chest_opened = False
    card_faces = []
    revealed_card_index = None
    card_revealed = False

    running = True

    while running:
        screen.blit(background, (0, 0))


        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not chest_opened and chest_rect.collidepoint(event.pos):
                    # Open chest, generate random card outcomes
                    chest_opened = True
                    card_faces = random.sample(card_options, 3)
                elif chest_opened and not card_revealed:
                    # Check which card was clicked
                    for i, rect in enumerate(card_rects):
                        if rect.collidepoint(event.pos):
                            revealed_card_index = i
                            card_revealed = True

        # Draw the chest or cards
        if not chest_opened:
            screen.blit(chest, chest_rect)
            screen.blit(text1, text1_rect)
        else:
            for i, rect in enumerate(card_rects):
                if revealed_card_index is not None and i == revealed_card_index:
                    # Show the face of the selected card
                    card_face = pygame.image.load(card_faces[i]).convert_alpha()
                    screen.blit(card_face, rect)
                else:
                    # Show card back
                    screen.blit(card_back, rect)

            if revealed_card_index is None:
                screen.blit(text2, text2_rect)

        pygame.display.flip()
        clock.tick(fps)



