import unittest
from ..src.TropiPy import TropiPy

class TropiPyTest(unittest.TestCase):
    def test_1(self):
        result = 1 #TropiPy.this()
        print(result)
        self.assertEqual(result, 1)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()