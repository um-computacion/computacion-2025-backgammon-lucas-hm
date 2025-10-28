import unittest
from core.tablero import board

class TestBoard(unittest.TestCase):

    def setUp(self):
        """Configuración inicial para cada test"""
        self.board = board()

    def test_initialization(self):
        """Test de inicialización correcta del tablero"""
        # Verificar que el tablero tiene 24 celdas
        self.assertEqual(len(self.board.celda), 24)
        # Verificar posiciones iniciales de fichas blancas
        self.assertEqual(self.board.celda[1], ["○", "○"])
        # Verificar posiciones iniciales de fichas negras
        self.assertEqual(self.board.celda[6], ["●", "●", "●", "●", "●"])
        self.assertEqual(self.board.celda[13], ["○", "○", "○", "○", "○"])
        # Verificar que barras y zonas de fuera están vacías al inicio
        self.assertEqual(self.board.barra_blancas, [])
        self.assertEqual(self.board.barra_negras, [])
        self.assertEqual(self.board.fuera_blancas, [])
        self.assertEqual(self.board.fuera_negras, [])

    def test_puede_mover_desde_barra(self):
        """Test para verificar si un jugador puede mover desde la barra"""
        # Verificar que inicialmente no se puede mover desde barra
        self.assertFalse(self.board.puede_mover_desde_barra("B"))
        self.assertFalse(self.board.puede_mover_desde_barra("N"))

        # Agregar fichas a la barra blanca y verificar
        self.board.barra_blancas = ["B", "B"]
        self.assertTrue(self.board.puede_mover_desde_barra("B"))
        self.assertFalse(self.board.puede_mover_desde_barra("N"))

        # Agregar fichas a la barra negra y verificar
        self.board.barra_negras = ["N"]
        self.assertTrue(self.board.puede_mover_desde_barra("N"))

    def test_movimiento_valido_blancas(self):
        """Test para movimientos válidos de fichas blancas"""
        # Movimiento válido para fichas blancas
        valido, mensaje = self.board.movimiento_valido(1, 3, "○", 2)
        self.assertTrue(valido)
        self.assertEqual(mensaje, "Movimiento válido")

        # Movimiento inválido: mismo punto
        valido, mensaje = self.board.movimiento_valido(1, 1, "○", 2)
        self.assertFalse(valido)

        # Movimiento inválido: distancia incorrecta
        valido, mensaje = self.board.movimiento_valido(1, 4, "○", 2)
        self.assertFalse(valido)

        # Movimiento inválido: punto bloqueado por oponente
        self.board.celda[3] = ["●", "●"]
        valido, _ = self.board.movimiento_valido(1, 3, "○", 2)
        self.assertFalse(valido)

    def test_movimiento_valido_negras(self):
        """Test para movimientos válidos de fichas negras"""
        # Configurar posición inicial para negras
        self.board.celda[24] = ["●", "●"]
        # Movimiento válido para fichas negras
        valido, mensaje = self.board.movimiento_valido(24, 22, "●", 2)
        self.assertTrue(valido)
        # Movimiento inválido: dirección incorrecta para negras
        valido, _ = self.board.movimiento_valido(24, 25, "●", 2)
        self.assertFalse(valido)

    def test_mover_ficha_normal(self):
        """Test para mover ficha sin captura"""
        resultado, _ = self.board.mover_ficha(1, 3, "B")
        self.assertTrue(resultado)
        # Verificar que la ficha se movió correctamente
        self.assertEqual(self.board.celda[1], ["○"])
        self.assertIn("○", self.board.celda[3])

    def test_mover_ficha_con_captura(self):
        """Test para mover ficha con captura de ficha oponente"""
        # Configurar posición con ficha negra que será capturada
        self.board.celda[3] = ["●"]
        self.board.celda[1] = ["○", "○"]
        resultado, _ = self.board.mover_ficha(1, 3, "B")
        self.assertTrue(resultado)
        # Verificar captura
        self.assertEqual(self.board.celda[3], ["○"])
        self.assertEqual(self.board.barra_negras, ["N"])

    def test_mover_desde_barra(self):
        """Test para mover ficha desde la barra"""
        self.board.barra_blancas = ["B"]
        resultado, _ = self.board.mover_ficha(0, 1, "B")
        self.assertTrue(resultado)
        # Verificar que la ficha salió de la barra
        self.assertEqual(self.board.barra_blancas, [])
        self.assertIn("○", self.board.celda[1] or self.board.celda[0])

    def test_puede_sacar(self):
        """Test para verificar si un jugador puede sacar fichas"""
        # Verificar condiciones iniciales
        self.assertTrue(self.board.puede_sacar("B"))
        self.assertTrue(self.board.puede_sacar("N"))

        # Configurar tablero para prueba de sacar fichas
        for i in range(1, 19):
            self.board.celda[i] = []
        self.board.celda[19] = ["○"] * 15
        self.assertTrue(self.board.puede_sacar("B"))

    def test_puede_sacar_con_barra(self):
        """Test para verificar que no se puede sacar con fichas en barra"""
        # Configurar tablero pero con ficha en barra
        for i in range(1, 19):
            self.board.celda[i] = []
        self.board.celda[19] = ["○"] * 14
        self.board.barra_blancas = ["B"]
        self.assertFalse(self.board.puede_sacar("B"))

    def test_movimiento_salida_valido(self):
        """Test para movimiento de salida válido"""
        # Configurar tablero para salida
        for i in range(1, 19):
            self.board.celda[i] = []
        self.board.celda[20] = ["○"] * 5
        valido, _ = self.board.movimiento_valido(20, 25, "B", 5)
        self.assertTrue(valido)

    def test_win_conditions(self):
        """Test para condiciones de victoria por fichas fuera"""
        # Verificar que inicialmente no hay ganador
        ganador, jugador = self.board.win_conditions()
        self.assertFalse(ganador)

        # Simular victoria de blancas
        self.board.fuera_blancas = ["○"] * 15
        ganador, jugador = self.board.win_conditions()
        self.assertTrue(ganador)
        self.assertEqual(jugador, "B")

        # Simular victoria de negras
        self.board.fuera_blancas = []
        self.board.fuera_negras = ["●"] * 15
        ganador, jugador = self.board.win_conditions()
        self.assertTrue(ganador)
        self.assertEqual(jugador, "N")

    def test_win_conditions_4_consecutivas(self):
        """Test para condiciones de victoria por 4 fichas consecutivas"""
        # Configurar 4 fichas blancas consecutivas
        for i in range(1, 5):
            self.board.celda[i] = ["○"]
        ganador, jugador = self.board.win_conditions()
        self.assertTrue(ganador)
        self.assertEqual(jugador, "○")

        # Configurar 4 fichas negras consecutivas
        for i in range(1, 25):
            self.board.celda[i] = []
        for i in range(13, 17):
            self.board.celda[i] = ["●"]
        ganador, jugador = self.board.win_conditions()
        self.assertTrue(ganador)
        self.assertEqual(jugador, "●")

    def test_movimiento_invalido_punto_vacio(self):
        """Test para movimiento desde punto vacío"""
        valido, mensaje = self.board.movimiento_valido(2, 4, "B", 2)
        self.assertFalse(valido)
        self.assertIn("no tienes fichas", mensaje.lower())

    def test_movimiento_invalido_ficha_oponente(self):
        """Test para movimiento de ficha del oponente"""
        valido, mensaje = self.board.movimiento_valido(6, 8, "B", 2)
        self.assertFalse(valido)
        self.assertIn("no tienes fichas", mensaje.lower())

    def test_capturar_ficha(self):
        """Test para captura manual de ficha"""
        self.board.celda[5] = ["●"]
        self.board.capturar_ficha(5)
        # Verificar que la ficha fue capturada y enviada a la barra
        self.assertEqual(self.board.celda[5], [])
        self.assertEqual(self.board.barra_negras, ["N"])

    def test_movimiento_desde_barra_bloqueado(self):
        """Test para movimiento desde barra a punto bloqueado"""
        self.board.barra_blancas = ["B"]
        # Punto 2 bloqueado con 2 fichas negras
        self.board.celda[2] = ["●", "●"]
        valido, mensaje = self.board.movimiento_valido(0, 2, "B", 2)
        self.assertFalse(valido)
        self.assertIn("bloqueado", mensaje.lower())

    def test_movimiento_desde_barra_valido_negras(self):
        """Test para movimiento válido desde barra de negras"""
        self.board.barra_negras = ["N"]
        self.board.celda[24] = []  # aseguramos que no esté bloqueado
        valido, mensaje = self.board.movimiento_valido(0, 24, "N", 1)
        self.assertTrue(valido)
        self.assertIn("barra", mensaje.lower())

    def test_movimiento_direccion_incorrecta(self):
        """Test para movimientos en dirección incorrecta"""
        # Blancas intentando mover hacia puntos menores
        valido, mensaje = self.board.movimiento_valido(1, 0, "B", 1)
        self.assertFalse(valido)
        self.assertIn("blancas", mensaje.lower())

        # Negras intentando mover hacia puntos mayores
        self.board.celda[23] = ["●", "●"]
        valido, mensaje = self.board.movimiento_valido(23, 24, "N", 1)
        self.assertFalse(valido)
        self.assertIn("negras", mensaje.lower())

    def test_movimiento_distancia_incorrecta(self):
        """Test para movimiento con distancia incorrecta"""
        valido, mensaje = self.board.movimiento_valido(1, 4, "B", 2)
        self.assertFalse(valido)
        self.assertIn("distancia", mensaje.lower())

    def test_salida_invalida_fichas_fuera_casa(self):
        """Test para salida inválida cuando hay fichas fuera de casa"""
        # Blancas tienen fichas fuera de casa
        self.board.celda[1] = ["○"] * 2
        valido, mensaje = self.board.movimiento_valido(1, 25, "B", 1)
        self.assertFalse(valido)
        self.assertIn("sacar", mensaje.lower())

    def test_mover_ficha_captura_manual(self):
        """Test manual para mover ficha con captura"""
        self.board.celda[4] = ["●"]
        self.board.celda[1] = ["○"]
        resultado, _ = self.board.mover_ficha(1, 4, "B")
        self.assertTrue(resultado)
        # Verificar captura y movimiento
        self.assertEqual(self.board.celda[4], ["○"])
        self.assertEqual(self.board.barra_negras, ["N"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
