#imports de librerias para eleccion de CLI o Pygame
import sys
import os

#imports de librerias para ejecucion de CLI
from CLI.cli import BackgammonCLI
from pygame_ui.screen import GameGUI

"""opciones a elegir"""
print("1. CLI")
print("2. Pygame")

#logica de eleccion de CLI o Pygame
eleccion = int(input("¿que deseas ejecutar?"))

#comparacion de eleccion con numeros
if eleccion == 1:
    cli = BackgammonCLI()
    cli.mostrar_menu_principal()
    cli.ejecutar()
elif eleccion == 2:
    gui = GameGUI()
    gui.ejecutar()
else:
    print("Opcion invalida")
    sys.exit()