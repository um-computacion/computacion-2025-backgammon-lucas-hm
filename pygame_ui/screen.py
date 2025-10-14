import pygame
import random

class screen:
    # --- Pedir nombres ---
    def nombres_jugadores():
        jugador1 = input("ingresa tu nombre: ")
        jugador2 = input("ingresa tu nombre: ")

    pygame.init()

    def listas(self):
        # Crear las listas como atributos de la clase
        self.pos1 = []
        self.pos2 = []
        self.pos3 = []
        self.pos4 = []
        self.pos5 = []
        self.pos6 = []
        self.pos7 = []
        self.pos8 = []
        self.pos9 = []
        self.pos10 = []
        self.pos11 = []
        self.pos12 = []
        
        self.pos13 = []
        self.pos14 = []
        self.pos15 = []
        self.pos16 = []
        self.pos17 = []
        self.pos18 = []
        self.pos19 = []
        self.pos20 = []
        self.pos21 = []
        self.pos22 = []
        self.pos23 = []
        self.pos24 = []

                # --- Coordenadas para las 24 posiciones ---
        self.coords = {
            1: (150, 900), 2: (230, 900), 3: (310, 900), 4: (390, 900),
            5: (470, 900), 6: (550, 900), 7: (750, 900), 8: (830, 900),
            9: (910, 900), 10: (990, 900), 11: (1070, 900), 12: (1150, 900),
            13: (1150, 150), 14: (1070, 150), 15: (990, 150), 16: (910, 150),
            17: (830, 150), 18: (750, 150), 19: (550, 150), 20: (470, 150),
            21: (390, 150), 22: (310, 150), 23: (230, 150), 24: (150, 150)
        }
    
        # --- Fichas blancas ---
        self.pos1.append(('assets/ficha-blanca.png', 3))
        self.pos2.append(('assets/ficha-blanca.png', 5))
        self.pos5.append(('assets/ficha-blanca.png', 2))
        self.pos7.append(('assets/ficha-blanca.png', 5))

        # --- Fichas negras ---
        self.pos20.append(('assets/ficha-negra.png', 5))
        self.pos21.append(('assets/ficha-negra.png', 3))
        self.pos23.append(('assets/ficha-negra.png', 5))
        self.pos24.append(('assets/ficha-negra.png', 2))

    # --- Configuración de ventana ---
    WIDTH, HEIGHT = 1920, 1080
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