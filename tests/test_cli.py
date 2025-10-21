"""Tests para la interfaz CLI del juego Backgammon"""

import unittest
from unittest.mock import patch, MagicMock
from CLI.cli import BackgammonCLI


class TestBackgammonCLI(unittest.TestCase):
    """Test unitarios para la clase BackgammonCLI"""

    def setUp(self):
        """Configura el entorno de prueba con un juego simulado"""
        self.cli = BackgammonCLI()
        self.cli.juego = MagicMock()  # Evita ejecutar lógica real del juego

    @patch("builtins.input", side_effect=["5"])  # Simula opción "Salir"
    def test_mostrar_menu_principal_salir(self, mock_input):
        """Verifica que la opción 'Salir' detiene el bucle principal"""
        self.cli.mostrar_menu_principal()
        self.assertFalse(self.cli.running)

    @patch("builtins.input", side_effect=["1", "", ""])  # Evita StopIteration
    def test_nueva_partida_automatica(self, mock_input):
        """Verifica que se llama a jugar_partida_completa en nueva partida"""
        self.cli.juego.jugar_partida_completa = MagicMock()
        self.cli.nueva_partida()
        self.cli.juego.jugar_partida_completa.assert_called_once()

    @patch("builtins.input", side_effect=["2", "1", "", "", ""])
    def test_partida_humano_vs_ia(self, mock_input):
        """Simula una partida humano vs IA y verifica flujo básico"""
        self.cli.juego.jugador_actual = "B"
        self.cli.juego.dados_disponibles.return_value = [1]
        self.cli.juego.calcular_destino.return_value = 2
        self.cli.juego.tablero.movimiento_valido.return_value = (True, "")
        self.cli.juego.tablero.puede_mover_desde_barra.return_value = True
        self.cli.juego.tablero.mostrar_board = MagicMock()
        self.cli.juego.tablero.win_conditions.return_value = (True, "B")
        self.cli.juego.tablero.mover_ficha = MagicMock()
        self.cli.partida_humano_vs_ia()

    def test_mostrar_reglas(self):
        """Verifica que mostrar_reglas no lanza errores"""
        with patch("builtins.input", return_value=""):
            self.cli.mostrar_reglas()

    def test_mostrar_historial(self):
        """Verifica que mostrar_historial se ejecuta correctamente"""
        self.cli.mostrar_historial()

    def test_configuracion(self):
        """Verifica que configuracion se ejecuta correctamente"""
        self.cli.configuracion()

    def test_mostrar_victoria(self):
        """Verifica que mostrar_victoria muestra el tablero"""
        self.cli.juego.tablero.mostrar_board = MagicMock()
        self.cli.mostrar_victoria("B")

    def test_salir(self):
        """Verifica que salir detiene el bucle principal"""
        self.cli.salir()
        self.assertFalse(self.cli.running)


if __name__ == "__main__":
    unittest.main()
