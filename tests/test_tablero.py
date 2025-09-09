import unittest

from core.tablero import board  # Asegurate de que el archivo se llame backgammon.py o ajustá el import

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.tablero = board()

    def test_puede_mover_desde_barra(self):
        self.tablero.barra_blancas.append("B")
        self.assertTrue(self.tablero.puede_mover_desde_barra("B"))
        self.assertFalse(self.tablero.puede_mover_desde_barra("N"))

    def test_movimiento_valido_desde_barra_obligatorio(self):
        self.tablero.barra_blancas.append("B")
        valido, mensaje = self.tablero.movimiento_valido(1, 3, "B", 2)
        self.assertFalse(valido)
        self.assertEqual(mensaje, "Debes mover fichas desde la barra primero")

    def test_movimiento_valido_direccion_incorrecta(self):
        valido, mensaje = self.tablero.movimiento_valido(13, 12, "B", 1)
        self.assertFalse(valido)
        self.assertEqual(mensaje, "Blancas solo pueden mover hacia puntos mayores")

        valido, mensaje = self.tablero.movimiento_valido(6, 7, "N", 1)
        self.assertFalse(valido)
        self.assertEqual(mensaje, "Negras solo pueden mover hacia puntos menores")

    def test_movimiento_valido_distancia_incorrecta(self):
        valido, mensaje = self.tablero.movimiento_valido(13, 15, "B", 3)
        self.assertFalse(valido)
        self.assertIn("Distancia incorrecta", mensaje)

    def test_movimiento_valido_bloqueado_por_oponente(self):
        self.tablero.celda[5] = ["N", "N"]
        valido, mensaje = self.tablero.movimiento_valido(1, 5, "B", 4)
        self.assertFalse(valido)
        self.assertEqual(mensaje, "Punto bloqueado por el oponente")

    def test_mover_ficha_normal(self):
        self.tablero.celda[13] = ["B"]
        self.tablero.celda[14] = []
        exito, mensaje = self.tablero.mover_ficha(13, 14, "B")
        self.assertTrue(exito)
        self.assertEqual(self.tablero.celda[14], ["B"])
        self.assertEqual(self.tablero.celda[13], [])

    def test_captura_ficha(self):
        self.tablero.celda[5] = ["N"]
        self.tablero.celda[1] = ["B"]
        self.tablero.mover_ficha(1, 5, "B")
        self.assertEqual(self.tablero.barra_negras, ["N"])
        self.assertEqual(self.tablero.celda[5], ["B"])

    def test_puede_sacar_false_si_fichas_fuera_de_casa(self):
        self.tablero.celda[10] = ["B"]
        self.assertFalse(self.tablero.puede_sacar("B"))

    def test_puede_sacar_true_si_todas_en_casa(self):
        for i in range(19, 25):
            self.tablero.celda[i] = ["B"]
        self.assertTrue(self.tablero.puede_sacar("B"))

    def test_win_conditions_por_sacar(self):
        self.tablero.fuera_blancas = ["B"] * 15
        win, ganador = self.tablero.win_conditions()
        self.assertTrue(win)
        self.assertEqual(ganador, "B")

    def test_win_conditions_por_cuatro_en_linea(self):
        self.tablero.celda[1] = ["B"]
        self.tablero.celda[2] = ["B"]
        self.tablero.celda[3] = ["B"]
        self.tablero.celda[4] = ["B"]
        win, ganador = self.tablero.win_conditions()
        self.assertTrue(win)
        self.assertEqual(ganador, "B")

if __name__ == "__main__":
    unittest.main()