import unittest
from core.jugador import jugador

class test_jugador(unittest.TestCase):
    def test_datos(self):
        player = jugador()
        player.datos(barra=0, fichas_sacadas=0)
        self.assertEqual(player.datos.nombre1, "Alice")
        self.assertEqual(player.datos.nombre2, "Bob")
        self.assertEqual(player.color1, 1)
        self.assertEqual(player.color2, 2)
        
if __name__ == "__main__":
    unittest.main()