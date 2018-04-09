from domain import *

# constants
PROJECT_NAME = 'dead_link_crawler_files'
HOMEPAGE = 'http://www.pythonanywhere.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
CRAWL_FILE_DIR = PROJECT_NAME
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
DEAD_LINK_FILE = PROJECT_NAME + '/dead.txt'
NUMBER_OF_THREADS = 4
