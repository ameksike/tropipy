# TropiPy
TropiPay is an electronic wallet that allows you to execute the most common financial operations of the day to day. It is easy and safe. It technology protects your money and ensures it reaches its destination safely. With your TropiPay wallet,you can send remittances and execute the most common collection and payment operations, from paying at a store to sharing expenses with your friends.

- Remittances and family support.
- Transfers between bank accounts.
- Paying with your mobile phone.
- Share expenses with your friends.
- Top-up phone balance.
- Promotions and discounts every month.

FOR SMALL COMPANIES AND BUSINESSES: 
Tropipay offer online payment and collection solutions to international customers and global markets. Whether you are a business owner, professional, or freelancer, Tropipay is the ultimate financial tool.

- Transfers between bank accounts.
- Sale through social networks.
- E-commerce integration through API.
- Customized solutions for tourism companies.
- Cross Border payments globally

This project is focused on create a simple python SDK for TropiPay, in order to facilitate the integration of the TropiPay platform with frameworks such as [Django](https://www.djangoproject.com/), [Flask](https://flask.palletsprojects.com/en/2.0.x/), etc. Form more information see [TropiPay Web](http://www.tropipay.com/) and our [wiki](https://github.com/ameksike/tropipy/wiki).

## Install
- pip install tropipy
- [pypi.org](https://pypi.org/project/tropipy/) 


## Develop
Contribute to us to improve our products and services

### Develop Install
- git clone https://github.com/ameksike/tropipy.git
- cd tropipy
- pip install -r requirements.txt
- pip show requests
- pip list -v

### Develop Test
- python -m unittest                        # One command to run them all
- python -m unittest tests/test_login.py    # Selective run some test suite


## Examples

Configure the lib: 
```python
TppSdk = TropiPy({
   "credential": {
		'id': 'cf33a19425421dcdfc82d26af3b126d0',
		'secret': '4a7eb4562e21eca14b9318d685950e3e',
		'scope': 'ALLOW_GET_PROFILE_DATA ALLOW_GET_BALANCE ALLOW_EXTERNAL_CHARGE'
	}
})
```

Login for get access token:
```python
result = TppSdk.get("Security").login()
```