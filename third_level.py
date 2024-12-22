from characters.avatar import Avatar
from config import *
import game_loop
from the_end import the_end_of_game


# define the tile size
tile_size = 150
screen = pygame.display.set_mode((720, 720))

global all_sprites

def fade_in(screen, color=(0, 0, 0), duration=1000):
    fade_surface = pygame.Surface(screen.get_size())
    fade_surface.fill(color)
    for alpha in range(255, 0, -5):  # Inicia com opacidade alta e reduz gradualmente
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(int(duration / 255))


class World:
    def __init__(self, data):
        self.tile_list = []
        self.platform_for_game = pygame.image.load("images/backgrounds/platform_levels.png")
        self.load_data(data)
        self.scroll_speed = 55  # Speed at which platforms scroll
        self.scroll_timer = 0  # Timer to control scrolling
        self.avatar_speed = 5
        self.list_of_left_wall = []
        self.list_of_right_wall = []
        self.list_of_roofs = []
        self.list_of_grounds = []

    def load_data(self, data):
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    self.image = pygame.transform.scale(self.platform_for_game,
                                                        (tile_size, tile_size))  # Load the platform image
                    self.rect = self.image.get_rect()  # Get the rectangle of the platform image
                    self.rect.x = col_count * (tile_size * 0.715)  # Position the platform in the column
                    self.rect.y = row_count * (tile_size * 0.715)  # Position the platform in the row
                    tile = (self.image, self.rect)  # Add a timer placeholder
                    self.tile_list.append(tile)

                col_count += 1
            row_count += 1

    def draw(self, scroll_speed):
        for tile in self.tile_list:  # Draw each platform
            tile[1].x += scroll_speed
            screen.blit(tile[0], tile[1])  # Draw the platform image at the platform rectangle

    def get_limits(self):

        for tile in self.tile_list:
            self.rect = tile[1]
            left_wall = pygame.Rect(self.rect.x, self.rect.y + 80, 1,
                                    self.rect.height)  # (x=100, y=100, width=200, height=150)
            right_wall = pygame.Rect(self.rect.x + self.rect.width, self.rect.y + 80, 1,
                                     self.rect.height)  # (x=100, y=100, width=200, height=150)
            roof = pygame.Rect(self.rect.x, self.rect.y + self.rect.height, self.rect.width,
                               1)  # (x=100, y=100, width=200, height=150)
            ground = pygame.Rect(self.rect.x, self.rect.y + 70, self.rect.width,
                                 1)  # (x=100, y=100, width=200, height=150)

            self.list_of_left_wall.append(left_wall)
            self.list_of_right_wall.append(right_wall)
            self.list_of_roofs.append(roof)
            self.list_of_grounds.append(ground)


world_data = [
    # draw the first row
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0,
     1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1,
     0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],

]

world = World(world_data)
world.get_limits()

list_of_left_wall = world.list_of_left_wall
list_of_right_wall = world.list_of_right_wall
list_of_roofs = world.list_of_roofs
list_of_grounds = world.list_of_grounds


def button_when_scroll_stop_levelthree(screen):
    poppins = pygame.font.Font("fonts/Cocogoose-Classic-Medium-trial.ttf", 35)
    button_text = poppins.render("YOU WONN", True, (0, 0, 0))
    button_rect = button_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    while True:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                square_transition(screen)  # Chama o efeito de fade antes de mudar para o próximo nível
                the_end_of_game()  # Chama o ultimo nível
                return

        button_text = poppins.render("YOU WONN", True, (255, 255, 255) if button_rect.collidepoint(mouse) else (0, 0, 0))
        screen.blit(button_text, button_rect)
        pygame.display.update()


# Função para criar um efeito de fade
def square_transition(screen, color=(0, 0, 0), duration=1500):
    """
    Efeito de transição em formato de quadrado.
    - `color`: Cor do quadrado.
    - `duration`: Duração total do efeito em milissegundos (5 segundos no caso).
    """
    screen_width, screen_height = screen.get_size()
    center_x, center_y = screen_width // 2, screen_height // 2

    # Calcula o número de frames e o incremento por frame
    clock = pygame.time.Clock()
    total_frames = duration // 30  # Número de frames (assumindo 30ms por frame)
    max_size = max(screen_width, screen_height) * 2  # Tamanho máximo do quadrado
    step = max_size / total_frames  # Incremento do tamanho por frame

    size = 0  # Tamanho inicial do quadrado

    for _ in range(total_frames):
        # Calcula a posição e o tamanho do quadrado
        rect_x = center_x - size // 2
        rect_y = center_y - size // 2

        # Desenha o quadrado crescente
        pygame.draw.rect(screen, color, (rect_x, rect_y, size, size))

        pygame.display.update()
        clock.tick(60)  # Garante 30ms por frame (aproximadamente 33 FPS)

        # Aumenta o tamanho do quadrado
        size += step


# Função do botão


def execute_game_levelthree():
    square_transition(screen)

    # SETUP:
    double_jump = False
    bigimage = pygame.image.load("images/backgrounds/background_of_level3.png").convert()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Jungle Rex")

    running = True
    bg_x = 0  # Posição horizontal da big image
    bg_width = bigimage.get_width()

    avatar = Avatar(screen, 40, 0, "JungleRex")
    all_sprites = pygame.sprite.Group()
    all_sprites.add(avatar)

    while running:
        clock.tick(fps)  # Control frame rate
        all_sprites.update(list_of_left_wall, list_of_right_wall, list_of_grounds, double_jump, list_of_roofs)

        keys = pygame.key.get_pressed()  # Verifica quais teclas estão pressionadas
        scroll_speed = 0  # Inicializa scroll_speed como 0

        # Movimento do avatar e sincronização
        if keys[pygame.K_RIGHT]:
            if avatar.rect.x < 500:  # Limita o avatar ao centro da tela (direita)
                avatar.rect.x += avatar.speed
            elif bg_x > -(bg_width - screen.get_width()):  # Move o fundo e plataformas
                scroll_speed = -avatar.speed
            else:
                scroll_speed = 0  # Para o movimento se o fundo atingir o limite direito
                the_end_of_game()
        elif keys[pygame.K_LEFT]:
            if avatar.rect.x > 100:  # Limita o avatar ao lado esquerdo da tela
                avatar.rect.x -= avatar.speed
            elif bg_x < 0:  # Move o fundo e plataformas
                scroll_speed = avatar.speed
            else:
                scroll_speed = 0  # Para o movimento se o fundo atingir o limite esquerdo

        # Ajuste do fundo (big image)
        bg_x += scroll_speed  # Move o fundo conforme a velocidade do scroll

        # Renderiza o fundo
        screen.blit(bigimage, (bg_x, -125))

        # Renderiza as plataformas
        world.draw(scroll_speed)

        # Renderiza o avatar
        all_sprites.draw(screen)

        # Botão de configurações
        settings = pygame.image.load("backgroundgame_level/settings_button.png")
        settings_rect = settings.get_rect(topleft=(30, 50))
        screen.blit(settings, (30, 50))

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if settings_rect.collidepoint(event.pos):
                    current_state = "settings"
        pygame.display.flip()  # Atualiza a tela
