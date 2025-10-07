# import unittest
# from unittest.mock import patch, MagicMock
# from CLI.cli import BackgammonCLI

# class TestBackgammonCLI(unittest.TestCase):
#     def setUp(self):
#         self.cli = BackgammonCLI()
#         self.cli.juego = MagicMock()  # Evita ejecutar lógica real del juego

#     @patch('builtins.input', side_effect=["5"])  # Simula opción "Salir"
#     def test_mostrar_menu_principal_salir(self, mock_input):
#         self.cli.mostrar_menu_principal()
#         self.assertFalse(self.cli.running)

#     @patch('builtins.input', side_effect=["1", "", ""])  # Agrega un extra para evitar StopIteration
#     def test_nueva_partida_automatica(self, mock_input):
#         self.cli.juego.jugar_partida_completa = MagicMock()
#         self.cli.nueva_partida()
#         self.cli.juego.jugar_partida_completa.assert_called_once()


#     @patch('builtins.input', side_effect=["2", "1", "", "", ""])  # agregá más "" según sea necesario
#     def test_partida_humano_vs_ia(self, mock_input):
#         self.cli.juego.jugador_actual = "B"
#         self.cli.juego.dados_disponibles.return_value = [1]
#         self.cli.juego.calcular_destino.return_value = 2
#         self.cli.juego.tablero.movimiento_valido.return_value = (True, "")
#         self.cli.juego.tablero.puede_mover_desde_barra.return_value = True
#         self.cli.juego.tablero.mostrar_board = MagicMock()
#         self.cli.juego.tablero.win_conditions.return_value = (True, "B")
#         self.cli.juego.tablero.mover_ficha = MagicMock()
#         self.cli.partida_humano_vs_ia()

#     def test_mostrar_reglas(self):
#         with patch('builtins.input', return_value=""):
#             self.cli.mostrar_reglas()

#     def test_mostrar_historial(self):
#         self.cli.mostrar_historial()  # Solo imprime y espera

#     def test_configuracion(self):
#         self.cli.configuracion()  # Solo imprime y espera

#     def test_mostrar_victoria(self):
#         self.cli.juego.tablero.mostrar_board = MagicMock()
#         self.cli.mostrar_victoria("B")

#     def test_salir(self):
#         self.cli.salir()
#         self.assertFalse(self.cli.running)

# if __name__ == "__main__":
#     unittest.main()

import unittest
from unittest.mock import patch, MagicMock
from CLI.cli import BackgammonCLI

class TestBackgammonCLI(unittest.TestCase):
    def setUp(self):
        self.cli = BackgammonCLI()
        self.cli.juego = MagicMock()

    @patch('builtins.input', side_effect=["5"])
    @patch('builtins.print')
    def test_mostrar_menu_principal_salir(self, mock_print, mock_input):
        self.cli.mostrar_menu_principal()
        self.assertFalse(self.cli.running)

    @patch('builtins.input', side_effect=["1"])
    @patch('builtins.print')
    def test_nueva_partida_automatica(self, mock_print, mock_input):
        self.cli.juego.jugar_partida_completa = MagicMock()
        self.cli.nueva_partida()
        self.cli.juego.jugar_partida_completa.assert_called_once()

    @patch('builtins.input', side_effect=["2", "1", "s", "n", "5"])
    @patch('builtins.print')
    def test_partida_humano_vs_ia(self, mock_print, mock_input):
        # Configurar mocks más completos
        self.cli.juego.jugador_actual = "B"
        self.cli.juego.jugador_blancas = "B"
        self.cli.juego.jugador_negras = "N"
        self.cli.juego.dados = [1, 2]
        self.cli.juego.dados_disponibles.return_value = [1, 2]
        self.cli.juego.tablero.movimiento_valido.return_value = (True, "")
        self.cli.juego.tablero.puede_mover_desde_barra.return_value = False
        self.cli.juego.tablero.mostrar_board = MagicMock()
        self.cli.juego.tablero.win_conditions.return_value = (False, None)
        self.cli.juego.tablero.mover_ficha = MagicMock()
        self.cli.juego.tirar_dados = MagicMock(return_value=[1, 2])
        
        self.cli.partida_humano_vs_ia()

    # @patch('builtins.input', side_effect=[""])
    # @patch('builtins.print')
    # def test_mostrar_historial(self, mock_print, mock_input):
    #     self.cli.mostrar_historial()

    @patch('builtins.print')
    def test_mostrar_victoria(self, mock_print):
        self.cli.juego.tablero.mostrar_board = MagicMock()
        self.cli.mostrar_victoria("B")

    def test_salir(self):
        self.cli.salir()
        self.assertFalse(self.cli.running)

if __name__ == "__main__":
    unittest.main()