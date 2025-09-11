#1
def mostrar_board(self):
        print(f"\n{self.celda[1]}|{self.celda[2]}|{self.celda[3]}|{self.celda[4]}|{self.celda[5]}|{self.celda[6]}|{self.celda[7]}|{self.celda[8]}|{self.celda[9]}|{self.celda[10]}|{self.celda[11]}|{self.celda[12]}")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print(f"\n{self.celda[13]}|{self.celda[14]}|{self.celda[15]}|{self.celda[16]}|{self.celda[17]}|{self.celda[18]}|{self.celda[19]}|{self.celda[20]}|{self.celda[21]}|{self.celda[22]}|{self.celda[23]}|{self.celda[24]}")
en base a este tablero haceme la funcion que se va a llamar win_conditions


#2
donde deberia poner un sistema de turnos si tengo que seguir la siguiente estructura?
estructura codigo
/backgammon/
├── core/           → lógica del juego
├── cli/            → CLI
├── pygame_ui/      → interfaz gráfica
├── assets/         → imágenes, sonidos
└── requirements.txt

#3
el sistema de turnos iria en jugador?
ahora, continuemos en tablero. hay algo que quiero implementarle, quiero implementar reglas de salida y el sis de captura

#4 
quiero implementar reglas de salida y el sis de captura en mi codigo

#5 
#reglas de salida y sistema de captura
class board:
    def __init__(self):
        self.celda = {}
        self.celda[1] = ["N", "N"]
        
        self.celda[2] = []
        self.celda[3] = []
        self.celda[4] = []
        self.celda[5] = []
        
        self.celda[6] = ["B", "B", "B", "B", "B"]

        self.celda[7] = []

        self.celda[8] = ["N", "N", "N"]

        self.celda[9] = []
        self.celda[10] = []
        self.celda[11] = []

        self.celda[12] = ["B", "B", "B", "B", "B"]

        self.celda[13] = ["N", "N", "N", "N", "N"]

        self.celda[14] = []
        self.celda[15] = []
        self.celda[16] = []
        
        self.celda[17] = ["B", "B", "B"]

        self.celda[18] = []

        self.celda[19] = ["B", "B"]

        self.celda[20] = ["N", "N", "N"]
        self.celda[21] = []
        self.celda[22] = []
        self.celda[23] = []
        
        self.celda[24] = ["N", "N"]
        self.barra_blancas = []
        self.barra_negras = []
        self.fuera_blancas = []
        self.fuera_negras = []

    def mostrar_board(self):
        print(f"\n{self.celda[1]}|{self.celda[2]}|{self.celda[3]}|{self.celda[4]}|{self.celda[5]}|{self.celda[6]}|{self.celda[7]}|{self.celda[8]}|{self.celda[9]}|{self.celda[10]}|{self.celda[11]}|{self.celda[12]}")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print(f"\n{self.celda[13]}|{self.celda[14]}|{self.celda[15]}|{self.celda[16]}|{self.celda[17]}|{self.celda[18]}|{self.celda[19]}|{self.celda[20]}|{self.celda[21]}|{self.celda[22]}|{self.celda[23]}|{self.celda[24]}")
    
    def win_conditions(self):
    
        for i in range(1, 9):  # Del 1 al 8 (puede formar línea del 1-4 hasta 8-11)
            if (self.celda[i] == self.celda[i+1] == self.celda[i+2] == self.celda[i+3] != " "):
                return True, self.celda[i]
        
        # Horizontal - segunda fila
        for i in range(13, 21):  # Del 13 al 20 (puede formar línea del 13-16 hasta 20-23)
            if (self.celda[i] == self.celda[i+1] == self.celda[i+2] == self.celda[i+3] != " "):
                return True, self.celda[i]
        
        # Vertical - entre filas
        for i in range(1, 13):  # Del 1 al 12 (puede formar línea vertical con celda inferior)
            if i + 12 <= 24:  # Asegurar que existe la celda inferior
                if (self.celda[i] == self.celda[i+12] != " "):
                    # Para vertical necesitamos 4 en línea, así que verificamos 4 celdas verticales
                    if i <= 9:  # Solo verificar vertical si hay espacio para 4 celdas
                        if (self.celda[i] == self.celda[i+12] == self.celda[i+24] == self.celda[i+36] != " "):
                            return True, self.celda[i]
        for i in range(1, 10):
            if i + 13 <= 24:
                if (self.celda[i] == self.celda[i+13] == self.celda[i+26] == self.celda[i+39] != " "):
                    return True, self.celda[i]
        
        # Diagonal ascendente (de derecha a izquierda)
        for i in range(4, 13):  # Del 4 al 12
            if i + 11 <= 24:  # Asegurar que existe la diagonal
                if (self.celda[i] == self.celda[i+11] == self.celda[i+22] == self.celda[i+33] != " "):
                    return True, self.celda[i]
        
        # Verificar si hay empate (todas las celdas llenas)
        empate = True
        for i in range(1, 25):
            if self.celda[i] == " ":
                empate = False
                break
        
        if empate:
            return True, "Empate"
    
        return False, None
if __name__ == "__main__":
    tablero = board()
    tablero.mostrar_board()

#6
aca el pop y el append estan marcados en blanco
ficha = self.celda[desde].pop()
            self.celda[hasta].append(ficha)

#7
# Colocar ficha en destino
        if hasta <= 24:
            self.celda[hasta].append(ficha)

y 

# Verificar captura en punto destino
            if hasta <= 24 and self.celda[hasta] and self.celda[hasta][0] != jugador and len(self.celda[hasta]) == 1:
                self.capturar_ficha(hasta)
            ficha = self.celda[desde].pop()

se siguen marcando en blanco

#8
decime que tengo que programarle, despues te pido tu codigo para ver si va encaminado. ok?

#9
como se comentaba con combinaciones de teclado?

#10
como se comentaba con combinaciones de teclado?

#11
me podes dar un video de pygame sobre este juego que estoy programando?

#12
si tuviera el backgammon con poo completo y terminado, como lo harias con pygame?

#13
como puedo hacer que con pygame el juego tenga requerimientos de componentes, como una rtx 4050 y un i7 o ryzen 7 7000 series de minimo?

#14
def __init__(self, nombre1, nombre2, ficha, barra, fichas_sacadas):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.ficha = ficha
        self.barra = barra
        self.fichas_sacadas = fichas_sacadas

en los nombres, como hago que por un input ingresen los nombres?

#15
def __init__(self, barra, fichas_sacadas):
        self.nombre1 = str(input("ingresa tu nombre: "))
        self.nombre2 = str(input("ingresa tu nombre: "))
        self.ficha = int(input("elige ficha (1 para blancas, 2 para rojas)"))
        self.barra = barra
        self.fichas_sacadas = fichas_sacadas

        if self.ficha == 1:
            self.nombre1 == "blancas"
        if self.ficha == 2:
            self.nombre1 == "rojas"

este if para asignar fichas esta bien?

#16
yo quiero que realizar movimiento sea usado para decidir que movimiento hacer en base a lo que va a ir en dice.py luego, y que se haga automatico. asi que ahora vamos a programarle movimientos legales y nada mas

#17
class board:
    def __init__(self):
        self.celda = {}
        self.celda[1] = ["N", "N"]
        self.celda[2] = []
        self.celda[3] = []
        self.celda[4] = []
        self.celda[5] = []
        self.celda[6] = ["B", "B", "B", "B", "B"]
        self.celda[7] = []
        self.celda[8] = ["N", "N", "N"]
        self.celda[9] = []
        self.celda[10] = []
        self.celda[11] = []
        self.celda[12] = ["B", "B", "B", "B", "B"]
        self.celda[13] = ["N", "N", "N", "N", "N"]
        self.celda[14] = []
        self.celda[15] = []
        self.celda[16] = []
        self.celda[17] = ["B", "B", "B"]
        self.celda[18] = []
        self.celda[19] = ["B", "B"]
        self.celda[20] = ["N", "N", "N"]
        self.celda[21] = []
        self.celda[22] = []
        self.celda[23] = []
        self.celda[24] = ["N", "N"]
        self.barra_blancas = []
        self.barra_negras = []
        self.fuera_blancas = []
        self.fuera_negras = []

    def mostrar_board(self):
        print(f"\nBarra Blancas: {self.barra_blancas} | Barra Negras: {self.barra_negras}")
        print(f"Fuera Blancas: {len(self.fuera_blancas)} | Fuera Negras: {len(self.fuera_negras)}")
        print(f"\n{self.celda[1]}|{self.celda[2]}|{self.celda[3]}|{self.celda[4]}|{self.celda[5]}|{self.celda[6]}|{self.celda[7]}|{self.celda[8]}|{self.celda[9]}|{self.celda[10]}|{self.celda[11]}|{self.celda[12]}")
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print(f"\n{self.celda[13]}|{self.celda[14]}|{self.celda[15]}|{self.celda[16]}|{self.celda[17]}|{self.celda[18]}|{self.celda[19]}|{self.celda[20]}|{self.celda[21]}|{self.celda[22]}|{self.celda[23]}|{self.celda[24]}")

    def puede_mover_desde_barra(self, jugador):
        """Verifica si un jugador puede mover desde la barra"""
        if jugador == "B" and self.barra_blancas:
            return True
        if jugador == "N" and self.barra_negras:
            return True
        return False

    def movimiento_valido(self, desde, hasta, jugador, dado):
        """
        Valida si un movimiento es permitido según reglas de Backgammon
        
        Args:
            desde: punto de origen (1-24, 0 para barra)
            hasta: punto destino (1-24, 25 para sacar)
            jugador: "B" o "N"
            dado: valor del dado usado
        """
        # Verificar si el jugador tiene fichas en la barra (prioridad)
        if self.puede_mover_desde_barra(jugador) and desde != 0:
            return False, "Debes mover fichas desde la barra primero"
        
        # Verificar punto de origen
        if desde > 0:
            if not self.celda[desde] or self.celda[desde][0] != jugador:
                return False, "No tienes fichas en ese punto"
        
        # Verificar distancia del movimiento
        if hasta <= 24:  # Movimiento normal (no salida)
            distancia = abs(hasta - desde)
            if distancia != dado:
                return False, f"Distancia incorrecta. Dado: {dado}, Movimiento: {distancia}"
            
            # Verificar dirección según jugador
            if jugador == "B" and hasta <= desde:
                return False, "Blancas solo pueden mover hacia puntos mayores"
            if jugador == "N" and hasta >= desde:
                return False, "Negras solo pueden mover hacia puntos menores"
            
            # Verificar punto destino (no puede tener 2+ fichas del oponente)
            if self.celda[hasta] and self.celda[hasta][0] != jugador and len(self.celda[hasta]) > 1:
                return False, "Punto bloqueado por el oponente"
        
        else:  # Salida (bear off)
            if not self.puede_sacar(jugador):
                return False, "No puedes sacar fichas todavía"
            
            if jugador == "B":
                distancia_necesaria = 25 - desde
            else:
                distancia_necesaria = desde
            
            if distancia_necesaria != dado:
                return False, f"Distancia incorrecta para salida. Dado: {dado}, Necesario: {distancia_necesaria}"
        
        return True, "Movimiento válido"

    def mover_ficha(self, desde, hasta, jugador):
        """
        Ejecuta un movimiento, manejando capturas si ocurren
        """
        # Mover desde barra
        if desde == 0:
            if jugador == "B" and self.barra_blancas:
                ficha = self.barra_blancas.pop()
            elif jugador == "N" and self.barra_negras:
                ficha = self.barra_negras.pop()
            else:
                return False, "No hay fichas en la barra"
        else:
            # Verificar captura en punto destino (SOLO si es movimiento normal, no salida)
            if hasta <= 24 and self.celda[hasta] and self.celda[hasta][0] != jugador and len(self.celda[hasta]) == 1:
                self.capturar_ficha(hasta)
            
            # SACAR la ficha del punto de origen (esta línea estaba mal indentada)
            ficha = self.celda[desde].pop()
        
        # Colocar ficha en destino
        if hasta <= 24:
            self.celda[hasta].append(ficha)
        else:
            if jugador == "B":
                self.fuera_blancas.append(ficha)
            else:
                self.fuera_negras.append(ficha)
        
        return True, "Movimiento exitoso"

    def capturar_ficha(self, punto):
        """Captura una ficha y la envía a la barra"""
        ficha_capturada = self.celda[punto].pop()
        if ficha_capturada == "B":
            self.barra_blancas.append("B")
        else:
            self.barra_negras.append("N")

    def puede_sacar(self, jugador):
        """
        Verifica si un jugador puede comenzar a sacar fichas
        Reglas: Todas las fichas deben estar en el cuadro de casa
        """
        # Verificar que no hay fichas en la barra
        if (jugador == "B" and self.barra_blancas) or (jugador == "N" and self.barra_negras):
            return False
        
        # Verificar que todas las fichas están en casa
        if jugador == "B":
            # Blancas: puntos 19-24 son casa
            casa_range = range(19, 25)
        else:
            # Negras: puntos 1-6 son casa
            casa_range = range(1, 7)
        
        for punto in range(1, 25):
            if punto not in casa_range and self.celda[punto] and self.celda[punto][0] == jugador:
                return False
        
        return True

    def win_conditions(self):
        """Verifica condiciones de victoria"""
        # Victoria por sacar todas las fichas
        if len(self.fuera_blancas) == 15:
            return True, "B"
        if len(self.fuera_negras) == 15:
            return True, "N"
        
        for i in range(1, 9):
            if (self.celda[i] and self.celda[i] == self.celda[i+1] == self.celda[i+2] == self.celda[i+3]):
                return True, self.celda[i][0]
        
        for i in range(13, 21):
            if (self.celda[i] and self.celda[i] == self.celda[i+1] == self.celda[i+2] == self.celda[i+3]):
                return True, self.celda[i][0]
        
        return False, None

# Ejemplo de uso
if __name__ == "__main__":
    tablero = board()
    tablero.mostrar_board()
    
    # Ejemplo: mover ficha blanca desde punto 6 al punto 7 con dado 1
    valido, mensaje = tablero.movimiento_valido(6, 7, "B", 1)
    if valido:
        tablero.mover_ficha(6, 7, "B")
        print("Movimiento exitoso!")
    else:
        print(f"Error: {mensaje}")
    
    tablero.mostrar_board()

decime unicamente si este codigo contiene para capturar fichas

#18
class board:
    def __init__(self):
        self.celda = {}
        self.celda[1] = ["N", "N"]
        self.celda[2] = []
        self.celda[3] = []
        self.celda[4] = []
        self.celda[5] = []
        self.celda[6] = ["B", "B", "B", "B", "B"]
        self.celda[7] = []
        self.celda[8] = ["N", "N", "N"]
        self.celda[9] = []
        self.celda[10] = []
        self.celda[11] = []
        self.celda[12] = ["B", "B", "B", "B", "B"]
        self.celda[13] = ["N", "N", "N", "N", "N"]
        self.celda[14] = []
        self.celda[15] = []
        self.celda[16] = []
        self.celda[17] = ["B", "B", "B"]
        self.celda[18] = []
        self.celda[19] = ["B", "B"]
        self.celda[20] = ["N", "N", "N"]
        self.celda[21] = []
        self.celda[22] = []
        self.celda[23] = []
        self.celda[24] = ["N", "N"]
        self.barra_blancas = []
        self.barra_negras = []
        self.fuera_blancas = []
        self.fuera_negras = []

    def mostrar_board(self):
        print(f"\nBarra Blancas: {self.barra_blancas} | Barra Negras: {self.barra_negras}")
        print(f"Fuera Blancas: {len(self.fuera_blancas)} | Fuera Negras: {len(self.fuera_negras)}")
        print(f"\n{self.celda[1]}|{self.celda[2]}|{self.celda[3]}|{self.celda[4]}|{self.celda[5]}|{self.celda[6]}|{self.celda[7]}|{self.celda[8]}|{self.celda[9]}|{self.celda[10]}|{self.celda[11]}|{self.celda[12]}")
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print("\n" + "|".join([" " * 15] * 12))
        print(f"\n{self.celda[13]}|{self.celda[14]}|{self.celda[15]}|{self.celda[16]}|{self.celda[17]}|{self.celda[18]}|{self.celda[19]}|{self.celda[20]}|{self.celda[21]}|{self.celda[22]}|{self.celda[23]}|{self.celda[24]}")

    def puede_mover_desde_barra(self, jugador):
        """Verifica si un jugador puede mover desde la barra"""
        if jugador == "B" and self.barra_blancas:
            return True
        if jugador == "N" and self.barra_negras:
            return True
        return False

    def movimiento_valido(self, desde, hasta, jugador, dado):
        """
        Valida si un movimiento es permitido según reglas de Backgammon
        
        Args:
            desde: punto de origen (1-24, 0 para barra)
            hasta: punto destino (1-24, 25 para sacar)
            jugador: "B" o "N"
            dado: valor del dado usado
        """
        # Verificar si el jugador tiene fichas en la barra (prioridad)
        if self.puede_mover_desde_barra(jugador) and desde != 0:
            return False, "Debes mover fichas desde la barra primero"
        
        # Verificar punto de origen
        if desde > 0:
            if not self.celda[desde] or self.celda[desde][0] != jugador:
                return False, "No tienes fichas en ese punto"
        
        # Verificar distancia del movimiento
        if hasta <= 24:  # Movimiento normal (no salida)
            distancia = abs(hasta - desde)
            if distancia != dado:
                return False, f"Distancia incorrecta. Dado: {dado}, Movimiento: {distancia}"
            
            # Verificar dirección según jugador
            if jugador == "B" and hasta <= desde:
                return False, "Blancas solo pueden mover hacia puntos mayores"
            if jugador == "N" and hasta >= desde:
                return False, "Negras solo pueden mover hacia puntos menores"
            
            # Verificar punto destino (no puede tener 2+ fichas del oponente)
            if self.celda[hasta] and self.celda[hasta][0] != jugador and len(self.celda[hasta]) > 1:
                return False, "Punto bloqueado por el oponente"
        
        else:  # Salida (bear off)
            if not self.puede_sacar(jugador):
                return False, "No puedes sacar fichas todavía"
            
            if jugador == "B":
                distancia_necesaria = 25 - desde
            else:
                distancia_necesaria = desde
            
            if distancia_necesaria != dado:
                return False, f"Distancia incorrecta para salida. Dado: {dado}, Necesario: {distancia_necesaria}"
        
        return True, "Movimiento válido"

    def mover_ficha(self, desde, hasta, jugador):
        """
        Ejecuta un movimiento, manejando capturas si ocurren
        """
        # Mover desde barra
        if desde == 0:
            if jugador == "B" and self.barra_blancas:
                ficha = self.barra_blancas.pop()
            elif jugador == "N" and self.barra_negras:
                ficha = self.barra_negras.pop()
            else:
                return False, "No hay fichas en la barra"
        else:
            # Verificar captura en punto destino (SOLO si es movimiento normal, no salida)
            if hasta <= 24 and self.celda[hasta] and self.celda[hasta][0] != jugador and len(self.celda[hasta]) == 1:
                self.capturar_ficha(hasta)
            
            # SACAR la ficha del punto de origen (esta línea estaba mal indentada)
            ficha = self.celda[desde].pop()
        
        # Colocar ficha en destino
        if hasta <= 24:
            self.celda[hasta].append(ficha)
        else:
            if jugador == "B":
                self.fuera_blancas.append(ficha)
            else:
                self.fuera_negras.append(ficha)
        
        return True, "Movimiento exitoso"

    def capturar_ficha(self, punto):
        """Captura una ficha y la envía a la barra"""
        ficha_capturada = self.celda[punto].pop()
        if ficha_capturada == "B":
            self.barra_blancas.append("B")
        else:
            self.barra_negras.append("N")

    def puede_sacar(self, jugador):
        """
        Verifica si un jugador puede comenzar a sacar fichas
        Reglas: Todas las fichas deben estar en el cuadro de casa
        """
        # Verificar que no hay fichas en la barra
        if (jugador == "B" and self.barra_blancas) or (jugador == "N" and self.barra_negras):
            return False
        
        # Verificar que todas las fichas están en casa
        if jugador == "B":
            # Blancas: puntos 19-24 son casa
            casa_range = range(19, 25)
        else:
            # Negras: puntos 1-6 son casa
            casa_range = range(1, 7)
        
        for punto in range(1, 25):
            if punto not in casa_range and self.celda[punto] and self.celda[punto][0] == jugador:
                return False
        
        return True

    def win_conditions(self):
        """Verifica condiciones de victoria"""
        # Victoria por sacar todas las fichas
        if len(self.fuera_blancas) == 15:
            return True, "B"
        if len(self.fuera_negras) == 15:
            return True, "N"
        
        for i in range(1, 9):
            if (self.celda[i] and self.celda[i] == self.celda[i+1] == self.celda[i+2] == self.celda[i+3]):
                return True, self.celda[i][0]
        
        for i in range(13, 21):
            if (self.celda[i] and self.celda[i] == self.celda[i+1] == self.celda[i+2] == self.celda[i+3]):
                return True, self.celda[i][0]
        
        return False, None

if __name__ == "__main__":
    tablero = board()
    tablero.mostrar_board()

este es mi codigo de tablero, y el que sigue es mi dice para los dados

import random
class dice:
    def tirar_dados():
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
                
            elif tirar in ['n', 'no']:
                print("Juego terminado")
                break
                
            else:
                print("Por favor responde 's' o 'n'")
                print()

    #el movimiento sera automatico
    def realizar_movimiento():

if __name__ == "__main__":
    dice.tirar_dados()

necesito nada mas que completes con las tirada de dado movimientos automaticos en base a la funcion de tablero.py que dice mover_ficha

#19
class board:
    def __init__(self):
        self.celda = {}
        self.celda[1] = ["N", "N"]
        self.celda[2] = []
        self.celda[3] = []
        self.celda[4] = []
        self.celda[5] = []
        self.celda[6] = ["B", "B", "B", "B", "B"]
        self.celda[7] = []
        self.celda[8] = ["N", "N", "N"]
        self.celda[9] = []
        self.celda[10] = []
        self.celda[11] = []
        self.celda[12] = ["B", "B", "B", "B", "B"]
        self.celda[13] = ["N", "N", "N", "N", "N"]
        self.celda[14] = []
        self.celda[15] = []
        self.celda[16] = []
        self.celda[17] = ["B", "B", "B"]
        self.celda[18] = []
        self.celda[19] = ["B", "B"]
        self.celda[20] = ["N", "N", "N"]
        self.celda[21] = []
        self.celda[22] = []
        self.celda[23] = []
        self.celda[24] = ["N", "N"]
        self.barra_blancas = []
        self.barra_negras = []
        self.fuera_blancas = []
        self.fuera_negras = []

    def mostrar_board(self):
        print(f"\nBarra Blancas: {self.barra_blancas} | Barra Negras: {self.barra_negras}")
        print(f"Fuera Blancas: {len(self.fuera_blancas)} | Fuera Negras: {len(self.fuera_negras)}")
        print(f"\n{self.celda[1]}|{self.celda[2]}|{self.celda[3]}|{self.celda[4]}|{self.celda[5]}|{self.celda[6]}|{self.celda[7]}|{self.celda[8]}|{self.celda[9]}|{self.celda[10]}|{self.celda[11]}|{self.celda[12]}")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print( "\n               |               |               |               |               |               |               |               |               |               |               |               |")
        print(f"\n{self.celda[13]}|{self.celda[14]}|{self.celda[15]}|{self.celda[16]}|{self.celda[17]}|{self.celda[18]}|{self.celda[19]}|{self.celda[20]}|{self.celda[21]}|{self.celda[22]}|{self.celda[23]}|{self.celda[24]}")

este es mi tablero, pero se ve las fichas hacia el costado y no como se ven en un backgammon real. podrias hacer que las fichas se vean como en un backgammon real?

#20
tengo en juego.py lo siguiente

from core import dice, jugador, tablero

class Juego:
    def movimiento_automatico():
        

el import es porque juego.py inicializa todo, y ademas hay que agregar en movimiento automatico que con dice.py en la funcion tirar_dados si sale por ejemplo 2 2 donde hay 2 fichas se suman 2 fichas. ok?

#21
mi codigo de backgammon es completo? respondeme por si o por no, gracias

#22
decime cuales son los ajustes menores? la integracion de modulos la entiendo como hacer