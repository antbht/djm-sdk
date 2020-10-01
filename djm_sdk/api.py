
from djm_sdk import http
from djm_sdk import model

class API:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.url = "http://{}:{}/".format(host, port)

    def get_cards(self, user_id):
        uri = f"users/{user_id}/cards"
        json_content = http.get(self.url+uri)
        return [model.Card.from_json(card_json) for card_json in json_content]
    
    
__all__=[
    API
]
