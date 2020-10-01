import requests
from requests.api import request


def get(url):
    req = requests.get(url)
    req.raise_for_status()
    return req.json()

def post(uri, data):
    pass

def delete(url):
    req = requests.delete(url)
    req.raise_for_status()
    return req.json()