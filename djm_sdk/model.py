import uuid
import re

def validate_uuid_v1(id):
    obj = uuid.UUID(id, version=1)
    return True


class Card:

    @staticmethod
    def validate_hidden_pan(hidden_pan):
        if re.match("X{12}[0-9]{4}", hidden_pan) is None:
            raise ValueError("Hidden PAN should be formatted as XXXXXXXXXXXX1234")
        return True

    @staticmethod
    def from_json(card_json):
        if not 'id' or not 'hidden_pan' in card_json:
            raise ValueError("A json represention of card should have two field id and hidden pan.")
        return Card(card_json['id'], card_json["hidden_pan"])

    def __init__(self, id, hidden_pan):
        validate_uuid_v1(id)
        Card.validate_hidden_pan(hidden_pan)
        self.id = id
        self.hidden_pan = hidden_pan

