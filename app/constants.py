<<<<<<< HEAD
from domain import *
=======
import domain
>>>>>>> ed089c1901e184f5b8adc4209ca556ed6aa86aa6

# constants
PROJECT_NAME = 'dead_link_crawler_files'
HOMEPAGE = 'http://www.pythonanywhere.com/'
DOMAIN_NAME = domain.get_domain_name(HOMEPAGE)
CRAWL_FILE_DIR = PROJECT_NAME
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
DEAD_LINK_FILE = PROJECT_NAME + '/dead.txt'
NUMBER_OF_THREADS = 4
