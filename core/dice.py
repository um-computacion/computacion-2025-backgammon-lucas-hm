# 1. Métodos esenciales:
#     tirar_dados(): Simular el tiro de dados
import random

class Dice:
    def tirar_dados(self):
        """Tira los dados y devuelve los valores con lógica de dobles"""
        minimo = 1
        maximo = 6
        
        while True:
            tirar = input("¿Tirar los dados? (s/n): ").lower().strip()
            
            if tirar in ['s', 'si', 'sí']:
                print("Tirando los dados...")
                dado1 = random.randint(minimo, maximo)
                dado2 = random.randint(minimo, maximo)
                
                print(f"Los números son: {dado1} y {dado2}")
                
                # ✅ LÓGICA DE DOBLES AÑADIDA
                if dado1 == dado2:
                    print(f"¡DOBLES {dado1}-{dado2}! Tienes 4 movimientos de {dado1}")
                    # Para dobles: devolver 4 dados del mismo valor
                    return [dado1, dado1, dado1, dado1]
                else:
                    return [dado1, dado2]
                
            elif tirar in ['n', 'no']:
                print("Juego terminado")
                return None
                
            else:
                print("Por favor responde 's' o 'n'")