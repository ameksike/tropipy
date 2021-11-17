from tropipy import TropiPy
TppSdk = TropiPy.sdk({
    "credential": {
        'id': 'cf33a19425421dcdfc82d26af3b126d0',
        'secret': '4a7eb4562e21eca14b9318d685950e3e',
    }
})
result = TppSdk.get("Security").login()
print(result)
print('///////////////////////////////////////////////////////////')
print(TppSdk.cfg)

result = TppSdk.get("Paylink").create({
    "reference": "demo23232323",
    "concept": "some product id",
    "description": "some product description",
    "favorite": "true",
    "amount": 11500,
    "currency": "EUR",
    "singleUse": "true",
    "reasonId": 4,
    "reasonDes": "",
    "expirationDays": 1,
    "userId": "e2931920-e402-11ea-a30d-83c978a74aaa",
    "lang": "es",
    "urlSuccess": "",
    "urlFailed": "",
    "urlNotification": "",

    "serviceDate": ""
})
print('///////////////////////////////////////////////////////////')
print(result)
print('///////////////////////////////////////////////////////////')