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
        self.configure(option)

    def configure(self, option=None):
        if option != None:
            for key, value in option.items():
                self.cfg[key] = value
        return self
    
    '''
    @decription factory
    @param OBJECT option
    @return OBJECT
    '''
    @staticmethod
    def sdk(option=None):
        return TropiPy(option)

    '''
    @decription IoC
    @param STRING modname
    @param OBJECT param
    @return OBJECT
    '''
    def get(self, modname, param=None):
        module = __import__(modname)
        modcls = getattr(module, modname)
        param = param != None if param else self.cfg
        instance = modcls(param)
        return instance
