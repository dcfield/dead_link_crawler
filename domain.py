from urllib.parse import urlparse


# Get domain name (example.com)
def get_domain_name(url):
    """Get the domain name of a given url
    :param url: String containing the URL
    :return: String with domain name

    >>> get_domain_name('https://www.google.com')
    'google.com'
    >>> get_domain_name('http://www.google.com')
    'google.com'
    >>> get_domain_name('http://google.com')
    'google.com'

    This function only recognizes complete urls ie. with either http or https

    >>> get_domain_name('')
    ''
    >>> get_domain_name('www.google.com')
    ''

    """
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
