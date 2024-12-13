import pygame
import sys
from config import *

# Brightness control variables
brightness_level = 255  # 0 is darkest, 255 is brightest
brightness_step = 15  # Increment/decrement step

# Music control variables
pygame.mixer.init()
pygame.mixer.music.load("background_music.mp3")  # Replace with your music file path
pygame.mixer.music.play(-1)  # Loop the music indefinitely
music_volume = 0.5  # Initial volume
pygame.mixer.music.set_volume(music_volume)


# Clock for controlling frame rate
clock = pygame.time.Clock()

# Main loop
while True:

    # ATENCION !!!
    # MUDAR DEPOIS PARA CARREGAR EM BOTOES NO ECRA EM VEZ DE TECLAS NO TECLADO PARA CONTROLAR O BRILHO E A MUSICA

    # Check for key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        brightness_level = min(brightness_level + brightness_step, 255)
    if keys[pygame.K_DOWN]:
        brightness_level = max(brightness_level - brightness_step, 0)


    if keys[pygame.K_m]:
        # if the music is playing ( get_busy() checks if the music is playing)
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()  # Turn off the music
        else:
            pygame.mixer.music.play(-1)  # Turn on the music
    if keys[pygame.K_PLUS] or keys[pygame.K_KP_PLUS]:
        music_volume = min(music_volume + 0.1, 1.0)
        pygame.mixer.music.set_volume(music_volume)
    if keys[pygame.K_MINUS] or keys[pygame.K_KP_MINUS]:
        music_volume = max(music_volume - 0.1, 0.0)
        pygame.mixer.music.set_volume(music_volume)

    # Apply brightness overlay
    overlay = pygame.Surface((width, height))
    overlay.fill(deep_black)
    overlay.set_alpha(255 - brightness_level)  # Adjust transparency based on brightness
    resolution.blit(overlay, (0, 0))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)
