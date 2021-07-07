"""
❯ calibredb set_metadata -l
Title                                    Field name

ISBN                                     #isbn
Author sort                              author_sort
Authors                                  authors
Comments                                 comments
Cover                                    cover
Identifiers                              identifiers
Languages                                languages
Published                                pubdate
Publisher                                publisher
Rating                                   rating
Series                                   series
Series Index                             series_index
Size                                     size
Title sort                               sort
Tags                                     tags
Date                                     timestamp
Title                                    title
Cover                                    cover
"""


class Book:
    def __init__(self, **kwargs):
        if kwargs is not None:
            self.__dict__.update(kwargs)
