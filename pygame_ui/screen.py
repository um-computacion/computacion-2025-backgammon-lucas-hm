"""Interfaz gráfica del juego Backgammon usando pygame."""

import random
from dataclasses import dataclass
from typing import Dict, List, Tuple

import pygame

import os

# Base del proyecto: carpeta donde está este archivo (screen.py)
BASE_DIR = os.path.dirname(__file__)

# Constantes globales
WIDTH = 1920
HEIGHT = 1080
DADO_SIZE = (100, 100)
FPS = 60
COLOR_TURNO_BLANCO = (240, 240, 255)
COLOR_TURNO_NEGRO = (255, 240, 240)
RUTA_TABLERO = os.path.join(BASE_DIR, "..", "assets", "Tablero.png")
RUTA_DADOS = os.path.join(BASE_DIR, "..", "assets", "dado-{}.png")
RUTA_FICHA_BLANCA = os.path.join(BASE_DIR, "..", "assets", "ficha-blanca.png")
RUTA_FICHA_NEGRA = os.path.join(BASE_DIR, "..", "assets", "ficha-negra.png")


@dataclass
class EstadoJuego:
    """Agrupa el estado dinámico del juego."""
    dado1: int = 0
    dado2: int = 0
    jugadas: int = 0
    turno_actual: str = "Blanco"
    running: bool = True


class Screen:
    """Clase que gestiona la ventana, tablero gráfico y dados."""

    def __init__(self) -> None:
        """Inicializa la ventana y los recursos gráficos."""
        pygame.init()
        self.window: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Backgammon con Dados")
        self.clock: pygame.time.Clock = pygame.time.Clock()

        self.background_base: pygame.Surface = self._cargar_tablero()
        self.dados_imgs: List[pygame.Surface] = self._cargar_dados()

        self.estado: EstadoJuego = EstadoJuego()
        self.coords: Dict[int, Tuple[int, int]] = self._generar_coordenadas()
        self.posiciones: Dict[int, List[Tuple[str, int]]] = {i: [] for i in range(1, 25)}
        self._inicializar_fichas()
        # Precargar imágenes de fichas con fallback
        if os.path.exists(RUTA_FICHA_BLANCA):
            self.ficha_blanca_img = pygame.image.load(RUTA_FICHA_BLANCA)
        else:
            print("⚠️ No se encontró ficha blanca, usando placeholder")
            self.ficha_blanca_img = pygame.Surface((50, 50))
            self.ficha_blanca_img.fill((255, 255, 255))

        if os.path.exists(RUTA_FICHA_NEGRA):
            self.ficha_negra_img = pygame.image.load(RUTA_FICHA_NEGRA)
        else:
            print("⚠️ No se encontró ficha negra, usando placeholder")
            self.ficha_negra_img = pygame.Surface((50, 50))
            self.ficha_negra_img.fill((0, 0, 0))


    def _cargar_tablero(self) -> pygame.Surface:
        """Carga y escala el fondo del tablero."""
        if not os.path.exists(RUTA_TABLERO):
            print(f"❌ No se encontró la imagen del tablero en: {RUTA_TABLERO}")
        else:
            print(f"✅ Cargando tablero desde: {RUTA_TABLERO}")
        tablero = pygame.image.load(RUTA_TABLERO)
        return pygame.transform.scale(tablero, (WIDTH, HEIGHT))

    def _cargar_dados(self) -> List[pygame.Surface]:
        """Carga y escala las imágenes de los dados."""
        return [
            pygame.transform.scale(
                pygame.image.load(RUTA_DADOS.format(i)),
                DADO_SIZE
            )
            for i in range(1, 7)
        ]

    def _generar_coordenadas(self) -> Dict[int, Tuple[int, int]]:
        """Genera las coordenadas de cada punto del tablero."""
        coords: Dict[int, Tuple[int, int]] = {}
        for i in range(1, 25):
            x_base = 150 + (i - 1) % 6 * 80
            x_offset = 200 if 7 <= i <= 12 else 0
            x_mirror = ((24 - i) % 6 * 80) if i > 12 else 0
            x = x_base + x_offset + x_mirror
            y = 900 if i <= 12 else 150
            coords[i] = (x, y)
        return coords

    def _inicializar_fichas(self) -> None:
        """Coloca las fichas iniciales en el tablero."""
        self.posiciones = {i: [] for i in range(1, 25)}

        # Distribución inicial ejemplo
        self.posiciones[1].append(("Blanca", 3))
        self.posiciones[2].append(("Blanca", 5))
        self.posiciones[5].append(("Blanca", 2))
        self.posiciones[7].append(("Blanca", 5))
        self.posiciones[20].append(("Negra", 5))
        self.posiciones[21].append(("Negra", 3))
        self.posiciones[23].append(("Negra", 5))
        self.posiciones[24].append(("Negra", 2))


    @staticmethod
    def _tirar_dados() -> Tuple[int, int, int]:
        """Genera dos valores aleatorios de dados."""
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        jugadas = 4 if dado1 == dado2 else 2
        return dado1, dado2, jugadas

    def _cambiar_turno(self) -> None:
        """Alterna el turno entre Blanco y Negro."""
        self.estado.turno_actual = (
            "Negro" if self.estado.turno_actual == "Blanco" else "Blanco"
        )

    def _dibujar_tablero(self) -> None:
        """Dibuja el fondo del tablero con overlay de turno."""
        fondo_color = (
            COLOR_TURNO_BLANCO if self.estado.turno_actual == "Blanco"
            else COLOR_TURNO_NEGRO
        )
        fondo = self.background_base.copy()
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(60)
        overlay.fill(fondo_color)
        fondo.blit(overlay, (0, 0))
        self.window.blit(fondo, (0, 0))

    def _dibujar_dados_y_texto(self) -> None:
        """Dibuja los dados y la información del turno."""
        if not (self.estado.dado1 and self.estado.dado2):
            return

        self.window.blit(self.dados_imgs[self.estado.dado1 - 1], (250, 250))
        self.window.blit(self.dados_imgs[self.estado.dado2 - 1], (450, 250))

        font = pygame.font.SysFont(None, 48)
        texto_jugadas = font.render(f"Jugadas: {self.estado.jugadas}", True, (0, 0, 255))
        self.window.blit(texto_jugadas, (300, 400))

        color_turno = (0, 0, 0) if self.estado.turno_actual == "Blanco" else (80, 0, 0)
        texto_turno = font.render(
            f"Turno: {self.estado.turno_actual}",
            True,
            color_turno
        )
        self.window.blit(texto_turno, (300, 460))

    def loop_principal(self) -> None:
        """Ejecuta el bucle principal del juego gráfico."""
        while self.estado.running:
            self._manejar_eventos()

            # Dibujar en el orden correcto:
            self._dibujar_tablero()       # Fondo del tablero
            self._dibujar_fichas()        # Fichas sobre el tablero
            self._dibujar_dados_y_texto() # Dados y texto sobre todo

            pygame.display.update()
            self.clock.tick(FPS)
        
        pygame.quit()


    def _manejar_eventos(self) -> None:
        """Maneja los eventos del juego."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.estado.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.estado.dado1, self.estado.dado2, self.estado.jugadas = self._tirar_dados()
                self._cambiar_turno()

    def _dibujar_fichas(self) -> None:
        """Dibuja todas las fichas en el tablero, apiladas correctamente según su posición."""
        for punto, fichas in self.posiciones.items():
            x, y = self.coords[punto]
            for ficha_color, cantidad in fichas:
                img = self.ficha_blanca_img if ficha_color == "Blanca" else self.ficha_negra_img
                for i in range(cantidad):
                    # Si el punto está en la mitad superior del tablero, apilar hacia abajo
                    if y < HEIGHT // 2:
                        self.window.blit(img, (x, y + i * 30))
                    # Si el punto está en la mitad inferior del tablero, apilar hacia arriba
                    else:
                        self.window.blit(img, (x, y - i * 30))


if __name__ == "__main__":
    juego = Screen()
    juego.loop_principal()
