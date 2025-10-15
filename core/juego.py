"""Lógica principal del juego de Backgammon"""

from core.dice import Dice
from core.tablero import board
from core.jugador import jugador
import random


class Juego:
    """Clase que gestiona el flujo completo de una partida de Backgammon"""

    def __init__(self):
        """Inicializa el estado del juego"""
        self.dados = Dice()
        self.tablero = board()
        self.jugadores = self.inicializar_jugadores()
        self.turno_actual = "B"

    def inicializar_jugadores(self):
        """Inicializa los jugadores y sus colores"""
        jugadores_info = jugador([], [])
        return {
            "B": {
                "nombre": (
                    jugadores_info.nombre1
                    if jugadores_info.color1 == "B"
                    else jugadores_info.nombre2
                ),
                "color": "B",
            },
            "N": {
                "nombre": (
                    jugadores_info.nombre2
                    if jugadores_info.color1 == "B"
                    else jugadores_info.nombre1
                ),
                "color": "N",
            },
        }

    def cambiar_turno(self):
        """Cambia el turno al otro jugador"""
        self.turno_actual = "N" if self.turno_actual == "B" else "B"

    def obtener_jugador_actual(self):
        """Devuelve la información del jugador actual"""
        return self.jugadores[self.turno_actual]

    def procesar_movimiento(self, desde, hasta, dado_usado):
        """Procesa un movimiento y actualiza el tablero"""
        valido, mensaje = self.tablero.movimiento_valido(
            desde, hasta, self.turno_actual, dado_usado
        )
        if not valido:
            return False, mensaje

        exito, mensaje = self.tablero.mover_ficha(desde, hasta, self.turno_actual)
        return exito, mensaje

    def jugar_turno(self, dados_resultado, movimientos=None):
        """
        Maneja un turno completo de un jugador.
        - `dados_resultado`: lista con los dados obtenidos.
        - `movimientos`: lista opcional de tuplas (desde, hasta, dado) para testear sin input().
        """
        print(
            f"\nTurno de {self.obtener_jugador_actual()['nombre']} "
            f"({'Blancas' if self.turno_actual == 'B' else 'Negras'})"
        )
        print(f"Dados: {dados_resultado[0]} y {dados_resultado[1]}")

        if self.tablero.puede_mover_desde_barra(self.turno_actual):
            print("Tienes fichas en la barra. Debes moverlas primero.")
            dado_usar = (
                dados_resultado[0]
                if self.puede_mover_desde_barra_con_dado(
                    self.turno_actual, dados_resultado[0]
                )
                else dados_resultado[1]
            )
            self.mover_desde_barra(dado_usar)
            dados_disponibles = [d for d in dados_resultado if d != dado_usar]
        else:
            dados_disponibles = list(dados_resultado)

        movimientos_iter = iter(movimientos) if movimientos is not None else None

        while dados_disponibles:
            self.tablero.mostrar_board()
            print(f"Dados disponibles: {dados_disponibles}")

            movimiento_valido = False
            while not movimiento_valido:
                try:
                    if movimientos_iter is not None:
                        desde, hasta, dado = next(movimientos_iter)
                    else:
                        desde = int(input("Ingresa punto de origen (1-24, 0 para barra): "))
                        hasta = int(input("Ingresa punto destino (1-24, 25 para sacar): "))
                        dado = int(input("Ingresa el dado a usar: "))

                    if dado not in dados_disponibles:
                        print("Ese dado no está disponible")
                        continue

                    exito, mensaje = self.procesar_movimiento(desde, hasta, dado)
                    if exito:
                        dados_disponibles.remove(dado)
                        movimiento_valido = True
                        print(mensaje)
                    else:
                        print(f"Movimiento inválido: {mensaje}")
                except ValueError:
                    print("Por favor ingresa números válidos")
                except StopIteration:
                    return False

        ganador, color_ganador = self.tablero.win_conditions()
        if ganador:
            nombre_ganador = self.jugadores[color_ganador]["nombre"]
            print(f"\n¡Felicidades {nombre_ganador}! Has ganado el juego.")
            return True

        return False

    def puede_mover_desde_barra_con_dado(self, jugador, dado):
        """Verifica si un jugador puede mover desde la barra con un dado específico"""
        punto_destino = dado if jugador == "B" else 25 - dado
        valido, _ = self.tablero.movimiento_valido(0, punto_destino, jugador, dado)
        return valido

    def mover_desde_barra(self, dado):
        """Mueve una ficha desde la barra usando un dado"""
        punto_destino = dado if self.turno_actual == "B" else 25 - dado
        exito, mensaje = self.procesar_movimiento(0, punto_destino, dado)
        if exito:
            print(f"Movido desde barra al punto {punto_destino}")
        else:
            print(f"No se pudo mover desde barra: {mensaje}")

    def jugar(self):
        """Bucle principal del juego"""
        print("¡Bienvenido al Backgammon!")
        print("Reglas:")
        print("- Las Blancas (B) mueven hacia puntos mayores")
        print("- Las Negras (N) mueven hacia puntos menores")
        print("- Debes mover fichas desde la barra primero si las tienes")
        print("- Gana el primero que saque todas sus fichas o forme 4 en línea")

        juego_terminado = False
        while not juego_terminado:
            self.tablero.mostrar_board()
            dados_resultado = self.dados.tirar_dados()
            if dados_resultado is None:
                print("Juego terminado por el usuario")
                break

            juego_terminado = self.jugar_turno(dados_resultado)

            if not juego_terminado:
                self.cambiar_turno()


if __name__ == "__main__":
    Juego()
