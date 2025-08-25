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
    
    def realizar_movimiento_automatico(self, jugador, dados):
        """
        Realiza movimientos automáticos basados en los dados
        
        Args:
            jugador: "B" o "N" (color del jugador)
            dados: lista con los valores de los dados [dado1, dado2]
        """
        movimientos_realizados = []
        
        # Si son dados dobles, se pueden hacer 4 movimientos
        movimientos_totales = 4 if dados[0] == dados[1] else 2
        dados_disponibles = dados.copy()
        
        for _ in range(movimientos_totales):
            if not dados_disponibles:
                break
            
            # Buscar todos los movimientos posibles
            movimiento = self.encontrar_movimiento_valido(jugador, dados_disponibles)
            
            if movimiento:
                desde, hasta, dado_usado = movimiento
                # Ejecutar el movimiento
                valido, mensaje = self.tablero.movimiento_valido(desde, hasta, jugador, dado_usado)
                if valido:
                    self.tablero.mover_ficha(desde, hasta, jugador)
                    movimientos_realizados.append((desde, hasta))
                    dados_disponibles.remove(dado_usado)
                    print(f"Movimiento automático: {desde} → {hasta} (dado: {dado_usado})")
                else:
                    print(f"Movimiento inválido: {mensaje}")
                    break
            else:
                print("No hay movimientos posibles")
                break
        
        return movimientos_realizados
    
    def encontrar_movimiento_valido(self, jugador, dados):
        """
        Encuentra un movimiento válido para el jugador
        
        Returns:
            tuple: (desde, hasta, dado) o None si no hay movimientos
        """
        # Prioridad 1: Mover desde barra si hay fichas capturadas
        if jugador == "B" and self.tablero.barra_blancas:
            for dado in dados:
                destino = self.calcular_destino_desde_barra(jugador, dado)
                if self.tablero.movimiento_valido(0, destino, jugador, dado)[0]:
                    return (0, destino, dado)
        elif jugador == "N" and self.tablero.barra_negras:
            for dado in dados:
                destino = self.calcular_destino_desde_barra(jugador, dado)
                if self.tablero.movimiento_valido(0, destino, jugador, dado)[0]:
                    return (0, destino, dado)
        
        # Prioridad 2: Sacar fichas si es posible
        if self.tablero.puede_sacar(jugador):
            for punto in range(1, 25):
                if self.tablero.celda[punto] and self.tablero.celda[punto][0] == jugador:
                    for dado in dados:
                        if self.es_movimiento_salida_valido(punto, dado, jugador):
                            if self.tablero.movimiento_valido(punto, 25, jugador, dado)[0]:
                                return (punto, 25, dado)
        
        # Prioridad 3: Movimientos normales
        for punto in range(1, 25):
            if self.tablero.celda[punto] and self.tablero.celda[punto][0] == jugador:
                for dado in dados:
                    destino = self.calcular_destino(punto, dado, jugador)
                    if 1 <= destino <= 24:
                        if self.tablero.movimiento_valido(punto, destino, jugador, dado)[0]:
                            return (punto, destino, dado)
        
        return None
    
    def calcular_destino_desde_barra(self, jugador, dado):
        """Calcula destino desde barra según jugador"""
        if jugador == "B":
            return dado  # Blancas: barra → punto [dado]
        else:
            return 25 - dado  # Negras: barra → punto [25 - dado]
    
    def calcular_destino(self, punto, dado, jugador):
        """Calcula destino normal según jugador"""
        if jugador == "B":
            return punto + dado  # Blancas: avanzan
        else:
            return punto - dado  # Negras: retroceden
    
    def es_movimiento_salida_valido(self, punto, dado, jugador):
        """Verifica si puede sacar ficha"""
        if jugador == "B":
            return punto + dado > 24  # Blancas: punto + dado > 24
        else:
            return punto - dado < 1   # Negras: punto - dado < 1
    
    def jugar_turno_automatico(self, jugador):
        """Juega un turno completo automáticamente"""
        print(f"\n=== TURNO DE {'BLANCAS' if jugador == 'B' else 'NEGRAS'} ===")
        
        # Tirar dados
        dados = self.tirar_dados()
        if dados is None:
            return False  # Juego terminado
        
        # Realizar movimientos automáticos
        movimientos = self.realizar_movimiento_automatico(jugador, dados)
        
        # Mostrar resultado
        print(f"Movimientos realizados: {movimientos}")
        self.tablero.mostrar_board()
        
        # Verificar victoria
        victoria, ganador = self.tablero.win_conditions()
        if victoria:
            print(f"¡{'BLANCAS' if ganador == 'B' else 'NEGRAS'} GANAN!")
            return False
        
        return True

if __name__ == "__main__":
    # Crear instancia de dados
    dado_manager = Dice()
    
    # Juego automático de ejemplo
    jugador_actual = "B"  # Comienzan las blancas
    
    while True:
        if not dado_manager.jugar_turno_automatico(jugador_actual):
            break
        
        # Cambiar turno
        jugador_actual = "N" if jugador_actual == "B" else "B"
