# -*- coding: utf-8 -*-
class Book:
    def __init__(
        self,
        title="",
        subtitle="",
        original_title=None,
        identifiers={},
        authors=[],
        translators=[],
        publisher="",
        pubdate=None,
        series=None,
        pages=0,
        price=0.0,
        binding=None,
        description=None,
        author_introduction=None,
        toc=None,
        languages=None,
        cover_url="",
        tags=[],
        rating=None,
        comments=None,
    ):
        self.title = title
        self.subtitle = subtitle
        self.original_title = original_title
        self.identifiers = identifiers
        self.authors = authors
        self.translators = translators
        self.publisher = publisher
        self.pubdate = pubdate
        self.series = series
        self.pages = pages
        self.price = price
        self.binding = binding
        self.description = description
        self.author_introduction = author_introduction
        self.languages = languages
        self.toc = toc
        self.cover_url = cover_url
        self.tags = tags
        self.rating = rating
        self.comments = comments
