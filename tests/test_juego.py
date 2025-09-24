import unittest
from unittest.mock import MagicMock, patch
from core.juego import Juego

class TestJuego(unittest.TestCase):
    def setUp(self):
        # Parcheamos las dependencias externas
        patcher_dice = patch('core.juego.Dice')
        patcher_board = patch('core.juego.board')
        patcher_jugador = patch('core.juego.jugador')

        self.mock_dice = patcher_dice.start()
        self.mock_board = patcher_board.start()
        self.mock_jugador = patcher_jugador.start()

        self.addCleanup(patcher_dice.stop)
        self.addCleanup(patcher_board.stop)
        self.addCleanup(patcher_jugador.stop)

        # Configuramos mocks
        self.mock_dice.return_value.tirar_dados.return_value = [3, 5]
        self.mock_board.return_value.movimiento_valido.return_value = (True, "válido")
        self.mock_board.return_value.mover_ficha.return_value = (True, "movido")
        self.mock_board.return_value.win_conditions.return_value = (False, None)
        self.mock_board.return_value.puede_mover_desde_barra.return_value = False
        self.mock_board.return_value.mostrar_board = MagicMock()

        self.mock_jugador.return_value.nombre1 = "Alice"
        self.mock_jugador.return_value.nombre2 = "Bob"
        self.mock_jugador.return_value.color1 = "B"
        self.mock_jugador.return_value.color2 = "N"

        self.juego = Juego()

    def test_inicializar_jugadores(self):
        jugadores = self.juego.jugadores
        self.assertEqual(jugadores["B"]["nombre"], "Alice")
        self.assertEqual(jugadores["N"]["nombre"], "Bob")

    def test_cambiar_turno(self):
        self.assertEqual(self.juego.turno_actual, "B")
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.turno_actual, "N")

    def test_obtener_jugador_actual(self):
        jugador = self.juego.obtener_jugador_actual()
        self.assertEqual(jugador["nombre"], "Alice")
        self.assertEqual(jugador["color"], "B")

    def test_procesar_movimiento_valido(self):
        exito, mensaje = self.juego.procesar_movimiento(1, 4, 3)
        self.assertTrue(exito)
        self.assertEqual(mensaje, "movido")

    def test_puede_mover_desde_barra_con_dado(self):
        self.mock_board.return_value.movimiento_valido.return_value = (True, "")
        puede = self.juego.puede_mover_desde_barra_con_dado("B", 4)
        self.assertTrue(puede)

    @patch('builtins.print')
    def test_mover_desde_barra(self, mock_print):
        self.juego.turno_actual = "B"
        self.juego.mover_desde_barra(3)
        mock_print.assert_any_call("Movido desde barra al punto 3")

    @patch('builtins.input', side_effect=["1", "4", "3"])
    @patch('builtins.print')
    def test_jugar_turno(self, mock_print, mock_input):
        terminado = self.juego.jugar_turno([3, 5])
        self.assertFalse(terminado)

if __name__ == "__main__":
    unittest.main()
