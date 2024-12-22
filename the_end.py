import pygame
import random
import math
from characters.avatar import Avatar
from config import *
from pages.settings import Settings

# Configuração inicial da tela
screen = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Jungle Rex")

# Função de transição em formato de quadrado
def square_transition(screen, color=(0, 0, 0), duration=1500):
    screen_width, screen_height = screen.get_size()
    center_x, center_y = screen_width // 2, screen_height // 2

    clock = pygame.time.Clock()
    total_frames = duration // 30
    max_size = max(screen_width, screen_height) * 2
    step = max_size / total_frames

    size = 0

    for _ in range(total_frames):
        rect_x = center_x - size // 2
        rect_y = center_y - size // 2

        pygame.draw.rect(screen, color, (rect_x, rect_y, size, size))

        pygame.display.update()
        clock.tick(60)

        size += step

# Função para criar confetis
def criar_confetis(quantidade, lado="esquerdo"):
    CORES = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

    confetis = []
    for _ in range(quantidade):
        x = random.randint(0, 100)
        if lado == "direito":
            x += 720 - 100
        y = random.randint(0, 720)
        tamanho = random.randint(10, 20)
        cor = random.choice(CORES)
        angulo = random.randint(0, 360)
        confetis.append({"cor": cor, "posicao": (x, y), "tamanho": tamanho, "angulo": angulo})
    return confetis

# Função para desenhar confetis
def confetiiis(confetis_esquerda, confetis_direita, screen):
    def desenhar_tracinho(ecrã, cor, inicio, comprimento, angulo):
        radianos = math.radians(angulo)
        fim_x = inicio[0] + comprimento * math.cos(radianos)
        fim_y = inicio[1] + comprimento * math.sin(radianos)
        pygame.draw.line(ecrã, cor, inicio, (fim_x, fim_y), 3)

    for confetti in confetis_esquerda:
        desenhar_tracinho(screen, confetti["cor"], confetti["posicao"], confetti["tamanho"], confetti["angulo"])

    for confetti in confetis_direita:
        desenhar_tracinho(screen, confetti["cor"], confetti["posicao"], confetti["tamanho"], confetti["angulo"])

# Função principal do jogo
def the_end_of_game():
    square_transition(screen)
    settings = Settings()

    poppins = pygame.font.Font("fonts/Cocogoose-Classic-Medium-trial.ttf", 35)
    button_text = poppins.render("CONGRATSS!:)", True, (0, 0, 0))


    # Setup inicial
    bigimage = pygame.image.load("images/menus/menus_back.png").convert()
    bigimage= pygame.transform.scale(bigimage, screen_resolution)

    platform = pygame.image.load("images/backgrounds/platform_levels.png")
    platform = pygame.transform.scale(platform, (250,250))
    avatare = pygame.image.load("images/avatar/JungleRex/JungleRex 3.png")
    avatare = pygame.transform.scale(avatare, (200, 188))
    clock = pygame.time.Clock()
    avatar = Avatar(screen, 300, 300, "JungleRex")
    fps = 60
    running = True

    # Gerar confetis
    confetis_esquerda = criar_confetis(500, lado="esquerdo")
    confetis_direita = criar_confetis(500, lado="direito")

    while running:
        clock.tick(fps)

        # Renderiza o fundo
        screen.blit(bigimage, (0,0))

        # Desenha os confetis
        confetiiis(confetis_esquerda, confetis_direita, screen)

        # Atualiza o avatar


        # Botão de configurações
        settings = pygame.image.load("backgroundgame_level/settings_button.png")
        settings_rect = settings.get_rect(topleft=(30, 50))
        screen.blit(settings, (30, 50))
        screen.blit(platform, (250, 250))
        screen.blit(avatare, (289, 200))
        screen.blit(button_text, (250,500))
        # Loop de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if settings_rect.collidepoint(event.pos):
                    return "settings"

        pygame.display.flip()


