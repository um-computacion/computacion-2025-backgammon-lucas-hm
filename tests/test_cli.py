 import unittest
 from unittest.mock import patch, MagicMock
 from CLI.cli import BackgammonCLI

 class TestBackgammonCLI(unittest.TestCase):
     def setUp(self):
         self.cli = BackgammonCLI()
         self.cli.juego = MagicMock()  # Evita ejecutar lógica real del juego

     @patch('builtins.input', side_effect=["5"])  # Simula opción "Salir"
     def test_mostrar_menu_principal_salir(self, mock_input):
         self.cli.mostrar_menu_principal()
         self.assertFalse(self.cli.running)

     @patch('builtins.input', side_effect=["1", "", ""])  # Agrega un extra para evitar StopIteration
     def test_nueva_partida_automatica(self, mock_input):
         self.cli.juego.jugar_partida_completa = MagicMock()
         self.cli.nueva_partida()
         self.cli.juego.jugar_partida_completa.assert_called_once()


     @patch('builtins.input', side_effect=["2", "1", "", "", ""])  # agregá más "" según sea necesario
     def test_partida_humano_vs_ia(self, mock_input):
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
         with patch('builtins.input', return_value=""):
             self.cli.mostrar_reglas()

     def test_mostrar_historial(self):
         self.cli.mostrar_historial()  # Solo imprime y espera

     def test_configuracion(self):
         self.cli.configuracion()  # Solo imprime y espera

     def test_mostrar_victoria(self):
         self.cli.juego.tablero.mostrar_board = MagicMock()
         self.cli.mostrar_victoria("B")

     def test_salir(self):
         self.cli.salir()
         self.assertFalse(self.cli.running)

 if __name__ == "__main__":
     unittest.main()
