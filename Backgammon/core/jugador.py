# 1. Atributos básicos:
#     nombre: Identificación del jugador

#     color: "B" (blanco) o "N" (negro)

#     fichas_en_juego: Fichas aún en el tablero

#     fichas_capturadas: Fichas en la barra

#     fichas_sacadas: Fichas que ya salieron del tablero
class jugador:
    def __init__(self, barra, fichas_sacadas):
        self.nombre1 = str(input("ingresa tu nombre: "))
        self.nombre2 = str(input("ingresa tu nombre: "))
        self.ficha = int(input("elige ficha (1 para blancas, 2 para rojas)"))
        self.barra = barra
        self.fichas_sacadas = fichas_sacadas

        if self.ficha == 1:
            self.color1 = "B"
            self.color2 = "R"
            print(f"{self.nombre1} juega con Blancas, {self.nombre2} con Rojas")
        elif self.ficha == 2:
            self.color1 = "R"
            self.color2 = "B"
            print(f"{self.nombre1} juega con Rojas, {self.nombre2} con Blancas")
        else:
            print("Opción inválida. Asignando Blancas al Jugador 1")
            self.color1 = "B"
            self.color2 = "R"
if __name__ == "__main__":
    # Código de prueba para la clase Jugador
    print("🎲 TESTEO DE CLASE JUGADOR 🎲")
    print("-" * 30)
    
    # Crear instancia de jugador
    jugador = Jugador()
    
    # Mostrar información del jugador
    print("\n📊 INFORMACIÓN DEL JUGADOR:")
    print(f"Nombre 1: {jugador.nombre1}")
    print(f"Nombre 2: {jugador.nombre2}")
    print(f"Color 1: {jugador.color1}")
    print(f"Color 2: {jugador.color2}")
    print(f"Ficha elegida: {jugador.ficha}")
    print(f"Barra: {jugador.barra}")
    print(f"Fichas sacadas: {jugador.fichas_sacadas}")
    
    # Test de funcionalidades adicionales (si las tuvieras)
    print("\n🧪 Prueba completada exitosamente!")
