# -*- coding: utf-8 -*-

import os.path
from bs4 import BeautifulSoup


class Douban:
    def __init__(self, **identifiers):
        self.isbn = identifiers.get('isbn')
        self.subject = identifiers.get('douban')

        if self.isbn is not None:
            self.url = 'https://www.douban.com/isbn/{}'.format(self.isbn)
        elif self.subject is not None:
            self.url = 'https://book.douban.com/subject/{}'.format(self.subject)
        else:
            self.url = None

    def parse(self, response):
        markup = response.text
        doc = BeautifulSoup(markup, 'html.parser')
        info = doc.find(id='info').text.split()
        meta = {info[i][:-1]: info[i + 1] for i in range(0, len(info), 2)}

        if self.subject is None:
            self.subject = os.path.basename(os.path.normpath(response.url))

        if self.isbn is None:
            self.isbn = meta.get('ISBN')

        self.cover = doc.find(id='mainpic').a.get('href')
        self.title = doc.h1.text.strip()
        self.author = meta.get('作者').replace('/', '&')
        self.publisher = meta.get('出版社')
        self.series = meta.get('丛书')
        self.price = meta.get('定价')
