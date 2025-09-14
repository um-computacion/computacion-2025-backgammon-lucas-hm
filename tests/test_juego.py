import unittest
from unittest.mock import MagicMock, patch
from core.juego import Juego

class TestJuego(unittest.TestCase):

    @patch("Juego.jugador")
    @patch("Juego.board")
    @patch("Juego.Dice")
    def setUp(self, mock_dice, mock_board, mock_jugador):
        # Mock de jugador
        mock_jugador.return_value.nombre1 = "Lucas"
        mock_jugador.return_value.nombre2 = "AI"
        mock_jugador.return_value.color1 = "B"
        mock_jugador.return_value.color2 = "N"

        # Mock de tablero
        self.mock_tablero = mock_board.return_value
        self.mock_tablero.movimiento_valido.return_value = (True, "Movimiento válido")
        self.mock_tablero.mover_ficha.return_value = (True, "Movimiento exitoso")
        self.mock_tablero.puede_mover_desde_barra.return_value = False
        self.mock_tablero.win_conditions.return_value = (False, None)

        # Mock de dados
        mock_dice.return_value.tirar_dados.return_value = (3, 5)

        self.juego = Juego()

    def test_inicializar_jugadores(self):
        self.assertEqual(self.juego.jugadores["B"]["nombre"], "Lucas")
        self.assertEqual(self.juego.jugadores["N"]["nombre"], "AI")

    def test_cambiar_turno(self):
        self.assertEqual(self.juego.turno_actual, "B")
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.turno_actual, "N")

    def test_obtener_jugador_actual(self):
        jugador = self.juego.obtener_jugador_actual()
        self.assertEqual(jugador["nombre"], "Lucas")
        self.juego.cambiar_turno()
        jugador = self.juego.obtener_jugador_actual()
        self.assertEqual(jugador["nombre"], "AI")

    def test_procesar_movimiento_valido(self):
        exito, mensaje = self.juego.procesar_movimiento(13, 14, 1)
        self.assertTrue(exito)
        self.assertEqual(mensaje, "Movimiento exitoso")

    def test_puede_mover_desde_barra_con_dado(self):
        self.mock_tablero.movimiento_valido.return_value = (True, "")
        self.assertTrue(self.juego.puede_mover_desde_barra_con_dado("B", 3))
        self.assertTrue(self.juego.puede_mover_desde_barra_con_dado("N", 3))

    def test_mover_desde_barra(self):
        self.juego.turno_actual = "B"
        self.juego.procesar_movimiento = MagicMock(return_value=(True, "OK"))
        self.juego.mover_desde_barra(3)
        self.juego.procesar_movimiento.assert_called_with(0, 3, 3)

        self.juego.turno_actual = "N"
        self.juego.mover_desde_barra(4)
        self.juego.procesar_movimiento.assert_called_with(0, 21, 4)

    def test_jugar_turno_sin_victoria(self):
        self.mock_tablero.puede_mover_desde_barra.return_value = False
        with patch("builtins.input", side_effect=["13", "14", "3"]):
            terminado = self.juego.jugar_turno((3, 5))
            self.assertFalse(terminado)

    def test_jugar_turno_con_victoria(self):
        self.mock_tablero.win_conditions.return_value = (True, "B")
        with patch("builtins.input", side_effect=["13", "14", "3"]):
            terminado = self.juego.jugar_turno((3, 5))
            self.assertTrue(terminado)

if __name__ == "__main__":
    unittest.main()
