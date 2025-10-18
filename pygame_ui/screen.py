"""Interfaz gráfica del juego Backgammon usando pygame"""

import pygame
import random


class Screen:
    """Clase que gestiona la ventana, tablero gráfico y dados"""

    def __init__(self):
        """Inicializa la ventana y recursos gráficos"""
        pygame.init()
        self.WIDTH, self.HEIGHT = 1920, 1080
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Juego con Dados")
        self.clock = pygame.time.Clock()

        self.background_base = pygame.image.load("assets/Tablero.png")
        self.background_base = pygame.transform.scale(self.background_base, (self.WIDTH, self.HEIGHT))

        self.dados_imgs: list[pygame.Surface] = []
        for i in range(1, 7):
            img = pygame.image.load(f"assets/dado-{i}.png")
            img = pygame.transform.scale(img, (100, 100))
            self.dados_imgs.append(img)

        self.dado1 = 0
        self.dado2 = 0
        self.jugadas = 0
        self.running = True
        self.turno_actual = "Blanco"  # Turno inicial

        self.coords: dict[int, tuple[int, int]] = {
            i: (150 + (i - 1) % 6 * 80 + (i > 6 and i < 13) * 200 + (i > 12) * ((24 - i) % 6 * 80), 900 if i <= 12 else 150)
            for i in range(1, 25)
        }

        self.posiciones: dict[int, list[tuple[str, int]]] = {i: [] for i in range(1, 25)}
        self.inicializar_fichas()

    def inicializar_fichas(self):
        """Coloca las fichas iniciales en el tablero"""
        self.posiciones[1].append(("assets/ficha-blanca.png", 3))
        self.posiciones[2].append(("assets/ficha-blanca.png", 5))
        self.posiciones[5].append(("assets/ficha-blanca.png", 2))
        self.posiciones[7].append(("assets/ficha-blanca.png", 5))

        self.posiciones[20].append(("assets/ficha-negra.png", 5))
        self.posiciones[21].append(("assets/ficha-negra.png", 3))
        self.posiciones[23].append(("assets/ficha-negra.png", 5))
        self.posiciones[24].append(("assets/ficha-negra.png", 2))

    def tirar_dados(self) -> tuple[int, int, int]:
        """Genera dos valores aleatorios de dados"""
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        jugadas = 4 if dado1 == dado2 else 2
        return dado1, dado2, jugadas

    def cambiar_turno(self):
        """Alterna el turno entre Blanco y Negro"""
        self.turno_actual = "Negro" if self.turno_actual == "Blanco" else "Blanco"

    def loop_principal(self):
        """Ejecuta el bucle principal del juego gráfico"""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.dado1, self.dado2, self.jugadas = self.tirar_dados()
                    self.cambiar_turno()

            # Fondo dinámico según turno
            fondo_color = (240, 240, 255) if self.turno_actual == "Blanco" else (255, 240, 240)
            fondo = self.background_base.copy()
            overlay = pygame.Surface((self.WIDTH, self.HEIGHT))
            overlay.set_alpha(60)
            overlay.fill(fondo_color)
            fondo.blit(overlay, (0, 0))
            self.window.blit(fondo, (0, 0))

            if self.dado1 and self.dado2:
                self.window.blit(self.dados_imgs[self.dado1 - 1], (250, 250))
                self.window.blit(self.dados_imgs[self.dado2 - 1], (450, 250))

                font = pygame.font.SysFont(None, 48)
                texto = font.render(f"Jugadas: {self.jugadas}", True, (0, 0, 255))
                self.window.blit(texto, (300, 400))

                color_turno = (0, 0, 0) if self.turno_actual == "Blanco" else (80, 0, 0)
                turno_texto = font.render(f"Turno: {self.turno_actual}", True, color_turno)
                self.window.blit(turno_texto, (300, 460))

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    juego = Screen()
    juego.loop_principal()
    