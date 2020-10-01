import json
import requests
from requests.api import request

from djm_sdk import exceptions

def catch_backend_http_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (requests.exceptions.ConnectTimeout, 
            requests.exceptions.HTTPError,
            requests.exceptions.ConnectionError):
            raise exceptions.BackendError("Not able to contact backend API.")
    return wrapper

@catch_backend_http_error
def get(url):
    req = requests.get(url)
    req.raise_for_status()
    return req.json()

@catch_backend_http_error
def post(url, data):
    req = requests.post(url, data=json.dumps(data))
    req.raise_for_status()
    return req.json()

@catch_backend_http_error
def delete(url):
    req = requests.delete(url)
    req.raise_for_status()
    return req.json()