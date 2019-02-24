import unittest

import domain


class DomainTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # get_sub_domain_name()
    def test_getSubdomainName_withEmptyString_returnEmptyString(self):
        self.assertEqual(domain.get_sub_domain_name(''), '')

    def test_getSubdomainName_withoutSchemeSpecifier_returnEmptyString(self):
        self.assertEqual(domain.get_sub_domain_name('www.google.com'), '')

    def test_getSubdomainName_withSchemeSpecifierHttp_returnSubdomain(self):
        self.assertEqual(domain.get_sub_domain_name('http://www.google.com'), 'www.google.com')

    def test_getSubdomainName_withSchemeSpecifierHttps_returnSubdomain(self):
        self.assertEqual(domain.get_sub_domain_name('https://www.google.com'), 'www.google.com')

    # get_domain_name()
    def test_getDomainName_withEmptyString_returnEmptyString(self):
        self.assertEqual(domain.get_domain_name(''), '')

    def test_getDomainName_withCompleteUrl_returnDomain(self):
        self.assertEqual(domain.get_domain_name('https://www.google.com'), 'google.com')

    def test_getDomainName_withSubdomain_returnDomain(self):
        self.assertEqual(domain.get_domain_name('https://test.google.com'), 'google.com')

    def test_getDomainName_withMultipleSubdomain_returnEmptyString(self):
        self.assertEqual(domain.get_domain_name('https://com.test.google.com'), 'google.com')

    def test_getDomainName_withoutSchemeSpecifier_returnEmptyString(self):
        self.assertEqual(domain.get_domain_name('www.google.com'), '')


if __name__ == '__main__':
    unittest.main()
