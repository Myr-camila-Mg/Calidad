from ejercicio import odd_numbers
import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
        resultado = odd_numbers([4,9,6,2,5,3,5,7,1,3,4,5,6,9,8,0])
        self.assertEqual(resultado,[9, 5, 3, 5, 7, 1, 3, 5, 9])

if __name__ == '__main__':
    unittest.main()