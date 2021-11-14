import requests
from TropiPy import TropiPy

class Paylink:
    def __init__(self, option):
        self.cfg = option
        self.sdk = TropiPy.sdk()
