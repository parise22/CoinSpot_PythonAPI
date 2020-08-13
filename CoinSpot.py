import hmac
from hashlib import sha512
from time import time
import json
import requests

class CoinSpot(object):
    # CoinSpot -Read Only- API
    API_ENDPOINT = "https://www.coinspot.com.au/api/ro/"

    def __init__(self, apiKey, apiSecret):
        self.key = apiKey
        self.secret = apiSecret.encode()

    # Generator
    def _extract(self, data):
        yield data

    def _request(self, path, data=None):
        if data is None:
            data = {}

        data["nonce"] = int(time() * 1000)
        json_data = json.dumps(data, separators=(',', ':')).encode()

        return requests.post(
            self.API_ENDPOINT + path,
            data=self._extract(json_data),
            headers={
                "Content-Type": "application/json",
                "sign": hmac.new(self.secret, json_data, sha512).hexdigest(),
                "key": self.key,
            }
        ).json()

    def getLatest(self):
        return requests.get("https://www.coinspot.com.au/pubapi/latest").json()

    def myBalances(self):
        return self._request("my/balances")

    def myDeposits(self):
        return self._request("my/deposits")

    def totalTransactionHistory(self):
        return self._request("my/transactions/")

    def transactionHistory(self, coinType):
        return self._request(f"my/transactions/{coinType}")

    def openTransactions(self):
        return self._request("my/transactions/open")
