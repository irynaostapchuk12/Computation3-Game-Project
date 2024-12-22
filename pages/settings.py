import pygame
import sys
from config import *
class Settings:
    def __init__(self):
        # Initialize Pygame and create screen
        self.screen = pygame.display.set_mode(screen_resolution)

        # BACKGROUND
        self.background = pygame.image.load("backgroundgame_level/menus_back.png")
        self.background = pygame.transform.scale(self.background, screen_resolution)

        self.settings_menu = pygame.image.load("images/menus/settings_menu.png").convert_alpha()
        self.settings_menu_rect = self.settings_menu.get_rect(center=(360, 360))

        # BACK BUTTON
        self.back_board = pygame.image.load("images/menus/wooden_board_2.png").convert_alpha()
        self.back_board_rect = self.back_board.get_rect(center=(360, 600))

        self.back_text = verdana_settings.render("Back", True, deep_black)
        self.back_text_rect = self.back_text.get_rect(center=(360, 597))

        # BRIGHTNESS
        self.brightness_text = verdana_settings.render("Brightness", True, deep_black)
        self.brightness_text_rect = self.brightness_text.get_rect(center=(360, 242))

        self.add_br_button = pygame.image.load("images/menus/add_button.png").convert_alpha()
        self.add_br_button_rect = self.add_br_button.get_rect(center=(535, 315))

        self.subtract_br_button = pygame.image.load("images/menus/subtract_button.png").convert_alpha()
        self.subtract_br_button_rect = self.subtract_br_button.get_rect(center=(185, 315))

        # VOLUME
        self.volume_text = verdana_settings.render("Volume", True, deep_black)
        self.volume_text_rect = self.volume_text.get_rect(center=(360, 395))

        self.volume_on = pygame.image.load("images/menus/sound_on.png").convert_alpha()
        self.volume_on_rect = self.volume_on.get_rect(center=(460, 470))

        self.volume_off = pygame.image.load("images/menus/remove_sound.png").convert_alpha()
        self.volume_off_rect = self.volume_off.get_rect(center=(260, 470))

        self.br_level_images = [
            pygame.image.load(f"images/menus/brightness_level_{i}.png").convert_alpha() for i in range(1, 6)
        ]

        # Brightness control variables
        self.brightness_level = 255  # 0 is darkest, 255 is brightest
        self.brightness_step = 51
        self.min_brightness = 51



        self.clock = pygame.time.Clock()


    def play(self):
        # Music control variables
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/Ian Post - Super Duper.mp3")  # Replace with your music file path
        pygame.mixer.music.play(-1)  # Loop the music indefinitely
        self.music_volume = 2  # Initial volume
        pygame.mixer.music.set_volume(self.music_volume)
        self.volume_step = 1
        self.min_vol = 0
        self.max_vol = 5

    def run(self):
        while True:
            mouse = pygame.mouse.get_pos()

            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    # BRIGHTNESS
                    if self.add_br_button_rect.collidepoint(ev.pos):
                        self.brightness_level = min(self.brightness_level + self.brightness_step, 255)
                    if self.subtract_br_button_rect.collidepoint(ev.pos):
                        self.brightness_level = max(self.brightness_level - self.brightness_step, self.min_brightness)

                    # VOLUME
                    if self.volume_on_rect.collidepoint(ev.pos):
                        if not pygame.mixer.music.get_busy():  # Check if music is not playing
                            pygame.mixer.music.play(-1)  # Turn on the music and loop it

                    if self.volume_off_rect.collidepoint(ev.pos):
                        if pygame.mixer.music.get_busy():  # Check if music is playing
                            pygame.mixer.music.stop()  # Turn off the music

                     #BACK
                    if self.back_board_rect.collidepoint(ev.pos):
                        return "interface"  # Go back to the main interface

            # BRIGHTNESS level bar
            br_level_index = (self.brightness_level - self.min_brightness) // self.brightness_step
            br_level_image = self.br_level_images[br_level_index]
            br_level_image_rect = br_level_image.get_rect(center=(360, 315))

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.settings_menu, self.settings_menu_rect)

            # BRIGHTNESS
            self.screen.blit(self.brightness_text, self.brightness_text_rect)
            self.screen.blit(self.add_br_button, self.add_br_button_rect)
            self.screen.blit(self.subtract_br_button, self.subtract_br_button_rect)

            # VOLUME
            self.screen.blit(self.volume_text, self.volume_text_rect)
            self.screen.blit(self.volume_on, self.volume_on_rect)
            self.screen.blit(self.volume_off, self.volume_off_rect)

            # BACK
            self.screen.blit(self.back_board, self.back_board_rect)
            self.screen.blit(self.back_text, self.back_text_rect)

            # Draw level bar image
            self.screen.blit(br_level_image, br_level_image_rect)

            # Apply brightness overlay
            overlay = pygame.Surface(self.screen.get_size())
            overlay.fill(deep_black)
            overlay.set_alpha(255 - self.brightness_level)  # Adjust transparency based on brightness
            self.screen.blit(overlay, (0, 0))

            pygame.display.flip()
            self.clock.tick(fps)

