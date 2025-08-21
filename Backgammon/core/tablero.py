#hacer movimientos, reglas de salida, condiciones de victoria y sistema de captura
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

        self.celda[19] = ["B", "B", "B", "B", "B"]

        self.celda[20] = []
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

if __name__ == "__main__":
    tablero = board()
    tablero.mostrar_board()