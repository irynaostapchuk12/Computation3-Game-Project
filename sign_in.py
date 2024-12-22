import pygame
import sys
from config import *

class SignIn:
    def __init__(self):

        self.screen = pygame.display.set_mode(screen_resolution)

        self.background = pygame.image.load("backgroundgame_level/menus_back.png")
        self.background = pygame.transform.scale(self.background, screen_resolution)



        self.title_text = verdana_settings.render("Sign In", True, deep_black)
        self.title_text_rect = self.title_text.get_rect(center=(360, 150))

        self.username_board = pygame.image.load("images/menus/wooden_board_big.png").convert_alpha()
        self.username_board_rect = self.username_board.get_rect(center=(360, 300))

        # We will store the user’s typed text here
        self.username_input = ""

        self.username_text_surface = verdana_settings.render(self.username_input, True, deep_black)
        self.username_text_rect = self.username_text_surface.get_rect(center=(360, 300))

        # SIGN IN button
        self.signin_button = pygame.image.load("images/menus/wooden_board_3.png").convert_alpha()
        self.signin_button_rect = self.signin_button.get_rect(center=(360, 420))

        self.signin_text = verdana_settings.render("Confirm", True, deep_black)
        self.signin_text_rect = self.signin_text.get_rect(center=(360, 418))

        # BACK button
        self.back_board = pygame.image.load("images/menus/wooden_board_4.png").convert_alpha()
        self.back_board_rect = self.back_board.get_rect(center=(360, 540))

        self.back_text = verdana_settings.render("Back", True, deep_black)
        self.back_text_rect = self.back_text.get_rect(center=(360, 538))

        self.clock = pygame.time.Clock()

    def run(self):
        mouse = pygame.mouse.get_pos()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(f"New user created: {self.username_input}")
                    return "login"

                if self.back_board_rect.collidepoint(mouse):
                    return "login"

            # Update the displayed text
            self.username_text_surface = verdana_settings.render(self.username_input, True, deep_black)
            # Keep the text rect centered on the same position
            self.username_text_rect = self.username_text_surface.get_rect(center=self.username_board_rect.center)

            # Drawing
            self.screen.blit(self.background, (0, 0))

            # Title
            self.screen.blit(self.title_text, self.title_text_rect)

            # “Enter username” label
            # Wooden board + typed text
            self.screen.blit(self.username_board, self.username_board_rect)
            self.screen.blit(self.username_text_surface, self.username_text_rect)

            # SIGN IN button
            self.screen.blit(self.signin_text, self.signin_text_rect)

            # BACK button
            self.screen.blit(self.back_board, self.back_board_rect)
            self.screen.blit(self.back_text, self.back_text_rect)

            pygame.display.flip()
            self.clock.tick(fps)

signin = SignIn()
signin.run()
