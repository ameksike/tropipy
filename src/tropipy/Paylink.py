import requests
from tropipy.TropiPy import TropiPy

class Paylink:
    def __init__(self, option):
        self.cfg = option
        self.sdk = TropiPy.sdk()

    def create(self, option):
        url = self.sdk.getUrl('paylink') 
        sec = self.sdk.get("Security").login()
        res = requests.post(url, json=option, headers={
            'Authorization' : sec.get('token_type', 'Bearer')  + ' ' + sec.get('access_token', ' ') 
        })
        data = res.json()
        return data
