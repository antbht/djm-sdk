import requests


def get(url):
    req = requests.get(url)
    req.raise_for_status()
    return req.json()

def post(uri, data):
    pass

def delete(uri):
    pass