import unittest
from src import TropiPy

class LoginTest(unittest.TestCase):
    def test_basic_login(self):
        TppSdk = TropiPy.sdk({
            "credential": {
                'id': 'dsfasdfasf98a7sd98f7as098d',
                'secret': '7df5hd7f5h7df65h8d7fhdfhfh6ddfh75h',
            }
        })
        result = TppSdk.get("Security").getData()
        self.assertEqual(result, 'kk')

if __name__ == '__main__':
    unittest.main()