# CoinSpot Python API
A CoinSpot API module for Python 3 and above. 

-Work in progress-

Currently designed for the Read Only CoinSpot API endpoint.

Getting Started:

# Establish Connection:
coinSpotAPI = (CoinSpot('enter API key here', 'enter API secret here'))

# Return JSON object of all owning crypto's and values:
print(CoinSpotAPI.myBalances())
