import sys, os, unittest
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core.jugador import jugador

class test_jugador(unittest.TestCase):
    def test_datos(self):
        player = jugador(nombre1="Alice", nombre2="Bob", color1="red", color2="blue")
        self.assertEqual(player.nombre1, "Alice")
        self.assertEqual(player.nombre2, "Bob")
        self.assertEqual(player.color1, "red")
        self.assertEqual(player.color2, "blue")
        
if __name__ == "__main__":
    unittest.main()