# -*- coding: utf-8 -*-
import requests


class Client:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.60"
            }
        )

    def get(self, url):
        r = self.session.get(url)
        return r if r.status_code == requests.codes.ok else None
