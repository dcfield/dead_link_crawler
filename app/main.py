import threading
from queue import Queue
from app.spider import Spider
from app.general import *
from app.constants import *
import shutil


queue = Queue()


# Ask user for a URL to crawl
def ask_for_url():
    url = input("Enter url to crawl: ")
    return sanitize_url(url)


# Ask user what they want to do
def ask_for_input():
    if not file_exists(DEAD_LINK_FILE):
        return ask_for_url()
    else:
        response = input("Would you like to delete your history and restart the webcrawler?(Y/n): ")
        if response is "Y":
            shutil.rmtree(CRAWL_FILE_DIR)
            return ask_for_url()
    pass


# Overwrite HOMEPAGE if required
HOMEPAGE = ask_for_input() or HOMEPAGE
DOMAIN_NAME = get_domain_name(HOMEPAGE)

# Create a Spider
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# Create worker threads (will die when main finishes)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the net job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# Check if items exist in queue. If so, crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()


create_workers()
crawl()
