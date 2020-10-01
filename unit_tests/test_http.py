import unittest

from djm_sdk import exceptions
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
                

    def test_catch_backend_http_error_decorator(self):
        """ It should raise a custom exception"""

        @http.catch_backend_http_error
        def test(a):
            http.get("http://0.0.0.1:9089")
            return a
        
        with self.assertRaises(exceptions.BackendError):
            test(10)
