# CoinSpot Python API
A CoinSpot API for Python 3 and above. 

-Work in progress-

Currently designed for the Read Only CoinSpot API endpoint.

To reach your CoinSpot API keys:
My Account --> API --> Generate New API Key

# Establish Connection:
coinSpotAPI = CoinSpot('enter API key here', 'enter API secret here')

# Return JSON object of all owning crypto's and values:
print(CoinSpotAPI.myBalances())
