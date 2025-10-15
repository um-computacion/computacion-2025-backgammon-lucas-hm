"""Módulo CLI para ejecutar Backgammon desde consola"""

# pylint: disable=no-member
# pylint: disable=broad-exception-caught

import sys
import time
from typing import TYPE_CHECKING

from core.juego import Juego

if TYPE_CHECKING:
    from core.tablero import Tablero  # noqa: F401  --- sólo para anotaciones estáticas

print("ejecutando cli.py ...")


class BackgammonCLI:
    """Interfaz de línea de comandos para jugar Backgammon"""

    juego: Juego
    running: bool

    def __init__(self):
        """Inicializa la instancia del juego y el estado de ejecución"""
        self.juego = Juego()
        self.running = True

    def mostrar_menu_principal(self):
        """Muestra el menú principal y gestiona la navegación del usuario"""
        while self.running:
            print("\n" + "=" * 50)
            print("🎲 BACKGAMMON - MENÚ PRINCIPAL 🎲")
            print("=" * 50)
            print("1. 🎯 Nueva Partida")
            print("2. 📊 Ver Reglas")
            print("3. 🏆 Historial de Partidas")
            print("4. ⚙️  Configuración")
            print("5. 🚪 Salir")
            print("=" * 50)

            opcion = input("Selecciona una opción (1-5): ").strip()

            if opcion == "1":
                self.nueva_partida()
            elif opcion == "2":
                self.mostrar_reglas()
            elif opcion == "3":
                self.mostrar_historial()
            elif opcion == "4":
                self.configuracion()
            elif opcion == "5":
                self.salir()
            else:
                print("❌ Opción no válida. Intenta nuevamente.")

    def nueva_partida(self):
        """Permite al usuario seleccionar el modo de juego"""
        print("\n" + "=" * 50)
        print("🎯 NUEVA PARTIDA")
        print("=" * 50)

        print("\nModos de juego:")
        print("1. 🤖 vs 🤖 (Automático completo)")
        print("2. 👤 vs 🤖 (Humano vs IA)")
        print("3. 👤 vs 👤 (Dos jugadores)")

        modo = input("Selecciona modo (1-3): ").strip()

        if modo == "1":
            self.partida_automatica()
        elif modo == "2":
            self.partida_humano_vs_ia()
        else:
            print("Modo no válido, iniciando automático")
            self.partida_automatica()

    def partida_automatica(self):
        """Ejecuta una partida automática entre dos IAs"""
        print("\n🤖 Iniciando partida automática...")
        print("Los movimientos se realizarán automáticamente")
        input("Presiona Enter para comenzar...")

        self.juego.jugar_partida_completa()
        input("\nPresiona Enter para volver al menú...")

    def partida_humano_vs_ia(self):
        """Configura y lanza una partida entre humano e IA"""
        print("\n👤 vs 🤖 Modo Humano vs IA")

        print("\nSelecciona tu color:")
        print("1. ⚪ Blancas (empiezas primero)")
        print("2. ⚫ Negras (IA empieza primero)")

        color = input("Opción (1-2): ").strip()
        jugador_humano = "B" if color == "1" else "N"

        print(f"\nJugando como {'Blancas' if jugador_humano == 'B' else 'Negras'}...")
        input("Presiona Enter para comenzar...")

        self.jugar_modo_humano_ia(jugador_humano)

    def jugar_modo_humano_ia(self, jugador_humano):
        """Ejecuta la lógica de turnos para el modo humano vs IA"""
        turno = 1

        while True:
            print(f"\n--- TURNO {turno} ---")
            self.juego.tablero.mostrar_board()

            if self.juego.jugador_actual == jugador_humano:
                self.turno_humano()
            else:
                print(
                    f"🤖 IA ({'Blancas' if self.juego.jugador_actual == 'B' else 'Negras'}) "
                    "pensando..."
                )
                time.sleep(1)
                self.juego.movimiento_automatico()

            victoria, ganador = self.juego.tablero.win_conditions()
            if victoria:
                self.mostrar_victoria(ganador)
                break

            turno += 1

    def turno_humano(self):
        """Gestiona el turno de un jugador humano"""
        print(
            f"👤 Tu turno ({'Blancas' if self.juego.jugador_actual == 'B' else 'Negras'})"
        )

        movimientos_posibles = self.obtener_movimientos_posibles()

        if not movimientos_posibles:
            print("❌ No hay movimientos posibles. Turno perdido.")
            self.juego.movimientos_restantes = 0
            return

        print("\nMovimientos posibles:")
        for i, (desde, hasta, dado) in enumerate(movimientos_posibles, 1):
            print(f"{i}. {desde} → {hasta} (dado: {dado})")

        while True:
            try:
                seleccion = input(
                    f"\nSelecciona movimiento (1-{len(movimientos_posibles)}): "
                ).strip()
                if seleccion.lower() == "salir":
                    return

                idx = int(seleccion) - 1
                if 0 <= idx < len(movimientos_posibles):
                    desde, hasta, dado = movimientos_posibles[idx]
                    break
                print("❌ Selección fuera de rango")
            except ValueError:
                print("❌ Ingresa un número válido")

        valido, mensaje = self.juego.tablero.movimiento_valido(
            desde, hasta, self.juego.jugador_actual, dado
        )
        if valido:
            self.juego.tablero.mover_ficha(desde, hasta, self.juego.jugador_actual)
            print(f"✅ Movimiento ejecutado: {desde} → {hasta}")
        else:
            print(f"❌ {mensaje}")

    def obtener_movimientos_posibles(self):
        """Calcula todos los movimientos válidos para el jugador actual"""
        movimientos = []

        for dado in self.juego.dados_disponibles():
            for punto in range(0, 25):
                if punto == 0 and not self.juego.tablero.puede_mover_desde_barra(
                    self.juego.jugador_actual
                ):
                    continue

                destino = self.juego.calcular_destino(punto, dado)
                if self.juego.tablero.movimiento_valido(
                    punto, destino, self.juego.jugador_actual, dado
                )[0]:
                    movimientos.append((punto, destino, dado))

        return movimientos

    def mostrar_reglas(self):
        """Imprime las reglas básicas del juego"""
        print("\n" + "=" * 50)
        print("📖 REGLAS DE BACKGAMMON")
        print("=" * 50)
        print(
            """
        1. Objetivo: Sacar todas tus fichas del tablero
        2. Movimiento: Según dados, avanzar o capturar
        3. Captura: Si caes en punto con 1 ficha enemiga
        4. Bloqueo: 2+ fichas protegen el punto
        5. Dados dobles: 4 movimientos del mismo valor
        6. Barra: Fichas capturadas deben reingresar
        """
        )
        input("Presiona Enter para continuar...")

    def mostrar_historial(self):
        """Muestra el historial de partidas (placeholder)"""
        print("\n📊 Historial de partidas (próximamente...)")
        time.sleep(1)

    def configuracion(self):
        """Muestra el menú de configuración (placeholder)"""
        print("\n⚙️  Configuración (próximamente...)")
        time.sleep(1)

    def mostrar_victoria(self, ganador):
        """Muestra el mensaje de victoria y el estado final del tablero"""
        print("\n" + "🎉" * 20)
        print(f"🏆 ¡{'BLANCAS' if ganador == 'B' else 'NEGRAS'} GANAN! 🏆")
        print("🎉" * 20)
        self.juego.tablero.mostrar_board()
        time.sleep(2)

    def salir(self):
        """Finaliza la ejecución del juego"""
        print("\n👋 ¡Gracias por jugar Backgammon!")
        self.running = False


def main():
    """Punto de entrada principal para ejecutar la CLI"""
    try:
        cli = BackgammonCLI()
        cli.mostrar_menu_principal()
    except KeyboardInterrupt:
        print("\n\n👋 Juego interrumpido. ¡Hasta pronto!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)