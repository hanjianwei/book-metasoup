# -*- coding: utf-8 -*-

import os.path
from bs4 import BeautifulSoup
from .book import Book
from .client import Client


class Douban:
    def __init__(self):
        self.douban = Client()

    def book_by_isbn(self, isbn):
        return self.book_by_url(f"https://www.douban.com/isbn/{isbn}")

    def book_by_subject(self, subject):
        return self.book_by_url(f"https://book.douban.com/subject/{subject}")

    def book_by_url(self, url):
        # Request the book page
        r = self.douban.get(url)
        if r is None:
            return None

        # Parse html for metadata
        markup = r.text
        doc = BeautifulSoup(markup, "html.parser")
        info = doc.find(id="info").text.split()
        meta = {info[i][:-1]: info[i + 1] for i in range(0, len(info), 2)}

        print(meta)
        # Mapping to book fields
        identifiers = {
            "douban": os.path.basename(os.path.normpath(r.url)),
        }
        if "ISBN" in meta:
            identifiers["isbn"] = meta.get("ISBN")

        book = Book(
            identifiers=identifiers,
            cover_url=doc.find(id="mainpic").a.get("href"),
            title=doc.h1.text.strip(),
            authors=meta.get("作者").replace("/", "&"),
            publisher=meta.get("出版社"),
            pubdate=meta.get("出版年"),
            series=meta.get("丛书"),
            price=meta.get("定价"),
            comments=doc.find(id="link-report").text.strip(),
        )
        return book
