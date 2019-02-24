# Python Web Crawler
This script will gather all dead links in a particular website.

## Pre-requisites
- python 3

Install the python packages.
- pip3 install -r requirements.txt

## Run application
- `python3 ./app/main.py`
- Enter a website to crawl (Default is [http://www.pythonanywhere.com/])
- Go for coffee
- Check `./dead_link_crawler/dead_link_crawler_files/dead.txt` for a list of all dead links

## Run unit tests
- `cd app`
- `python3 -m pytest`