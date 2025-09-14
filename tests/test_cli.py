import unittest
from unittest.mock import patch, MagicMock
from CLI.cli import BackgammonCLI

class TestBackgammonCLI(unittest.TestCase):

    def setUp(self):
        self.cli = BackgammonCLI()
        self.cli.juego = MagicMock()

    @patch("builtins.input", side_effect=["5"])
    def test_mostrar_menu_principal_salir(self, mock_input):
        self.cli.mostrar_menu_principal()
        self.assertFalse(self.cli.running)

    @patch("builtins.input", side_effect=["1", "1", "", ""])
    def test_nueva_partida_automatica(self, mock_input):
        self.cli.juego.jugar_partida_completa = MagicMock()
        self.cli.mostrar_menu_principal()
        self.cli.juego.jugar_partida_completa.assert_called_once()

    @patch("builtins.input", side_effect=["2", "1", "", "salir"])
    def test_partida_humano_vs_ia_turno_humano(self, mock_input):
        self.cli.juego.jugador_actual = "B"
        self.cli.juego.dados_disponibles.return_value = [3]
        self.cli.juego.calcular_destino.return_value = 6
        self.cli.juego.tablero.puede_mover_desde_barra.return_value = False
        self.cli.juego.tablero.movimiento_valido.return_value = (True, "")
        self.cli.juego.tablero.mover_ficha.return_value = (True, "")
        self.cli.mostrar_menu_principal()

    @patch("builtins.input", side_effect=["2", "2", "", "salir"])
    def test_partida_humano_vs_ia_turno_ia(self, mock_input):
        self.cli.juego.jugador_actual = "N"
        self.cli.juego.movimiento_automatico = MagicMock()
        self.cli.juego.tablero.win_conditions.return_value = (True, "N")
        self.cli.mostrar_menu_principal()
        self.cli.juego.movimiento_automatico.assert_called_once()

    @patch("builtins.input", return_value="")
    def test_mostrar_reglas(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.mostrar_reglas()
            mock_print.assert_any_call("📖 REGLAS DE BACKGAMMON")

    def test_mostrar_historial(self):
        with patch("builtins.print") as mock_print:
            self.cli.mostrar_historial()
            mock_print.assert_any_call("\n📊 Historial de partidas (próximamente...)")

    def test_configuracion(self):
        with patch("builtins.print") as mock_print:
            self.cli.configuracion()
            mock_print.assert_any_call("\n⚙️  Configuración (próximamente...)")

    def test_mostrar_victoria(self):
        self.cli.juego.tablero.mostrar_board = MagicMock()
        with patch("builtins.print") as mock_print:
            self.cli.mostrar_victoria("B")
            mock_print.assert_any_call("🏆 ¡BLANCAS GANAN! 🏆")

    def test_salir(self):
        self.cli.salir()
        self.assertFalse(self.cli.running)

if __name__ == "__main__":
    unittest.main()