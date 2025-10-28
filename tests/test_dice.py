"""Tests unitarios para la clase Dice del módulo core.dice"""

import random
import unittest
from unittest.mock import patch
from core.dice import Dice


class TestDice(unittest.TestCase):
    """Pruebas para el método tirar_dados de la clase Dice"""

    def setUp(self):
        """Inicializa la semilla de random para consistencia"""
        random.seed(0)

    @patch("builtins.input", side_effect=["s"])
    @patch("random.randint", side_effect=[3, 5])
    def test_tirar_dados_normal(self, mock_randint, mock_input):
        """Verifica que se devuelven dos valores distintos"""
        dice = Dice()
        result = dice.tirar_dados()
        self.assertEqual(result, [3, 5])

    @patch("builtins.input", side_effect=["s"])
    @patch("random.randint", side_effect=[4, 4])
    def test_tirar_dados_dobles(self, mock_randint, mock_input):
        """Verifica que se duplican los dados si son iguales"""
        dice = Dice()
        result = dice.tirar_dados()
        self.assertEqual(result, [4, 4, 4, 4])

    @patch("builtins.input", side_effect=["n"])
    def test_tirar_dados_terminar_juego(self, mock_input):
        """Verifica que se retorna None si el usuario elige no tirar"""
        dice = Dice()
        result = dice.tirar_dados()
        self.assertIsNone(result)

    @patch("builtins.input", side_effect=["maybe", "s"])
    @patch("random.randint", side_effect=[2, 6])
    def test_tirar_dados_input_invalido(self, mock_randint, mock_input):
        """Verifica que se repite el input hasta recibir 's'"""
        dice = Dice()
        result = dice.tirar_dados()
        self.assertEqual(result, [2, 6])


if __name__ == "__main__":
    unittest.main()
