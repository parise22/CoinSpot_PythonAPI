# CoinSpot_PythonAPI
A CoinSpot API module for Python 3 and above. 

-Work in progress-

Currently designed to work with the Read Only CoinSpot API.

Getting Started:

Establish Connection:
coinSpotAPI = (CoinSpot('enter API key here', 'enter API secret here'))

Returns JSON object of all owning crypto's and values:
print(CoinSpotAPI.myBalances())
