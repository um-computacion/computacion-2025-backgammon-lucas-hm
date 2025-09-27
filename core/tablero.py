class board:
    def __init__(self):
        self.celda = {}
        self.celda[1] = ["○", "○"]
        self.celda[2] = []
        self.celda[3] = []
        self.celda[4] = []
        self.celda[5] = []
        self.celda[6] = ["●", "●", "●", "●", "●"]
        self.celda[7] = []
        self.celda[8] = ["○", "○", "○"]
        self.celda[9] = []
        self.celda[10] = []
        self.celda[11] = []
        self.celda[12] = ["●", "●", "●", "●", "●"]
        self.celda[13] = ["○", "○", "○", "○", "○"]
        self.celda[14] = []
        self.celda[15] = []
        self.celda[16] = []
        self.celda[17] = ["●", "●", "●"]
        self.celda[18] = []
        self.celda[19] = ["●", "●"]
        self.celda[20] = ["○", "○", "○"]
        self.celda[21] = []
        self.celda[22] = []
        self.celda[23] = []
        self.celda[24] = ["○", "○"]
        self.barra_blancas = []
        self.barra_negras = []
        self.fuera_blancas = []
        self.fuera_negras = []

    def mostrar_board(self):
        print(f"\nBarra Blancas: {self.barra_blancas} | Barra Negras: {self.barra_negras}")
        print(f"Fuera Blancas: {len(self.fuera_blancas)} | Fuera Negras: {len(self.fuera_negras)}")
        for i in range(1, 25):
            print(f"{i}: {self.celda[i]}")

    def puede_mover_desde_barra(self, jugador):
        if jugador == "B" and self.barra_blancas:
            return True
        if jugador == "N" and self.barra_negras:
            return True
        return False

    def puede_sacar(self, jugador):
        if (jugador == "B" and self.barra_blancas) or (jugador == "N" and self.barra_negras):
            return False

        casa = range(19, 25) if jugador == "B" else range(1, 7)
        for punto in range(1, 25):
            if punto not in casa and self.celda[punto] and self.celda[punto][0] == jugador:
                return False
        return True

    def movimiento_valido(self, desde, hasta, jugador, dado):
        """
        Valida un movimiento según reglas de Backgammon.

        Args:
            desde: punto de origen (1-24, 0 para barra)
            hasta: punto destino (1-24, 25 para sacar)
            jugador: "B" o "N"
            dado: valor del dado usado
        Returns:
            Tuple (bool, str) -> True/False y mensaje explicativo
        """

        # 1️⃣ Prioridad: si hay fichas en barra, solo se pueden mover desde barra
        if self.puede_mover_desde_barra(jugador) and desde != 0:
            return False, "Debes mover fichas desde la barra primero"

        # 2️⃣ Movimiento desde barra
        if desde == 0:
            if jugador == "B":
                destino_correcto = dado  # Blancas entran desde izquierda
            else:
                destino_correcto = 25 - dado  # Negras entran desde derecha

            if hasta != destino_correcto:
                return False, f"Debes entrar desde la barra al punto {destino_correcto}"

            # Verificar si punto destino está bloqueado
            if self.celda[hasta] and self.celda[hasta][0] != jugador and len(self.celda[hasta]) > 1:
                return False, "Punto bloqueado por el oponente"

            return True, "Movimiento válido desde barra"

        # 3️⃣ Salida de fichas (bear off)
        if hasta == 25:
            if not self.puede_sacar(jugador):
                return False, "No puedes sacar fichas todavía"
            # Verificar distancia correcta para salida
            distancia_necesaria = (25 - desde) if jugador == "B" else desde
            if distancia_necesaria != dado:
                return False, f"Distancia incorrecta para sacar ficha. Dado: {dado}, Necesario: {distancia_necesaria}"
            return True, "Movimiento válido de salida"

        # 4️⃣ Verificar existencia de ficha en punto de origen
        if not self.celda[desde] or (jugador == "B" and self.celda[desde][0] != "○") or (jugador == "N" and self.celda[desde][0] != "●"):
            return False, "No tienes fichas en ese punto"

        # 5️⃣ Validar dirección del movimiento
        if jugador == "B" and hasta <= desde:
            return False, "Blancas solo pueden mover hacia puntos mayores"
        if jugador == "N" and hasta >= desde:
            return False, "Negras solo pueden mover hacia puntos menores"

        # 6️⃣ Validar distancia correcta
        distancia = abs(hasta - desde)
        if distancia != dado:
            return False, f"Distancia incorrecta. Dado: {dado}, Movimiento: {distancia}"

        # 7️⃣ Verificar si punto destino está bloqueado
        if self.celda[hasta] and self.celda[hasta][0] != jugador and len(self.celda[hasta]) > 1:
            return False, "Punto bloqueado por el oponente"

        return True, "Movimiento válido"

    def mover_ficha(self, desde, hasta, jugador):
        # Mover desde barra
        if desde == 0:
            if jugador == "B" and self.barra_blancas:
                ficha = self.barra_blancas.pop()
            elif jugador == "N" and self.barra_negras:
                ficha = self.barra_negras.pop()
            else:
                return False, "No hay fichas en la barra"
        else:
            # Captura
            if hasta <= 24 and self.celda[hasta] and self.celda[hasta][0] != jugador and len(self.celda[hasta]) == 1:
                self.capturar_ficha(hasta)
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
        ficha_capturada = self.celda[punto].pop()
        if ficha_capturada == "B":
            self.barra_blancas.append("B")
        else:
            self.barra_negras.append("N")

    def win_conditions(self):
        if len(self.fuera_blancas) == 15:
            return True, "B"
        if len(self.fuera_negras) == 15:
            return True, "N"

        # 4 fichas consecutivas (blancas o negras)
        for i in range(1, 22):
            if all(self.celda[i + j] and self.celda[i + j] == self.celda[i] for j in range(4)):
                return True, self.celda[i][0]

        return False, None
