from ejercicio import remove_letter
import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
        resultado = remove_letter("e", "esmeralda, equipo, estado, este, elefante")
        self.assertEqual(resultado,"smralda, quipo, stado, st, lfant")

if __name__ == '__main__':
    unittest.main()