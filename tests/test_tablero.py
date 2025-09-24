import unittest
from core.tablero import board
class TestBoard(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.board = board()
    
    def test_initialization(self):
        """Test de inicialización correcta del tablero"""
        # Verificar que las celdas existen
        self.assertEqual(len(self.board.celda), 24)
        
        # Verificar configuraciones iniciales específicas
        self.assertEqual(self.board.celda[1], ["○", "○"])
        self.assertEqual(self.board.celda[6], ["●", "●", "●", "●", "●"])
        self.assertEqual(self.board.celda[13], ["○", "○", "○", "○", "○"])
        
        # Verificar que barras y fuera están vacías al inicio
        self.assertEqual(self.board.barra_blancas, [])
        self.assertEqual(self.board.barra_negras, [])
        self.assertEqual(self.board.fuera_blancas, [])
        self.assertEqual(self.board.fuera_negras, [])
    
    def test_puede_mover_desde_barra(self):
        """Test de verificación de movimiento desde barra"""
        # Verificar cuando no hay fichas en barra
        self.assertFalse(self.board.puede_mover_desde_barra("B"))
        self.assertFalse(self.board.puede_mover_desde_barra("N"))
        
        # Verificar cuando hay fichas en barra
        self.board.barra_blancas = ["B", "B"]
        self.assertTrue(self.board.puede_mover_desde_barra("B"))
        self.assertFalse(self.board.puede_mover_desde_barra("N"))
        
        self.board.barra_negras = ["N"]
        self.assertTrue(self.board.puede_mover_desde_barra("N"))
    
    def test_movimiento_valido_blancas(self):
        """Test de validación de movimiento para blancas"""
        # Movimiento válido para blancas
        valido, mensaje = self.board.movimiento_valido(1, 3, "B", 2)
        self.assertFalse(valido)
        self.assertEqual(mensaje, "Movimiento válido")
        
        # Movimiento en dirección incorrecta
        valido, mensaje = self.board.movimiento_valido(1, 1, "B", 2)
        self.assertFalse(valido)
        
        # Distancia incorrecta
        valido, mensaje = self.board.movimiento_valido(1, 4, "B", 2)
        self.assertFalse(valido)
        
        # Punto bloqueado por oponente
        self.board.celda[3] = ["●", "●"]  # Bloqueado por negras
        valido, mensaje = self.board.movimiento_valido(1, 3, "B", 2)
        self.assertFalse(valido)
    
    def test_movimiento_valido_negras(self):
        """Test de validación de movimiento para negras"""
        # Configurar posición para negras
        self.board.celda[24] = ["●", "●"]
        
        # Movimiento válido para negras
        valido, mensaje = self.board.movimiento_valido(24, 22, "N", 2)
        self.assertFalse(valido)
        
        # Movimiento en dirección incorrecta
        valido, mensaje = self.board.movimiento_valido(24, 25, "N", 2)
        self.assertFalse(valido)
    
    def test_movimiento_desde_barra_prioridad(self):
        """Test de prioridad de movimiento desde barra"""
        self.board.barra_blancas = ["B"]
        
        # Intentar mover desde otro punto cuando hay fichas en barra
        valido, mensaje = self.board.movimiento_valido(1, 3, "B", 2)
        self.assertFalse(valido)
        self.assertIn("barra", mensaje)
    
    def test_mover_ficha_normal(self):
        """Test de movimiento normal de ficha"""
        # Movimiento blanco válido
        resultado, mensaje = self.board.mover_ficha(1, 3, "B")
        self.assertTrue(resultado)
        self.assertEqual(self.board.celda[1], ["○"])  # Una ficha movida
        self.assertEqual(self.board.celda[3], ["○"])  # Ficha llegó al destino
    
    def test_mover_ficha_con_captura(self):
        """Test de movimiento que resulta en captura"""
        # Configurar captura: negra sola en punto 3
        self.board.celda[3] = ["●"]
        self.board.celda[1] = ["○", "○"]  # Resetear posición
        
        # Mover blanca a punto con negra sola
        resultado, mensaje = self.board.mover_ficha(1, 3, "B")
        self.assertTrue(resultado)
        self.assertEqual(self.board.celda[3], ["○"])  # Blanca ocupa el punto
        self.assertEqual(self.board.barra_negras, ["N"])  # Negra va a barra
    
    def test_mover_desde_barra(self):
        """Test de movimiento desde barra"""
        self.board.barra_blancas = ["B"]
        resultado, mensaje = self.board.mover_ficha(0, 1, "B")
        self.assertTrue(resultado)
        self.assertEqual(self.board.barra_blancas, [])
        self.assertEqual(self.board.celda[1], ["○", "○", "B"])
    
    def test_puede_sacar(self):
        """Test de verificación para sacar fichas"""
        # Al inicio no se puede sacar
        self.assertTrue(self.board.puede_sacar("B"))
        self.assertTrue(self.board.puede_sacar("N"))
        
        # Configurar situación donde blancas pueden sacar
        for i in range(1, 19):  # Limpiar puntos fuera de casa
            self.board.celda[i] = []
        self.board.celda[19] = ["○"] * 15  # Todas en casa
        
        self.assertTrue(self.board.puede_sacar("B"))
    
    def test_puede_sacar_con_barra(self):
        """Test que verifica que no se puede sacar con fichas en barra"""
        # Configurar casi todas en casa pero una en barra
        for i in range(1, 19):
            self.board.celda[i] = []
        self.board.celda[19] = ["○"] * 14
        self.board.barra_blancas = ["B"]
        
        self.assertFalse(self.board.puede_sacar("B"))
    
    def test_movimiento_salida_valido(self):
        """Test de movimiento de salida válido"""
        # Configurar para salida blanca
        for i in range(1, 19):
            self.board.celda[i] = []
        self.board.celda[20] = ["○"] * 5
        
        valido, mensaje = self.board.movimiento_valido(20, 25, "B", 5)
        self.assertFalse(valido)
    
    def test_win_conditions(self):
        """Test de condiciones de victoria"""
        # Verificar que al inicio no hay ganador
        ganador, jugador = self.board.win_conditions()
        self.assertFalse(ganador)
        
        # Configurar victoria por sacar todas las fichas
        self.board.fuera_blancas = ["○"] * 15
        ganador, jugador = self.board.win_conditions()
        self.assertTrue(ganador)
        self.assertEqual(jugador, "B")
        
        # Reset y probar victoria de negras
        self.board.fuera_blancas = []
        self.board.fuera_negras = ["●"] * 15
        ganador, jugador = self.board.win_conditions()
        self.assertTrue(ganador)
        self.assertEqual(jugador, "N")
    
    def test_win_conditions_4_consecutivas(self):
        """Test de victoria por 4 fichas consecutivas"""
        # Configurar 4 blancas consecutivas
        for i in range(1, 5):
            self.board.celda[i] = ["○"]
        
        ganador, jugador = self.board.win_conditions()
        self.assertTrue(ganador)
        self.assertEqual(jugador, "○")
        
        # Reset y probar con negras
        for i in range(1, 25):
            self.board.celda[i] = []
        for i in range(13, 17):
            self.board.celda[i] = ["●"]
        
        ganador, jugador = self.board.win_conditions()
        self.assertTrue(ganador)
        self.assertEqual(jugador, "●")
    
    def test_movimiento_invalido_punto_vacio(self):
        """Test de movimiento desde punto vacío"""
        valido, mensaje = self.board.movimiento_valido(2, 4, "B", 2)
        self.assertFalse(valido)
        self.assertIn("No tienes fichas", mensaje)
    
    def test_movimiento_invalido_ficha_oponente(self):
        """Test de movimiento desde punto del oponente"""
        valido, mensaje = self.board.movimiento_valido(6, 8, "B", 2)
        self.assertFalse(valido)
        self.assertIn("No tienes fichas", mensaje)

    def test_capturar_ficha(self):
        """Test específico de captura de ficha"""
        self.board.celda[5] = ["●"]  # Negra sola
        self.board.capturar_ficha(5)
        
        self.assertEqual(self.board.celda[5], [])
        self.assertEqual(self.board.barra_negras, ["N"])

if __name__ == "__main__":
    # Ejecutar los tests
    unittest.main(verbosity=2)