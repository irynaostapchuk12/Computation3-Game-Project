import math

from enemy import Enemy
from config import *
import pygame
from player import Player
from shed import shed
import math


def game_loop():
    # creating the player for the game - only done once :)
    player = Player()

    # by default I start the game in the main area
    current_state = "main"

    # "endeless" game loop:
    while True:
        if current_state == "main":
            current_state = execute_game(player)
        elif current_state == "shed":
            current_state = shed(player)


def execute_game(player):
    # SETUP:

    # setting up the background:
    bigimage = pygame.image.load("backgroundgame_level/background_of_level1.png").convert()
    bigimagewidth = bigimage.get_width()
    bigimage__ = pygame.transform.scale(bigimage, (bigimagewidth, 750))
    bigimageheight = bigimage.get_height()

    # background = pygame.transform.scale(image_level_one, (width, height))

    # using the clock to control the time frame.
    clock = pygame.time.Clock()

    # screen setup:
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Jungle Rex")

    # creating an empty group for the player (that we received as input)
    # player_group = pygame.sprite.Group()

    # adding the player to the group
    # player_group.add(player)

    # creating an empty bullet group that will be given as input to the player.shoot() method
    # bullets = pygame.sprite.Group()

    # creating the enemy group
    # enemies = pygame.sprite.Group()

    # before starting our main loop, setup the enemy cooldown variable
    # enemy_cooldown = 0

    # MAIN GAME LOOP
    running = True

    # Configurações do scroll
    scroll_speed = 1  # Velocidade do scroll
    offset_x = 0  # Deslocamento horizontal
    cycles_completed = 0
    max_cycles = 2
    while running:

        # controlling the frame rate
        clock.tick(fps)

        # handling events:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Atualizar o deslocamento horizontal apenas se nao atingir o nr máximo de ciclos
        if cycles_completed < max_cycles:
            offset_x -= scroll_speed  # Mover para a esquerda

            # Fim ao scroll quando a imagem sair totalmente do ecrã
            if offset_x <= -bigimagewidth:  # -bigimagewidht -> saiu completamente da janela visível
                offset_x = 0  # logo reinicia o deslocamento horizontal para que a imagem volte ao início
                cycles_completed += 1 # acabou um ciclo




        # Desenhar a imagem principal
        screen.blit(bigimage, (offset_x, -124))  # Primeira posição da imagem

        # Desenhar uma segunda cópia da imagem para o loop contínuo
        if offset_x + bigimageheight < 720:
            screen.blit(bigimage, (offset_x + bigimagewidth, 0))

        pygame.display.flip()

    # the main while game loop has terminated and the game ends
    pygame.quit()
