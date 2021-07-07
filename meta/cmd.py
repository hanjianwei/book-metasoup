#!/usr/bin/env python3

from .douban import Douban
from .calibre import Calibre

import sys


def is_supported_id_type(name):
    return name.lower() in ["isbn", "douban"]


def main():
    identifiers = sys.argv[1:]
    t = 'isbn'

    id_handlers = {
        'isbn': Douban(),
    }


    for id in identifiers:
        if is_supported_id_type(id):
            t = id
        else:
            pass

if __name__ == "__main__":
    main()


    # c = Calibre()
    # calibre_id = c.search_isbn(isbn)
    # print(calibre_id)

    # cmd = "calibredb add -e -t {title} -T HomeLibrary".format(title=title)

    # if "作者" in meta:
    #     cmd += " -a {作者}".format(**meta)
    # if "ISBN" in meta:
    #     cmd += " -i {ISBN}".format(**meta)
    #     # if '丛书' in meta:

    # # Download cover image
    # if img is not None:
    #     cover = meta["ISBN"] + img[-4:]
    #     with open(cover, "wb") as f:
    #         f.write(requests.get(img).content)
    #         cmd += " -c {cover}".format(cover=cover)

    # print(cmd)
