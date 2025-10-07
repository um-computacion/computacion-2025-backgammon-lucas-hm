# 1. Atributos básicos:
#     nombre: Identificación del jugador

#     color: "B" (blanco) o "N" (negro)


#     fichas_en_juego: Fichas aún en el tablero
class jugador:
    def __init__(self, es_humano=True):
        self.nombre1 = None
        self.nombre2 = None
        self.ficha = None
        self.fichas_fuera = 0
        self.fichas_en_barra = 0
        self.es_humano = es_humano

    def datos(self, barra, fichas_sacadas):
        self.nombre1 = str(input("ingresa tu nombre: "))
        self.nombre2 = str(input("ingresa tu nombre: "))
        self.ficha = int(input("elige ficha (1 para blancas, 2 para negras)"))
        self.barra = barra
        self.fichas_sacadas = fichas_sacadas

        if self.ficha == 1:
            self.color1 = "○"
            self.color2 = "●"
            print(f"{self.nombre1} juega con Blancas, {self.nombre2} con negras")
        elif self.ficha == 2:
            self.color1 = "●"
            self.color2 = "○"
            print(f"{self.nombre1} juega con negras, {self.nombre2} con Blancas")
        else:
            print("Opción inválida. Asignando Blancas al Jugador 1")
            self.color1 = "○"
            self.color2 = "●"
