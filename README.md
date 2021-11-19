# TropiPy
Python SDK for TropiPay, form more information see [TropiPay Web](http://www.tropipay.com/) and our [wiki](https://github.com/ameksike/tropipy/wiki).

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