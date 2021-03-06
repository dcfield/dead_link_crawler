<<<<<<< HEAD
from app import general
=======
import app.general as general
>>>>>>> ed089c1901e184f5b8adc4209ca556ed6aa86aa6
import unittest


class GeneralTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sanitizeUrl_withEmptyString_returnHttp(self):
        self.assertEqual(general.sanitize_url(''), None)

    def test_sanitizeUrl_withoutHttp_returnUrlWithHttp(self):
        self.assertEqual(
            general.sanitize_url('www.google.com'),
            'http://www.google.com'
            )

    def test_sanitizeUrl_withHttps_returnSameInput(self):
        self.assertEqual(
            general.sanitize_url('https://www.google.com'),
            'https://www.google.com'
            )

    def test_sanitizeUrl_withHttp_returnSameInput(self):
        self.assertEqual(
            general.sanitize_url('http://www.google.com'),
            'http://www.google.com'
            )


if __name__ == '__main__':
    unittest.main()
