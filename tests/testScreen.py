import unittest
from unittest.mock import patch, MagicMock
import pygame
import random

from tu_modulo import Screen  # Reemplazá 'tu_modulo' por el nombre real del archivo .py

class TestScreen(unittest.TestCase):

    @patch("pygame.image.load")
    @patch("pygame.display.set_mode")
    @patch("pygame.font.SysFont")
    def setUp(self, mock_font, mock_display, mock_image_load):
        # Mockeo imágenes para evitar cargar archivos reales
        mock_image = MagicMock(spec=pygame.Surface)
        mock_image_load.return_value = mock_image
        mock_display.return_value = MagicMock()
        mock_font.return_value = MagicMock()

        self.screen = Screen()

    def test_inicializar_fichas(self):
        # Verifica que las posiciones iniciales tengan las fichas correctas
        self.assertEqual(self.screen.posiciones[1][0][1], 3)
        self.assertEqual(self.screen.posiciones[2][0][1], 5)
        self.assertEqual(self.screen.posiciones[20][0][1], 5)
        self.assertEqual(self.screen.posiciones[24][0][1], 2)

    def test_tirar_dados_valores_validos(self):
        for _ in range(100):
            d1, d2, jugadas = self.screen.tirar_dados()
            self.assertIn(d1, range(1, 7))
            self.assertIn(d2, range(1, 7))
            self.assertIn(jugadas, [2, 4])
            if d1 == d2:
                self.assertEqual(jugadas, 4)
            else:
                self.assertEqual(jugadas, 2)

    def test_cambiar_turno(self):
        turno_inicial = self.screen.turno_actual
        self.screen.cambiar_turno()
        self.assertNotEqual(self.screen.turno_actual, turno_inicial)
        self.screen.cambiar_turno()
        self.assertEqual(self.screen.turno_actual, turno_inicial)

    def test_coords_generadas_correctamente(self):
        self.assertEqual(len(self.screen.coords), 24)
        for i in range(1, 25):
            self.assertIsInstance(self.screen.coords[i], tuple)
            self.assertEqual(len(self.screen.coords[i]), 2)

    def test_dados_imgs_cargados(self):
        self.assertEqual(len(self.screen.dados_imgs), 6)
        for img in self.screen.dados_imgs:
            self.assertIsInstance(img, pygame.Surface)

if __name__ == "__main__":
    unittest.main()
