import random, unittest
from unittest.mock import patch
from core.dice import Dice


class TestDice(unittest.TestCase):
    def setUp(self):
        random.seed(0)

    @patch("builtins.input", side_effect=["s"])
    @patch("random.randint", side_effect=[3, 5])
    def test_tirar_dados_normal(self, mock_randint, mock_input):
        dice = Dice()
        result = dice.tirar_dados()
        self.assertEqual(result, [3, 5])

    @patch("builtins.input", side_effect=["s"])
    @patch("random.randint", side_effect=[4, 4])
    def test_tirar_dados_dobles(self, mock_randint, mock_input):
        dice = Dice()
        result = dice.tirar_dados()
        self.assertEqual(result, [4, 4, 4, 4])

    @patch("builtins.input", side_effect=["n"])
    def test_tirar_dados_terminar_juego(self, mock_input):
        dice = Dice()
        result = dice.tirar_dados()
        self.assertIsNone(result)

    @patch("builtins.input", side_effect=["maybe", "s"])
    @patch("random.randint", side_effect=[2, 6])
    def test_tirar_dados_input_invalido(self, mock_randint, mock_input):
        dice = Dice()
        result = dice.tirar_dados()
        self.assertEqual(result, [2, 6])


if __name__ == "__main__":
    unittest.main()
