import unittest
import general
from unittest.mock import patch


class TestGeneral(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sanitize_url(self):
        self.assertEqual(general.sanitize_url(''), 'http://')
        self.assertEqual(general.sanitize_url('www.google.com'), 'http://www.google.com')
        self.assertEqual(general.sanitize_url('https://www.google.com'), 'https://www.google.com')
        self.assertEqual(general.sanitize_url('http://www.google.com'), 'http://www.google.com')


if __name__ == '__main__':
    unittest.main()