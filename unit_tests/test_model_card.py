import unittest

from djm_sdk import model
from djm_sdk import exceptions

class ModelCardTests(unittest.TestCase):

    def test_card_init(self):
        """ Card constructor should initialize attributes with the given values"""
        id = "e290b6aa-03a9-11eb-8b48-3c15c2c07228"
        pan = "XXXXXXXXXXXX1234"
        card = model.Card(id, pan)
        self.assertEqual(card.id, id)
        self.assertEqual(card.hidden_pan, pan)

    def test_card_validate_id(self):
        """ Card id should be UUID v1 valid."""
        id = "e290b6aa-03a9-11eb-8b48-3c15c2c07228"
        self.assertTrue(model.validate_uuid_v1(id))

    def test_card_validate_id_error(self):
        """ It should raise an error while an non conforme uuid is given."""
        id = "e290b6aa-03a9-11eb-8b48-3c15c2c07228"
        with self.assertRaises(ValueError):
            model.validate_uuid_v1("12")

    def test_card_validate_pan(self):
        """ It should return True while an hidden_pan is valid"""
        pan = "XXXXXXXXXXXX4567"
        self.assertTrue(model.Card.validate_hidden_pan(pan))

    def test_card_validate_pan_error(self):
        """ It should raise an error while an non conforme hidden-pan is given."""
        pan = "1234567891234567"
        with self.assertRaises(ValueError):
            model.Card.validate_hidden_pan(pan)


    def test_card_from_json(self):
        """ By giving a json repr of a Card, it should return a Card object"""
        card_json = {
            'id': "e290b6aa-03a9-11eb-8b48-3c15c2c07228",
            'hidden_pan': "XXXXXXXXXXXX0302"
        }
        card = model.Card.from_json(card_json)
        self.assertEqual(card_json["id"], card.id)
        self.assertEqual(card_json["hidden_pan"], card.hidden_pan)

    def test_card_from_json_error(self):
        """ By giving a non valid json repr of a Card, it should raise an error"""
        card_json = {
            'id': "e290b6aa-03a9-11eb-8b48-3c15c2c07228",
        }
        with self.assertRaises(ValueError):
            model.Card.from_json(card_json)

        card_json = {
        }
        with self.assertRaises(ValueError):
            model.Card.from_json(card_json)