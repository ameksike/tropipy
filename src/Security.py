import requests

class Security:
    def __init__(self, cfg):
        self.cfg = cfg

    def login(self, credential=None, grant="client_credentials", scope=""):
        cred = credential != None if credential else self.cfg['credential']
        url = self.cfg['url'] + self.cfg['endpoint']['login']
        response = requests.post(url, json={
            "grant_type": grant,
            "client_id": cred['id'],
            "client_secret": cred['secret'],
            "scope": scope
        })
        print(response.status_code)
        return response.json()
    
    def getData(self):
        print(self.cfg)
        return "kk"
