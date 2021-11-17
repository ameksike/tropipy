import requests
from tropipy.TropiPy import TropiPy

class Paylink:
    def __init__(self, option):
        self.cfg = option
        self.sdk = TropiPy.sdk()

    def create(self, option):
        url = self.sdk.getUrl('paylink') 
        access_token = self.sdk.cfg['token']['access_token']
        response = requests.post(url, json=option, headers={'Authorization' : 'Bearer ' + access_token})
        data = response.json()
        return data
