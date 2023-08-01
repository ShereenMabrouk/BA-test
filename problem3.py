# Shereen Mabrouk 
'''
(3) A tool for extracting the URLs from either of www.curlie.org or www.wikipedia.org recursively (i.e., including sub-pages).
'''
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_soup(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for failed requests
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def extract_urls(url):
    soup = get_soup(url)
    base_url = urljoin(url, '/')

    urls = set()
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('/') or href.startswith(base_url):
            urls.add(urljoin(base_url, href))

    return urls

def recursive_extract_urls(url, max_depth=3, visited_urls=None, current_depth=0):
    if visited_urls is None:
        visited_urls = set()

    if current_depth > max_depth or url in visited_urls:
        return set()

    visited_urls.add(url)
    urls = extract_urls(url)

    sub_urls = set()
    for new_url in urls:
        sub_urls.update(recursive_extract_urls(new_url, max_depth, visited_urls, current_depth + 1))

    return urls.union(sub_urls)

def main():
    starting_url = 'https://www.wikipedia.org/'
    max_depth = 3

    print(f"Extracting URLs recursively from {starting_url} up to depth {max_depth}...")
    extracted_urls = recursive_extract_urls(starting_url, max_depth)

    print("\nExtracted URLs:")
    for url in extracted_urls:
        print(url)

if __name__ == "__main__":
    main()
