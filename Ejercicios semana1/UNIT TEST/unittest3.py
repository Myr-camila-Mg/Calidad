from ejercicio import mult
import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
        resultado = mult(20)
        self.assertEqual(resultado,500)

if __name__ == '__main__':
    unittest.main()