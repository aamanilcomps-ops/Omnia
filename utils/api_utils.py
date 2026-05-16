python
import requests
def send_request(url, method, data=None):
    if method == "GET":
        return requests.get(url)
    elif method == "POST":
        return requests.post(url, json=data)
