import unittest
from src import TropiPy

class LoginTest(unittest.TestCase):
    def test_basic_login(self):
        TppSdk = TropiPy.sdk({
            "url": "https://tropipay-dev.herokuapp.com",
            "credential": {
                'id': 'cf33a19425421dcdfc82d26af3b126d0',
                'secret': '4a7eb4562e21eca14b9318d685950e3e',
            }
        })
        result = TppSdk.get("Security").login()
        self.assertTrue(TppSdk.cfg['token']['access_token'] != None)

if __name__ == '__main__':
    unittest.main()