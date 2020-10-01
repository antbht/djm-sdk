import json
import requests
from requests.api import request


def get(url):
    req = requests.get(url)
    req.raise_for_status()
    return req.json()

def post(url, data):
    req = requests.post(url, data=json.dumps(data))
    req.raise_for_status()
    return req.json()

def delete(url):
    req = requests.delete(url)
    req.raise_for_status()
    return req.json()