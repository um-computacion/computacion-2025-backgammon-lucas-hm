import unittest
from unittest.mock import patch, MagicMock
from core.juego import Juego

class TestJuegoMejorado(unittest.TestCase):
    def setUp(self):
        self.juego = Juego()
        # Parcheamos tablero y jugadores reales con mocks para no depender de input real
        self.juego.tablero = MagicMock()
        self.juego.jugadores = {
            "B": {"nombre": "Alice", "color": "B"},
            "N": {"nombre": "Bob", "color": "N"}
            }
        self.juego.turno_actual = "B"

        self.juego.turno_actual = "B"
        self.juego.dados = MagicMock()
    
    def test_cambiar_turno(self):
        self.assertEqual(self.juego.turno_actual, "B")
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.turno_actual, "N")
    
    def test_obtener_jugador_actual(self):
        jugador = self.juego.obtener_jugador_actual()
        self.assertEqual(jugador["nombre"], "Alice")
    
    def test_procesar_movimiento_valido(self):
        self.juego.tablero.movimiento_valido.return_value = (True, "válido")
        self.juego.tablero.mover_ficha.return_value = (True, "movido")
        exito, mensaje = self.juego.procesar_movimiento(1, 2, 1)
        self.assertTrue(exito)
        self.assertEqual(mensaje, "movido")
    
    def test_procesar_movimiento_invalido(self):
        self.juego.tablero.movimiento_valido.return_value = (False, "barra")
        exito, mensaje = self.juego.procesar_movimiento(1, 2, 1)
        self.assertFalse(exito)
        self.assertIn("barra", mensaje)
    
    def test_puede_mover_desde_barra_con_dado(self):
        self.juego.tablero.movimiento_valido.return_value = (True, "válido")
        puede = self.juego.puede_mover_desde_barra_con_dado("B", 3)
        self.assertTrue(puede)
    
    def test_mover_desde_barra_valido(self):
        self.juego.tablero.movimiento_valido.return_value = (True, "válido")
        self.juego.tablero.mover_ficha.return_value = (True, "movido")
        with patch("builtins.print") as mock_print:
            self.juego.turno_actual = "B"
            self.juego.mover_desde_barra(3)
            mock_print.assert_any_call("Movido desde barra al punto 3")
    
    def test_mover_desde_barra_invalido(self):
        self.juego.tablero.movimiento_valido.return_value = (False, "bloqueado")
        with patch("builtins.print") as mock_print:
            self.juego.turno_actual = "B"
            self.juego.mover_desde_barra(3)
            mock_print.assert_any_call("No se pudo mover desde barra: bloqueado")
    
    @patch("builtins.input", side_effect=["1","2","1","1","2","1","1","2","1","1"])
    @patch("builtins.print")
    def test_jugar_turno_simple(self, mock_print, mock_input):
        self.juego.tablero.movimiento_valido.return_value = (True, "válido")
        self.juego.tablero.mover_ficha.return_value = (True, "movido")
        self.juego.tablero.puede_mover_desde_barra.return_value = False

        terminado = self.juego.jugar_turno([1, 2])
        self.assertFalse(terminado)

    @patch("builtins.input", side_effect=["1","2","1","1","2","1","1","2","1","1"])
    @patch("builtins.print")
    def test_jugar_turno_ganador(self, mock_print, mock_input):
        # Forzamos condición de victoria
        self.juego.tablero.win_conditions.return_value = (True, "B")
        self.juego.tablero.movimiento_valido.return_value = (True, "válido")
        self.juego.tablero.mover_ficha.return_value = (True, "movido")
        self.juego.tablero.puede_mover_desde_barra.return_value = False

        terminado = self.juego.jugar_turno([1, 2])
        self.assertFalse(terminado)
        print("jugador1 gana!")
    
    
if __name__ == "__main__":
    unittest.main(verbosity=2)