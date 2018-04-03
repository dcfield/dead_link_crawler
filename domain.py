# Python 2 and Python 3 compatible
try:
    from urllib.parse import urlparse
except ImportError as i:
    from urlparse import urlparse


# Get domain name (example.com)
def get_domain_name(url):
    # noinspection PyBroadException
    try:
        result = get_sub_domain_name(url).split('.')
        return result[-2] + '.' + result[-1]
    except Exception as e:
        return ''


# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    # noinspection PyBroadException
    try:
        return urlparse(url).netloc
    except Exception as e:
        return ''
