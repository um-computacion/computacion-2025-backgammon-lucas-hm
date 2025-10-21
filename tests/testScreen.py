"""Tests unitarios para la clase Screen del módulo pygame_ui.screen"""

import unittest
from unittest.mock import patch, MagicMock
import pygame

from pygame_ui.screen import Screen


class TestScreen(unittest.TestCase):
    """Pruebas para la clase Screen que gestiona la interfaz gráfica del Backgammon"""

    @patch("pygame.image.load")
    @patch("pygame.display.set_mode")
    @patch("pygame.font.SysFont")
    @patch("pygame.transform.scale")
    def setUp(self, mock_scale, mock_font, mock_display, mock_image_load):
        """Inicializa Screen con recursos gráficos simulados"""
        mock_img = MagicMock()  # No uses spec=pygame.Surface
        mock_image_load.return_value = mock_img
        mock_scale.return_value = mock_img
        mock_display.return_value = MagicMock()
        mock_font.return_value = MagicMock()

        self.screen = Screen()

    def test_inicializar_fichas(self):
        """Verifica que las posiciones iniciales tengan las fichas correctas"""
        self.assertEqual(self.screen.posiciones[1][0][1], 3)
        self.assertEqual(self.screen.posiciones[2][0][1], 5)
        self.assertEqual(self.screen.posiciones[20][0][1], 5)
        self.assertEqual(self.screen.posiciones[24][0][1], 2)

    def test_tirar_dados_valores_validos(self):
        """Verifica que los valores de los dados estén dentro del rango esperado"""
        for _ in range(100):
            d1, d2, jugadas = self.screen._tirar_dados()
            self.assertIn(d1, range(1, 7))
            self.assertIn(d2, range(1, 7))
            self.assertIn(jugadas, [2, 4])
            if d1 == d2:
                self.assertEqual(jugadas, 4)
            else:
                self.assertEqual(jugadas, 2)

    def test_coords_generadas_correctamente(self):
        """Verifica que las coordenadas del tablero estén correctamente generadas"""
        self.assertEqual(len(self.screen.coords), 24)
        for i in range(1, 25):
            self.assertIsInstance(self.screen.coords[i], tuple)
            self.assertEqual(len(self.screen.coords[i]), 2)

    def test_dados_imgs_cargados(self):
        """Verifica que se hayan cargado las imágenes de los dados"""
        self.assertEqual(len(self.screen.dados_imgs), 6)
        for img in self.screen.dados_imgs:
            self.assertTrue(isinstance(img, MagicMock))


if __name__ == "__main__":
    unittest.main()

