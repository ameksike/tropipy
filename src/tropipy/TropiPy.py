from tropipy.SingletonMeta import SingletonMeta

class TropiPy(metaclass=SingletonMeta):

    def __init__(self, option=None):
        self.cfg = {
            'url': 'https://tropipay-dev.herokuapp.com',
            'credential': {
                'id': '',
                'secret': '',
                'scope': 'ALLOW_EXTERNAL_CHARGE ALLOW_CREATE_BENEFICIARY ALLOW_UPDATE_BENEFICIARY ALLOW_PAYMENT_IN ALLOW_PAYMENT_OUT ALLOW_MARKET_PURCHASES ALLOW_GET_PROFILE_DATA ALLOW_GET_BALANCE ALLOW_GET_MOVEMENT_LIST'
            },
            'endpoint': {
                'login': '/api/v2/access/token',
                'paylink': '/api/v2/paymentcards',
            },
            'token': {
                'type': 'Bearer',
                'access_token': None
            },
            'contentType': 'application/json'
        }
        self.configure(option)

    def configure(self, option=None):
        if option != None:
            for key, value in option.items():
                self.cfg[key] = value
        return self

    def getUrl(self, key):
        return self.cfg['url'] + self.cfg['endpoint'][key]
    
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
        module = __import__("tropipy." + modname)
        print(module)
        modcls = getattr(module, modname)
        param = param != None if param else self.cfg
        instance = modcls(param)
        return instance
