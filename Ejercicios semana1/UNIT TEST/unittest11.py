from ejercicio import is_even
import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
        resultado = is_even(48)
        self.assertEqual(resultado, True)

if __name__ == '__main__':
    unittest.main()