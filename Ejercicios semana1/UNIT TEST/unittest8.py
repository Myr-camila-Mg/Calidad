from ejercicio import max
import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
        resultado = max([7,9,54,798,3211,57645, 87, 2341323, 958, 3342])
        self.assertEqual(resultado,2341323)

if __name__ == '__main__':
    unittest.main()