import unittest
from src.tropipy.TropiPy import TropiPy

class LoginTest(unittest.TestCase):
    def test_basic_login(self):
        TppSdk = TropiPy({
            "credential": {
                'id': 'cf33a19425421dcdfc82d26af3b126d0',
                'secret': '4a7eb4562e21eca14b9318d685950e3e',
                'scope': 'ALLOW_GET_PROFILE_DATA ALLOW_GET_BALANCE ALLOW_EXTERNAL_CHARGE'
            }
        })
        result = TppSdk.get("Security").login()
        self.assertTrue(result['access_token'] != None)

if __name__ == '__main__':
    unittest.main()