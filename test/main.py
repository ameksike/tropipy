from .. import TropiPy

import unittest

class TestMain(unittest.TestCase):
    def test_1(self):
        resultado = TropiPy
        self.assertEqual(resultado, 10)

    def test_2(self):
        resultado = TropiPy([5, 3, 4])
        self.assertEqual(resultado, 4)

if __name__ == '__main__':
    unittest.main()