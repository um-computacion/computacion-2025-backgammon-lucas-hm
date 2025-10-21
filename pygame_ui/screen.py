"""Tests para la clase Screen del juego Backgammon usando unittest."""

import unittest
from unittest.mock import patch, MagicMock
from typing import Tuple

import pygame

# Importamos la clase Screen desde el módulo correspondiente
from pygame_ui.screen import Screen


class TestScreen(unittest.TestCase):
    """Tests unitarios para la clase Screen."""

    def setUp(self) -> None:
        """Inicializa una instancia de Screen con mocks para evitar abrir ventana real."""
        # Parcheamos funciones de pygame y os.path para evitar efectos secundarios
        self.patcher_display = patch("pygame.display.set_mode", return_value=MagicMock())
        self.patcher_font = patch("pygame.font.SysFont", return_value=MagicMock())
        self.patcher_image = patch("pygame.image.load", return_value=MagicMock())
        self.patcher_surface = patch("pygame.Surface", return_value=MagicMock())
        self.patcher_caption = patch("pygame.display.set_caption")
        self.patcher_clock = patch("pygame.time.Clock", return_value=MagicMock())

        self.mock_display = self.patcher_display.start()
        self.mock_font = self.patcher_font.start()
        self.mock_image = self.patcher_image.start()
        self.mock_surface = self.patcher_surface.start()
        self.mock_caption = self.patcher_caption.start()
        self.mock_clock = self.patcher_clock.start()

        self.addCleanup(self.patcher_display.stop)
        self.addCleanup(self.patcher_font.stop)
        self.addCleanup(self.patcher_image.stop)
        self.addCleanup(self.patcher_surface.stop)
        self.addCleanup(self.patcher_caption.stop)
        self.addCleanup(self.patcher_clock.stop)

    @patch("os.path.exists", return_value=True)
    def test_constructor_carga_imagenes(self, mock_exists: MagicMock) -> None:
        """Verifica que el constructor cargue las imágenes si existen."""
        screen = Screen()
        self.assertIsNotNone(screen.ficha_blanca_img)
        self.assertIsNotNone(screen.ficha_negra_img)

    @patch("os.path.exists", side_effect=lambda path: "ficha-blanca" not in path)
    @patch("pygame.Surface", return_value=MagicMock())
    def test_constructor_placeholder_blanca(self, mock_surface: MagicMock, mock_exists: MagicMock) -> None:
        """Verifica que se use un placeholder si no se encuentra la ficha blanca."""
        screen = Screen()
        self.assertIsNotNone(screen.ficha_blanca_img)

    def test_estado_inicial(self) -> None:
        """Verifica que el estado inicial del juego sea correcto."""
        screen = Screen()
        self.assertEqual(screen.estado.turno_actual, "Blanco")
        self.assertEqual(screen.estado.dado1, 0)
        self.assertEqual(screen.estado.dado2, 0)
        self.assertEqual(screen.estado.jugadas, 0)
        self.assertTrue(screen.estado.running)

    def test_tirar_dados_valores_validos(self) -> None:
        """Verifica que los dados generen valores entre 1 y 6."""
        for _ in range(100):
            dado1, dado2, jugadas = Screen._tirar_dados()
            self.assertIn(dado1, range(1, 7))
            self.assertIn(dado2, range(1, 7))
            self.assertIn(jugadas, [2, 4])

    def test_cambiar_turno(self) -> None:
        """Verifica que el turno se alterne correctamente."""
        screen = Screen()
        turno_inicial = screen.estado.turno_actual
        screen._cambiar_turno()
        self.assertNotEqual(screen.estado.turno_actual, turno_inicial)
        screen._cambiar_turno()
        self.assertEqual(screen.estado.turno_actual, turno_inicial)

    def test_generar_coordenadas(self) -> None:
        """Verifica que se generen 24 coordenadas únicas."""
        screen = Screen()
        coords = screen._generar_coordenadas()
        self.assertEqual(len(coords), 24)
        for punto, (x, y) in coords.items():
            self.assertIsInstance(punto, int)
            self.assertIsInstance(x, int)
            self.assertIsInstance(y, int)

    def test_inicializar_fichas(self) -> None:
        """Verifica que las fichas se coloquen en las posiciones iniciales."""
        screen = Screen()
        screen._inicializar_fichas()
        self.assertEqual(screen.posiciones[1][0], ("Blanca", 3))
        self.assertEqual(screen.posiciones[24][0], ("Negra", 2))

    def test_dibujar_tablero_no_excepciona(self) -> None:
        """Verifica que el método de dibujo del tablero no lance errores."""
        screen = Screen()
        try:
            screen._dibujar_tablero()
        except Exception as e:
            self.fail(f"_dibujar_tablero lanzó una excepción: {e}")

    def test_dibujar_dados_y_texto_no_excepciona(self) -> None:
        """Verifica que el método de dibujo de dados no lance errores."""
        screen = Screen()
        screen.estado.dado1 = 3
        screen.estado.dado2 = 5
        screen.estado.jugadas = 2
        try:
            screen._dibujar_dados_y_texto()
        except Exception as e:
            self.fail(f"_dibujar_dados_y_texto lanzó una excepción: {e}")


if __name__ == "__main__":
    unittest.main()
