import requests
from tropipy.TropiPy import TropiPy

class Security:
    def __init__(self, option):
        self.cfg = option
        self.sdk = TropiPy.sdk()

    def login(self, credential=None, grant="client_credentials"):
        cred = credential != None if credential else self.cfg['credential']
        url = self.sdk.getUrl('login') 
        response = requests.post(url, json={
            "grant_type": grant,
            "client_id": cred.get('id'),
            "client_secret": cred.get('secret'),
            "scope": cred.get('scope')
        })
        data = response.json()
        if response.status_code == 200:
            for key, value in data.items():
                self.sdk.cfg['token'][key] = value
        return data

