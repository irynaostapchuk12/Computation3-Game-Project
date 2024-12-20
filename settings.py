import pygame
import sys
from config import *



def settings_function():
    screen = pygame.display.set_mode(screen_resolution)

    # BACKGROUND
    background = pygame.image.load("backgroundgame_level/menus_back.png")
    background = pygame.transform.scale(background, screen_resolution)

    settings_menu = pygame.image.load("images/menus/settings_menu.png").convert_alpha()
    settings_menu_rect = settings_menu.get_rect(center= (360, 360))

    # BACK BUTTON
    back_board = pygame.image.load("images/menus/wooden_board_2.png").convert_alpha()
    back_board_rect = back_board.get_rect(center = (360, 550))

    back_text = verdana_settings.render("Back", True, deep_black)

    # BRIGHTNESS
    brightness_text = verdana_settings.render("Brightness", True, deep_black)
    brightness_text_rect = brightness_text.get_rect(center = (360, 242))

    add_br_button = pygame.image.load("images/menus/add_button.png").convert_alpha()
    add_br_button_rect = add_br_button.get_rect(center = (535, 315))

    subtract_br_button = pygame.image.load("images/menus/subtract_button.png").convert_alpha()
    subtract_br_button_rect = subtract_br_button.get_rect(center=(185, 315))

    # VOLUME
    volume_text = verdana_settings.render("Volume", True, deep_black)
    volume_text_rect = volume_text.get_rect(center=(360, 395))

    add_vol_button = pygame.image.load("images/menus/add_button.png").convert_alpha()
    add_vol_button_rect = add_vol_button.get_rect(center=(535, 470))

    subtract_vol_button = pygame.image.load("images/menus/subtract_button.png").convert_alpha()
    subtract_vol_button_rect = subtract_vol_button.get_rect(center=(185, 470))

    br_level_images = [
        pygame.image.load(f"images/menus/brightness_level_{i}.png").convert_alpha() for i in range(1, 6)]

    vol_level_images = [
        pygame.image.load(f"images/menus/brightness_level_{i}.png").convert_alpha() for i in range(0, 6)]

    # Brightness control variables
    brightness_level = 255  # 0 is darkest, 255 is brightest
    brightness_step = 51
    min_brightness = 51

    # Music control variables
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/Ian Post - Super Duper.mp3")  # Replace with your music file path
    pygame.mixer.music.play(-1)  # Loop the music indefinitely
    music_volume = 2  # Initial volume
    pygame.mixer.music.set_volume(music_volume)
    volume_step = 1
    min_vol = 0
    max_vol = 5


    clock = pygame.time.Clock()


    # Main loop
    while True:
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                #BRIGHTNESS
                if add_br_button_rect.collidepoint(ev.pos):
                    brightness_level = min(brightness_level + brightness_step, 255)
                if subtract_br_button_rect.collidepoint(ev.pos):
                    brightness_level = max(brightness_level - brightness_step, min_brightness)

                # VOLUME
                if add_vol_button_rect.collidepoint(ev.pos):
                    music_volume = min(music_volume + volume_step, max_vol)
                    pygame.mixer.music.set_volume(music_volume)
                if subtract_vol_button_rect.collidepoint(ev.pos):
                    music_volume = max(music_volume - volume_step, min_vol)
                    pygame.mixer.music.set_volume(music_volume)  # Normalize for Pygame

                # BACK
                #if back_board_rect.collidepoint(ev.pos):
                    #interface()

        # BRIGHTNESS level bar
        br_level_index = (brightness_level - min_brightness) // brightness_step
        br_level_image = br_level_images[br_level_index]
        br_level_image_rect = br_level_image.get_rect(center = (360, 315))

        # VOLUME level bar
        vol_level_index = (music_volume - min_vol) // volume_step
        vol_level_image = vol_level_images[vol_level_index]
        vol_level_image_rect = vol_level_image.get_rect(center=(360, 470))

        screen.blit(background, (0, 0))
        screen.blit(settings_menu, settings_menu_rect)

        # BRIGHTNESS
        screen.blit(brightness_text, brightness_text_rect)
        screen.blit(add_br_button, add_br_button_rect)
        screen.blit(subtract_br_button, subtract_br_button_rect)

        # VOLUME
        screen.blit(volume_text, volume_text_rect)
        screen.blit(add_vol_button, add_vol_button_rect)
        screen.blit(subtract_vol_button, subtract_vol_button_rect)

        # BACK
        screen.blit(back_text, back_board_rect)

        # Draw level bar image
        screen.blit(br_level_image, br_level_image_rect)
        screen.blit(vol_level_image, vol_level_image_rect)

        # Apply brightness overlay
        overlay = pygame.Surface(screen.get_size())
        overlay.fill(deep_black)
        overlay.set_alpha(255 - brightness_level)  # Adjust transparency based on brightness
        screen.blit(overlay, (0, 0))


        pygame.display.flip()


        clock.tick(fps)
