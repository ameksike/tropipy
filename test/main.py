import unittest
from src import TropiPy

class MainTest(unittest.TestCase):
    def test_basic_configure(self):
        TppSdk = TropiPy.sdk()
        options = {
            "credential": {
                'id': 'dsfasdfasf98a7sd98f7as098d',
                'secret': '7df5hd7f5h7df65h8d7fhdfhfh6ddfh75h',
            }
        }
        result = TppSdk.configure(options).get("Security").getData()
        self.assertEqual(result, 'kk')

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