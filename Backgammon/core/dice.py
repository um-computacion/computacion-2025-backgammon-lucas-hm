# 1. Métodos esenciales:
#     tirar_dados(): Simular el tiro de dados

#     realizar_movimiento(): Decidir qué movimiento hacer
import random
from tablero import board  # Importamos el tablero para usar sus funciones

class Dice:
    def __init__(self):
        self.tablero = board()
    
    def tirar_dados(self):
        """Tira los dados y devuelve los valores"""
        minimo = 1
        maximo = 6
        
        while True:
            tirar = input("¿Tirar los dados? (s/n): ").lower().strip()
            
            if tirar in ['s', 'si', 'sí']:
                print("Tirando los dados...")
                dado1 = random.randint(minimo, maximo)
                dado2 = random.randint(minimo, maximo)
                print(f"Los números son: {dado1} y {dado2}")
                print()
                return [dado1, dado2]
                
            elif tirar in ['n', 'no']:
                print("Juego terminado")
                return None
                
            else:
                print("Por favor responde 's' o 'n'")
                print()

if __name__ == "__main__":
    Dice.tirar_dados()