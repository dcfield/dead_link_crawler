from urllib.parse import urlparse


# Get domain name (example.com)
def get_domain_name(url):
    try:
        result = get_sub_domain_name(url).split('.')
        return result[-2] + '.' + result[-1]
    except:
        return ''


# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
