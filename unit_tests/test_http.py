import unittest

from djm_sdk import http

class HttpTests(unittest.TestCase):


    def test_get_raise_error(self):
        """ Connections error should be raised if appears"""

        with self.assertRaises(Exception):
            http.get("http://fail.test/uri")


    def test_delete_raise_error(self):
            """ Connections error should be raised if appears"""

            with self.assertRaises(Exception):
                http.delete("http://fail.test/uri")
                
