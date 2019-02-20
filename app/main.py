import threading
import queue
import spider
import general
import constants
import domain
import shutil


QUEUE = queue.Queue()


# Ask user for a URL to csrawl
def ask_for_url():
    url = input("Enter url to crawl: ")
    return general.sanitize_url(url)


# Ask user what they want to do
def ask_for_input():
    if not general.file_exists(constants.DEAD_LINK_FILE):
        return ask_for_url()
    else:
        response = input(
            """Would you like to delete your history
            and restart the webcrawler?(Y/n): """
            )
        if response is "Y":
            shutil.rmtree(constants.CRAWL_FILE_DIR)
            return ask_for_url()
    pass


HOMEPAGE = ask_for_input() or constants.HOMEPAGE
DOMAIN_NAME = domain.get_domain_name(HOMEPAGE)


# Create a Spider
spider.Spider(constants.PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# Create worker threads (will die when main finishes)
def create_workers():
    for _ in range(constants.NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the net job in the queue
def work():
    while True:
        url = QUEUE.get()
        spider.Spider.crawl_page(threading.current_thread().name, url)
        QUEUE.task_done()


# Each queued link is a new job
def create_jobs():
    for link in general.file_to_set(constants.QUEUE_FILE):
        QUEUE.put(link)
        QUEUE.join()
    crawl()


# Check if items exist in queue. If so, crawl them
def crawl():
    queued_links = general.file_to_set(constants.QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()

create_workers()
crawl()
