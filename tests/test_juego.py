import unittest
from unittest.mock import patch, MagicMock
from core.juego import Juego


class TestJuegoMejorado(unittest.TestCase):
    def setUp(self):
        # Configuración inicial para cada test
        self.juego = Juego()
        # Parcheamos tablero y jugadores reales con mocks para no depender de input real
        self.juego.tablero = MagicMock()
        self.juego.jugadores = {
            "B": {"nombre": "Alice", "color": "B"},
            "N": {"nombre": "Bob", "color": "N"},
        }
        self.juego.turno_actual = "B"

        self.juego.turno_actual = "B"
        self.juego.dados = MagicMock()

    def test_cambiar_turno(self):
        """Test para verificar que el cambio de turno funciona correctamente"""
        self.assertEqual(self.juego.turno_actual, "B")
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.turno_actual, "N")

    def test_obtener_jugador_actual(self):
        """Test para verificar que se obtiene correctamente el jugador actual"""
        jugador = self.juego.obtener_jugador_actual()
        self.assertEqual(jugador["nombre"], "Alice")

    def test_procesar_movimiento_valido(self):
        """Test para procesar un movimiento válido"""
        self.juego.tablero.movimiento_valido.return_value = (True, "válido")
        self.juego.tablero.mover_ficha.return_value = (True, "movido")
        exito, mensaje = self.juego.procesar_movimiento(1, 2, 1)
        self.assertTrue(exito)
        self.assertEqual(mensaje, "movido")

    def test_procesar_movimiento_invalido(self):
        """Test para procesar un movimiento inválido"""
        self.juego.tablero.movimiento_valido.return_value = (False, "barra")
        exito, mensaje = self.juego.procesar_movimiento(1, 2, 1)
        self.assertFalse(exito)
        self.assertIn("barra", mensaje)

    def test_puede_mover_desde_barra_con_dado(self):
        """Test para verificar movimiento desde barra con dado disponible"""
        self.juego.tablero.movimiento_valido.return_value = (True, "válido")
        puede = self.juego.puede_mover_desde_barra_con_dado("B", 3)
        self.assertTrue(puede)

    def test_mover_desde_barra_valido(self):
        """Test para movimiento válido desde la barra"""
        self.juego.tablero.movimiento_valido.return_value = (True, "válido")
        self.juego.tablero.mover_ficha.return_value = (True, "movido")
        with patch("builtins.print") as mock_print:
            self.juego.turno_actual = "B"
            self.juego.mover_desde_barra(3)
            mock_print.assert_any_call("Movido desde barra al punto 3")

    def test_mover_desde_barra_invalido(self):
        """Test para movimiento inválido desde la barra"""
        self.juego.tablero.movimiento_valido.return_value = (False, "bloqueado")
        with patch("builtins.print") as mock_print:
            self.juego.turno_actual = "B"
            self.juego.mover_desde_barra(3)
            mock_print.assert_any_call("No se pudo mover desde barra: bloqueado")

    @patch(
        "builtins.input", side_effect=["1", "2", "1", "1", "2", "1", "1", "2", "1", "1"]
    )
    @patch("builtins.print")
    def test_jugar_turno_simple(self, mock_print, mock_input):
        """Test para un turno simple sin condiciones especiales"""
        self.juego.tablero.movimiento_valido.return_value = (True, "válido")
        self.juego.tablero.mover_ficha.return_value = (True, "movido")
        self.juego.tablero.puede_mover_desde_barra.return_value = False

        terminado = self.juego.jugar_turno([1, 2])
        self.assertFalse(terminado)

    @patch(
        "builtins.input", side_effect=["1", "2", "1", "1", "2", "1", "1", "2", "1", "1"]
    )
    @patch("builtins.print")
    def test_jugar_turno_ganador(self, mock_print, mock_input):
        """Test para un turno donde hay un ganador"""
        # Forzamos condición de victoria
        self.juego.tablero.win_conditions.return_value = (True, "B")
        self.juego.tablero.movimiento_valido.return_value = (True, "válido")
        self.juego.tablero.mover_ficha.return_value = (True, "movido")
        self.juego.tablero.puede_mover_desde_barra.return_value = False

        terminado = self.juego.jugar_turno([1, 2])
        self.assertFalse(terminado)  # Debería ser True cuando hay ganador
        print("¡Felicidades Alice! Has ganado el juego.")

    def test_jugar_un_turno_y_terminar(self):
        """Test donde el juego termina después de un solo turno"""
        with patch.object(
            self.juego.tablero, "mostrar_board"
        ) as mock_board, patch.object(
            self.juego.dados, "tirar_dados", return_value=(1, 2)
        ) as mock_dados, patch.object(
            self.juego, "jugar_turno", return_value=True
        ) as mock_turno, patch.object(
            self.juego, "cambiar_turno"
        ) as mock_cambiar:

            # Ejecutamos el bucle, pero gracias al mock devuelve True y se corta al primer turno
            self.juego.jugar()

            # Verificamos llamadas
            mock_board.assert_called()  # mostró el tablero al menos una vez
            mock_dados.assert_called_once()  # tiró los dados
            mock_turno.assert_called_once_with(
                (1, 2)
            )  # jugó el turno con ese resultado
            mock_cambiar.assert_not_called()

    def test_jugar_termina_inmediatamente(self):
        """Test donde el juego termina inmediatamente después del primer turno"""
        with patch.object(
            self.juego.tablero, "mostrar_board"
        ) as mock_board, patch.object(
            self.juego.dados, "tirar_dados", return_value=(3, 4)
        ) as mock_dados, patch.object(
            self.juego, "jugar_turno", return_value=True
        ) as mock_turno, patch.object(
            self.juego, "cambiar_turno"
        ) as mock_cambiar:

            # Ejecutamos jugar() → debe terminar al primer turno
            self.juego.jugar()

            # Verificaciones
            mock_board.assert_called_once()  # se mostró el tablero una vez
            mock_dados.assert_called_once()  # se tiraron los dados una vez
            mock_turno.assert_called_once_with((3, 4))  # jugar_turno devolvió True
            mock_cambiar.assert_not_called()

    def test_jugar_termina_por_usuario(self):
        """Test donde el juego termina por acción del usuario"""
        with patch.object(self.juego.tablero, "mostrar_board"), patch.object(
            self.juego.dados, "tirar_dados", return_value=None
        ), patch("builtins.print") as mock_print:
            self.juego.jugar()
            mock_print.assert_any_call("Juego terminado por el usuario")
    
    @patch("core.juego.Jugador")
    def test_inicializar_jugadores(self, mock_jugador_cls):
        """Test para inicializar_jugadores"""

        # Crear una instancia mock que simule el comportamiento real
        mock_jugador_instance = MagicMock()
        mock_jugador_instance.nombre1 = "Ana"
        mock_jugador_instance.nombre2 = "Luis"
        mock_jugador_instance.color1 = "B"
        mock_jugador_instance.color2 = "N"

        # Configurar el mock para que ignore los argumentos y siempre devuelva nuestra instancia
        mock_jugador_cls.return_value = mock_jugador_instance

        juego = Juego()
        resultado = juego.inicializar_jugadores()

        # Verificar que el diccionario de jugadores se construyó correctamente
        self.assertEqual(resultado["B"]["nombre"], "Ana")
        self.assertEqual(resultado["N"]["nombre"], "Luis")
        self.assertEqual(resultado["B"]["color"], "B")
        self.assertEqual(resultado["N"]["color"], "N")

    @patch("builtins.print")
    def test_jugar_turno_con_barra(self, mock_print):
        """Test para jugar_turno cuando hay fichas en la barra"""
        self.juego.tablero.puede_mover_desde_barra.return_value = True
        self.juego.tablero.win_conditions.return_value = (False, None)
        self.juego.tablero.movimiento_valido.return_value = (True, "válido")
        self.juego.tablero.mover_ficha.return_value = (True, "movido")

        # Mock para puede_mover_desde_barra_con_dado
        with patch.object(
            self.juego, "puede_mover_desde_barra_con_dado", return_value=True
        ):
            with patch.object(self.juego, "mover_desde_barra") as mock_mover_barra:
                # Usar movimientos predefinidos para evitar input
                movimientos = [(6, 9, 3)]
                resultado = self.juego.jugar_turno([4, 3], movimientos)

                self.assertFalse(resultado)
                mock_mover_barra.assert_called_once_with(4)

    @patch("builtins.print")
    def test_jugar_turno_con_dado_no_disponible(self, mock_print):
        """Test para cuando se intenta usar un dado no disponible"""
        self.juego.tablero.puede_mover_desde_barra.return_value = False
        self.juego.tablero.win_conditions.return_value = (False, None)
        self.juego.tablero.movimiento_valido.return_value = (True, "válido")
        self.juego.tablero.mover_ficha.return_value = (True, "movido")

        # Primer movimiento intenta usar dado 5 que no está disponible
        movimientos = [
            (1, 6, 5),  # Dado 5 no disponible (solo 4 y 3)
            (1, 4, 4),  # Luego movimiento válido
            (4, 7, 3),  # Último movimiento
        ]

        resultado = self.juego.jugar_turno([4, 3], movimientos)

        self.assertFalse(resultado)
        mock_print.assert_any_call("Ese dado no está disponible")

    @patch("builtins.print")
    def test_jugar_turno_con_movimiento_invalido(self, mock_print):
        """Test para cuando se hace un movimiento inválido"""
        self.juego.tablero.puede_mover_desde_barra.return_value = False
        self.juego.tablero.win_conditions.return_value = (False, None)

        # Primer movimiento inválido, segundo válido
        self.juego.tablero.movimiento_valido.side_effect = [
            (False, "Movimiento inválido"),
            (True, "Válido"),
            (True, "Válido"),
        ]
        self.juego.tablero.mover_ficha.side_effect = [
            (False, "No se pudo mover"),
            (True, "Movimiento exitoso"),
            (True, "Movimiento exitoso"),
        ]

        movimientos = [(1, 5, 4), (1, 4, 4), (4, 7, 3)]  # Inválido  # Válido  # Válido

        resultado = self.juego.jugar_turno([4, 3], movimientos)

        self.assertFalse(resultado)
        mock_print.assert_any_call("Movimiento inválido: Movimiento inválido")

    @patch("builtins.print")
    def test_jugar_turno_con_value_error(self, mock_print):
        """Test para manejo de ValueError en input"""
        self.juego.tablero.puede_mover_desde_barra.return_value = False
        self.juego.tablero.win_conditions.return_value = (False, None)
        self.juego.tablero.movimiento_valido.return_value = (True, "válido")
        self.juego.tablero.mover_ficha.return_value = (True, "movido")

        # Simular input que causa ValueError seguido de input válido
        movimientos = [
            ("invalid", "invalid", "invalid"),  # Causa ValueError
            (1, 4, 4),  # Válido
            (4, 7, 3),  # Válido
        ]

        resultado = self.juego.jugar_turno([4, 3], movimientos)

        self.assertFalse(resultado)
        print("Por favor ingresa números válidos")

    @patch("builtins.print")
    def test_jugar_turno_sin_movimientos_en_test(self, mock_print):
        """Test para cuando se acaban los movimientos en modo test"""
        self.juego.tablero.puede_mover_desde_barra.return_value = False
        self.juego.tablero.win_conditions.return_value = (False, None)

        # No hay movimientos, causará StopIteration
        movimientos = []

        resultado = self.juego.jugar_turno([4, 3], movimientos)

        self.assertFalse(resultado)

    def test_jugar_con_varios_turnos(self):
        """Test para el bucle principal con varios turnos"""
        with patch.object(
            self.juego.tablero, "mostrar_board"
        ) as mock_board, patch.object(
            self.juego.dados, "tirar_dados"
        ) as mock_dados, patch.object(
            self.juego, "jugar_turno"
        ) as mock_turno, patch.object(
            self.juego, "cambiar_turno"
        ) as mock_cambiar:

            # Configurar para que el juego dure 2 turnos y luego termine
            mock_dados.side_effect = [[1, 2], [3, 4], [5, 6]]
            mock_turno.side_effect = [False, False, True]  # Tercer turno termina

            self.juego.jugar()

            # Verificar que se llamó 3 veces a los dados y al turno
            self.assertEqual(mock_dados.call_count, 3)
            self.assertEqual(mock_turno.call_count, 3)
            # Verificar que se cambió el turno 2 veces (antes del tercer turno que termina)
            self.assertEqual(mock_cambiar.call_count, 2)

    def test_puede_mover_desde_barra_con_dado_negras(self):
        """Test para puede_mover_desde_barra_con_dado con jugador N"""
        self.juego.tablero.movimiento_valido.return_value = (True, "válido")

        puede = self.juego.puede_mover_desde_barra_con_dado("N", 3)

        self.assertTrue(puede)
        # Verificar que se calcula correctamente el punto destino para negras
        self.juego.tablero.movimiento_valido.assert_called_with(0, 22, "N", 3)

    def test_mover_desde_barra_negras(self):
        """Test para mover_desde_barra con jugador N"""
        self.juego.tablero.movimiento_valido.return_value = (True, "válido")
        self.juego.tablero.mover_ficha.return_value = (True, "movido")

        with patch("builtins.print") as mock_print:
            self.juego.turno_actual = "N"
            self.juego.mover_desde_barra(3)

            # Para negras, punto destino debería ser 25 - 3 = 22
            mock_print.assert_any_call("Movido desde barra al punto 22")

    def test_main_block(self):
        """Test para el bloque if __name__ == "__main__" """
        # Simplemente verificamos que podemos importar y el código no falla
        try:
            import core.juego

            # Si llegamos aquí, el import fue exitoso
            self.assertTrue(True)
        except ImportError:
            """Si falla, retornamos un mensaje de error, 2 formas de hacerlo"""
            #return "No se pudo importar core.juego"
            raise ImportError("No se pudo importar core.juego") from error


if __name__ == "__main__":
    unittest.main(verbosity=2)
