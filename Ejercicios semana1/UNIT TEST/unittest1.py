from ejercicio import total
import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
        resultado = total([3,4,1,8])
        self.assertEqual(resultado,16)

if __name__ == '__main__':
    unittest.main()