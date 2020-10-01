#!/usr/bin/env python3

import requests
from douban import Douban

if __name__ == "__main__":
    s = requests.Session()

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.60"
    }

    isbn = "9787533687557"
    subject = "30761557"

    # bk = Douban(isbn=isbn)
    bk = Douban(douban=subject)

    r = s.get(bk.url, headers=headers)
    # r = s.get('https://book.douban.com/subject/30761557/', headers = headers)
    bk.parse(r)

    print(r.url)

    print(bk.__dict__)

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
