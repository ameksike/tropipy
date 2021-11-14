from base.SingletonMeta import SingletonMeta

class TropiPy(metaclass=SingletonMeta):

    def __init__(self, option=None):
        self.cfg = {
            'url': 'localhost:3001',
            'credential': {
                'id': '',
                'secret': ''
            },
            'endpoint': {
                'login': '/api/v2/access/token'
            },
            'token': 'Bearer',
            'contentType': 'application/json'
        }
    
    @staticmethod
    def this(option=None):
        return TropiPy(option)

    def configure(self, option):
        self.cfg = option

    def get(self, modname, param=None):
        module = __import__(modname)
        modcls = getattr(module, modname)
        param = param != None if param else self.cfg
        instance = modcls(param)
        return instance
