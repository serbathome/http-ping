
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import threading
import random
import time


def download_page(url):
    sleep_time = random.randint(1, 10)
    time.sleep(sleep_time)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for tag in soup.find_all(['link', 'script', 'img']):
        if tag.name == 'link' and tag.get('href'):
            resource_url = urljoin(url, tag['href'])
        elif tag.name == 'script' and tag.get('src'):
            resource_url = urljoin(url, tag['src'])
        elif tag.name == 'img' and tag.get('src'):
            resource_url = urljoin(url, tag['src'])
        else:
            continue
        r = requests.get(resource_url)
        if r.status_code != 200:
            print(f'Failed to download {resource_url}')
        else:
            print(f"Downloaded {resource_url}, caching status: {
                  r.headers.get('X-Cache')}")


if __name__ == '__main__':
    num_threads = 100
    url = 'https://uat.deltadentalins.com/shopping/aarp/get-a-quote'
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=download_page, args=([url]))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
