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
