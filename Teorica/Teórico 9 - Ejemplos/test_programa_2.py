import unittest
from programa import sumar, restar

class TestPrograma(unittest.TestCase):

    def test_sumar(self):
        resultado = sumar(3, 2)
        self.assertEqual(resultado, 5)

    def test_sumar2(self):
        resultado = sumar(2, 1)
        self.assertEqual(resultado, 3)

    def test_restar(self):
        resultado = restar(5, 2)
        self.assertEqual(resultado, 3)

if __name__ == '__main__':
    unittest.main()

