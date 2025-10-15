"""Clase que representa a los jugadores del juego Backgammon"""

class Jugador:
    """Define los atributos y configuración de los jugadores"""

    def __init__(self, es_humano: bool = True):
        """
        Inicializa los atributos básicos del jugador.

        Args:
            es_humano (bool): Indica si el jugador es humano.
        """
        self.nombre1: str | None = None
        self.nombre2: str | None = None
        self.ficha: int | None = None
        self.fichas_fuera: int = 0
        self.fichas_en_barra: int = 0
        self.es_humano: bool = es_humano

        self.barra: list | None = None
        self.fichas_sacadas: list | None = None
        self.color1: str | None = None
        self.color2: str | None = None

    def datos(self, barra: list, fichas_sacadas: list):
        """
        Solicita los nombres y colores de los jugadores.

        Args:
            barra (list): Fichas en la barra.
            fichas_sacadas (list): Fichas que ya salieron del tablero.
        """
        self.nombre1 = str(input("Ingresa tu nombre: "))
        self.nombre2 = str(input("Ingresa tu nombre: "))
        self.ficha = int(input("Elige ficha (1 para blancas, 2 para negras): "))
        self.barra = barra
        self.fichas_sacadas = fichas_sacadas

        if self.ficha == 1:
            self.color1 = "○"
            self.color2 = "●"
            print(f"{self.nombre1} juega con Blancas, {self.nombre2} con Negras")
        elif self.ficha == 2:
            self.color1 = "●"
            self.color2 = "○"
            print(f"{self.nombre1} juega con Negras, {self.nombre2} con Blancas")
        else:
            print("Opción inválida. Asignando Blancas al Jugador 1")
            self.color1 = "○"
            self.color2 = "●"