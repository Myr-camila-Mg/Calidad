from ejercicio import length
import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
        resultado = length([1,2,4,4,6,2,2,4,6,6,3,5,4,5,8,7])
        self.assertEqual(resultado,"Longer than 5")
    def test_2(self):
        resultado = length("aguacateconpapas")
        self.assertEqual(resultado,"Longer than 5")
if __name__ == '__main__':
    unittest.main()