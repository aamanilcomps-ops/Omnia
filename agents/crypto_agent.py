python
import hashlib
from urllib.request import Request, urlopen
from .abstract_agent import AbstractAgent
class CryptoAgent(AbstractAgent):
    def __init__(self):
        self.api_key = "YOUR_API_KEY"
        self.api_secret = "YOUR_API_SECRET"
        self.exchange = "https://api.binance.com"
    def process(self, input):
        if input["type"] == "buy":
            return self.buy_crypto(input["symbol"], input["quantity"])
        elif input["type"] == "sell":
            return self.sell_crypto(input["symbol"], input["quantity"])
        elif input["type"] == "get_price":
            return self.get_crypto_price(input["symbol"])
    def buy_crypto(self, symbol, quantity):
        params = {
            "symbol": symbol,
            "side": "BUY",
            "type": "MARKET",
            "quantity": quantity
        }
        return self.send_request(params)
    def sell_crypto(self, symbol, quantity):
        params = {
            "symbol": symbol,
            "side": "SELL",
            "type": "MARKET",
            "quantity": quantity
        }
        return self.send_request(params)
    def get_crypto_price(self, symbol):
        params = {
            "symbol": symbol
        }
        return self.send_request(params, "GET /api/v3/ticker/price")
    def send_request(self, params, endpoint=None):
        if endpoint is None:
            endpoint = "/api/v3/order"
        params["api-key"] = self.api_key
        params["api-secret"] = self.api_secret
        params["timestamp"] = int(time.time() * 1000)
        query_string = urllib.parse.urlencode(params)
        signature = hmac.new(self.api_secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()
        headers = {
            "X-MBX-APIKEY": self.api_key,
            "X-MBX-ACCESS-KEY": self.api_key,
            "X-MBX-SIGNATURE": signature
        }
        req = Request(f"{self.exchange}{endpoint}?{query_string}", headers=headers)
        response = urlopen(req)
        return response.read()
