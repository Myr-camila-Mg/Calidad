from ejercicio import addit
import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
        resultado = addit(20)
        self.assertEqual(resultado,25)

if __name__ == '__main__':
    unittest.main()