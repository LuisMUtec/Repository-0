import unittest
from calculadora import sumar, restar, multiplicar, dividir

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_resta(self):
        self.assertEqual(restar(10, 4), 6)

    def test_multiplicacion(self):
        self.assertEqual(multiplicar(3, 4), 12)

    def test_division(self):
        self.assertEqual(dividir(12, 4), 3)

    def test_division_por_cero(self):
        self.assertEqual(dividir(10, 0), "Error: división por cero")

if __name__ == '__main__':
    unittest.main()

