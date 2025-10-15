import unittest
from unittest.mock import patch
from core.jugador import Jugador


class TestJugador(unittest.TestCase):
    @patch("builtins.input", side_effect=["Alice", "Bob", "1", "2"])
    def test_datos_blancas(self, mock_input):
        player = jugador()
        player.datos(barra=0, fichas_sacadas=0)
        self.assertEqual(player.nombre1, "Alice")
        self.assertEqual(player.nombre2, "Bob")
        self.assertEqual(player.color1, "○")
        self.assertEqual(player.color2, "●")
        self.assertEqual(player.barra, 0)
        self.assertEqual(player.fichas_sacadas, 0)

    @patch("builtins.input", side_effect=["Carlos", "Diana", "2", "1"])
    def test_datos_negras(self, mock_input):
        player = jugador()
        player.datos(barra=5, fichas_sacadas=3)
        self.assertEqual(player.nombre1, "Carlos")
        self.assertEqual(player.nombre2, "Diana")
        self.assertEqual(player.color1, "●")
        self.assertEqual(player.color2, "○")
        self.assertEqual(player.barra, 5)
        self.assertEqual(player.fichas_sacadas, 3)


if __name__ == "__main__":
    unittest.main()
