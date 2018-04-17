import domain
import general
import constants
from urllib.request import urlopen
from link_finder import Linkfinder
from urllib import error


class Spider:

    # Class variables (shared among all instances)
    project_name = ''
    crawled_name = ''
    base_url = ''
    domain_name = ''
    crawled_file = ''
    queue_file = ''
    dead_file = ''
    queue_set = set()
    crawled_set = set()
    dead_set = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = constants.QUEUE_FILE
        Spider.crawled_file = constants.CRAWLED_FILE
        Spider.dead_file = constants.DEAD_LINK_FILE

        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    @staticmethod
    def boot():
        general.create_project_dir(Spider.project_name)
        general.create_data_files(Spider.project_name, Spider.base_url)
        Spider.crawled_set = general.file_to_set(Spider.crawled_file)
        Spider.queue_set = general.file_to_set(Spider.queue_file)
        Spider.dead_set = general.file_to_set(Spider.dead_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled_set:
            print(thread_name + ' is now crawling ' + page_url)
            print(
                'Queue ' + str(len(Spider.queue_set))
                + ' | Crawled ' + str(len(Spider.crawled_set))
                + ' | Dead ' + str(len(Spider.dead_set))
            )

            Spider.add_links_to_queue(Spider.gather_links(page_url))

            if page_url in Spider.queue_set:
                Spider.queue_set.remove(page_url)

            Spider.crawled_set.add(page_url)

            # Update the files
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-type'):
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')

            # Get all links
            finder = Linkfinder(Spider.base_url, page_url)
            finder.feed(html_string)

        except error.HTTPError as e_http:
            if e_http.getcode() == 404:
                Spider.dead_set.add(page_url)
                print('Dead link: ' + page_url)
            else:
                print(str(e_http))
            return set()

        except Exception as e:
            print(str(e))
            return set()

        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:

            # Check we don't already have link
            if url in Spider.queue_set:
                continue
            if url in Spider.crawled_set:
                continue

            # Make sure we don't add a link that
            # points towards a different site
            if Spider.domain_name != domain.get_domain_name(url):
                continue

            # Add to waiting list
            Spider.queue_set.add(url)

    @staticmethod
    def update_files():
        general.set_to_file(Spider.queue_set, Spider.queue_file)
        general.set_to_file(Spider.crawled_set, Spider.crawled_file)
        general.set_to_file(Spider.dead_set, Spider.dead_file)
