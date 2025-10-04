import pygame
import random

pygame.init()

# --- Configuración de ventana ---
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego con Dados")
clock = pygame.time.Clock()

# --- Cargar fondo ---
background = pygame.image.load("assets/Tablero.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# --- Cargar imágenes de dados ---
dados_imgs = []
for i in range(1, 7):
    img = pygame.image.load(f"assets/dado-{i}.png")
    img = pygame.transform.scale(img, (100, 100))  # tamaño de los dados en pantalla
    dados_imgs.append(img)

# --- Función para tirar dados ---
def tirar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    jugadas = 4 if dado1 == dado2 else 2
    return dado1, dado2, jugadas

# --- Variables de juego ---
running = True
dado1 = dado2 = jugadas = 0

# --- Loop principal ---
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Tirar dados al presionar espacio
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dado1, dado2, jugadas = tirar_dados()

    # --- Dibujar fondo ---
    screen.blit(background, (0, 0))

    # --- Mostrar dados si se tiraron ---
    if dado1 and dado2:
        screen.blit(dados_imgs[dado1 - 1], (250, 250))  # dado1
        screen.blit(dados_imgs[dado2 - 1], (450, 250))  # dado2

        # Texto de jugadas
        font = pygame.font.SysFont(None, 48)
        texto = font.render(f"Jugadas: {jugadas}", True, (0, 0, 255))
        screen.blit(texto, (300, 400))

    pygame.display.update()
    clock.tick(60)
pygame.quit()
