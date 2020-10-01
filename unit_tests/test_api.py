import unittest
import unittest.mock
from unittest.mock import Mock

from djm_sdk import api
from djm_sdk import model

class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

    def raise_for_status(self):
        pass

class HttpTests(unittest.TestCase):

    def test_get_cards(self):
        """ Get cards should request it to backend and return a lsit of card objects"""
        cards_mock = [{'id': 'e290b6aa-03a9-11eb-8b48-3c15c2c07228', 'hidden_pan':'XXXXXXXXXXXX1234'}]
        with unittest.mock.patch("requests.get", return_value=MockResponse(cards_mock, 200)) as requests_mock:
            app = api.API("ip", "port")
            cards = app.get_cards('1234')
            for card in cards:
                self.assertIsInstance(card, model.Card)
            self.assertEqual(cards[0].id, 'e290b6aa-03a9-11eb-8b48-3c15c2c07228')
            self.assertEqual(cards[0].hidden_pan, 'XXXXXXXXXXXX1234')

    def test_delete_card(self):
        """ Get cards should request it to backend and return a lsit of card objects"""
        card_id_mock = {'id': 'e290b6aa-03a9-11eb-8b48-3c15c2c07228'}
        with unittest.mock.patch("requests.delete", return_value=MockResponse(card_id_mock, 200)) as requests_mock:
            app = api.API("ip", "port")
            card_id = app.delete_card('1234', 'e290b6aa-03a9-11eb-8b48-3c15c2c07228')
            self.assertEqual(card_id, 'e290b6aa-03a9-11eb-8b48-3c15c2c07228')