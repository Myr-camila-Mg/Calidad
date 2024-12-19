from ejercicio import even_numbers
import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
        resultado = even_numbers([4,9,6,2,5,3,5,7,1,3,4,5,6,9,8,0])
        self.assertEqual(resultado,[4, 6, 2, 4, 6, 8, 0])

if __name__ == '__main__':
    unittest.main()