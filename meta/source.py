import requests


class Source:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.60"
        }

    def req(self, url):
        r = self.session.get(url, headers=self.headers)
        return r if r.status_code == requests.codes.ok else None
