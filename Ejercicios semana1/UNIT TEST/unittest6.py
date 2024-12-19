from ejercicio import reverse
import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
        resultado = reverse("abcdefghijklmnopqrstu")
        self.assertEqual(resultado,"utsrqponmlkjihgfedcba")

if __name__ == '__main__':
    unittest.main()