import requests

class Security:
    def __init__(self, cfg):
        self.cfg = cfg

    def login(self):
        response = requests.post(self.cfg.endpoint.login, json={
            "grant_type": "client_credentials",
            "client_id": self.cfg.credential.id,
            "client_secret": self.cfg.credential.secret,
        })
        print(response.status_code)
        return response.json()
    
    def getData(self):
        print(self.cfg)
        return "kk"
