from ejercicio import divide
import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
        resultado = divide(20,10)
        self.assertEqual(resultado,2)

if __name__ == '__main__':
    unittest.main()