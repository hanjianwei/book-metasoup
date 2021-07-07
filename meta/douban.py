# -*- coding: utf-8 -*-

import os.path
from bs4 import BeautifulSoup
from .book import Book
from .source import Source


class Douban(Source):
    def __init__(self, **identifiers):
        super().__init__()

    def search(self, **query):
        isbn = query.get("isbn")
        subject = query.get("douban")

        # Get book URL
        if isbn is not None:
            url = "https://www.douban.com/isbn/{isbn}".format(query)
        elif subject is not None:
            url = "https://book.douban.com/subject/{douban}".format(query)
        else:
            return None

        # Request the book page
        r = self.req(url)
        if r is None:
            return None

        return self.parse(r)

    def parse(self, r):
        # Parse html for metadata
        markup = r.text
        doc = BeautifulSoup(markup, "html.parser")
        info = doc.find(id="info").text.split()
        meta = {info[i][:-1]: info[i + 1] for i in range(0, len(info), 2)}

        print(meta)
        # Mapping to book fields
        book = Book()

        book.subject = os.path.basename(os.path.normpath(r.url))
        book.isbn = meta.get("ISBN")
        book.cover = doc.find(id="mainpic").a.get("href")
        book.title = doc.h1.text.strip()
        book.authors = meta.get("作者").replace("/", "&")
        book.publisher = meta.get("出版社")
        book.pubdate = meta.get("出版年")
        book.series = meta.get("丛书")
        book.price = meta.get("定价")
        book.comments = doc.find(id="link-report").text.strip()

        return book
