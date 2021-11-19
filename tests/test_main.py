import unittest
from tropipy import TropiPy

class MainTest(unittest.TestCase):
    def test_basic_configure(self):
        TppSdk = TropiPy.sdk()
        options = {
            "credential": {
                'id': 'cf33a19425421dcdfc82d26af3b126d0',
                'secret': '4a7eb4562e21eca14b9318d685950e3e',
                'scope': 'ALLOW_GET_PROFILE_DATA ALLOW_GET_BALANCE ALLOW_EXTERNAL_CHARGE'
            }
        }
        result = TppSdk.configure(options).get("Security")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
