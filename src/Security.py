import requests
from TropiPy import TropiPy

class Security:
    def __init__(self, option):
        self.cfg = option
        self.sdk = TropiPy.sdk()

    def login(self, credential=None, grant="client_credentials", scope=""):
        cred = credential != None if credential else self.cfg['credential']
        url = self.cfg['url'] + self.cfg['endpoint']['login']
        response = requests.post(url, json={
            "grant_type": grant,
            "client_id": cred['id'],
            "client_secret": cred['secret'],
            "scope": scope
        })
        data = response.json()
        if response.status_code == 200:
            for key, value in data.items():
                self.sdk.cfg['token'][key] = value
        return data
    
    def getData(self):
        print(self.cfg)
        return "kk"
