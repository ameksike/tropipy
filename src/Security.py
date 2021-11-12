import requests

class Security:
    def __init__(self, cfg):
        self.cfg = cfg

    def login(self):
        response = requests.post(self.cfg.endpoint.login, json={
            "key": "value"
        })
        response.status_code
        return response.json()
