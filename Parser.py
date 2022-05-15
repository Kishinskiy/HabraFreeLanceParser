from time import sleep
from bs4 import BeautifulSoup as bs
from config import BASE_URL
import requests


class Parser:
    def __init__(self, header={'user-agent': 'my-app/0.0.1'}):
        self.header = header

    def __get_page(self, url):
        r = requests.get(url, headers=self.header)
        if r.status_code != 200:
            raise Exception('bad response', r.status_code)
        return r.text

    def __get_soup(self, URL):
        page = self.__get_page(URL)
        return bs(page, features="html.parser")

    def get_links_from_page(self, URL):
        posts = []
        soup = self.__get_soup(URL)
        links = soup.find_all(class_='tm-article-snippet__title-link')
        next_page = soup.find(id='pagination-next-page',
                              class_='tm-pagination__navigation-link tm-pagination__navigation-link_active')
        for link in links:
            title = link.text
            url = link.get('href')
            data = {title.strip(): BASE_URL + url}
            posts.append(data)
        return next_page, posts

    def get_links_from_all_pages(self):
        next_page = "start"
        n = 0
        while next_page is not None:
            sleep(5)
            n = n + 1
            URL = BASE_URL + f'ru/all/page{n}/'
            next_page, posts = self.get_links_from_page(URL)
            print(posts)
