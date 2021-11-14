from SingletonMeta import SingletonMeta

class TropiPy(metaclass=SingletonMeta):

    def __init__(self, option=None):
        self.cfg = {
            url: 'localhost:3001',
            credential: {
                'id': '',
                'secret': ''
            },
            endpoint: {
                'login': '/api/v2/access/token'
            },
            token: 'Bearer',
            contentType: 'application/json'
        }
    
    @staticmethod
    def this(option=None):
        return TropiPy(option)

    def configure(self, option):
        self.cfg = option

    def get(self, modname):
        module = __import__(modname)
        modcls = getattr(module, class_name)
        instance = modcls(self.cfg)
        return instance
